"""Query Ensembl REST API for ESR1 variant MAF at specified amino acid positions."""

import csv
import sys
import time
from pathlib import Path
from typing import Any

import requests

ENSEMBL_REST = "https://rest.ensembl.org"
PROTEIN_ID = "ENSP00000206249"  # ESR1 MANE Select translation
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
OUTPUT_FIELDS = ["aa_position", "rsid", "consequence_type", "allele_string", "1kg_all_af", "gnomad_exomes_af", "gnomad_genomes_af"]


def get_translation_variants(protein_id: str) -> list[dict[str, Any]]:
    url = f"{ENSEMBL_REST}/overlap/translation/{protein_id}"
    r = requests.get(url, headers=HEADERS, params={"feature": "transcript_variation"}, timeout=60)
    r.raise_for_status()
    return r.json()  # type: ignore[no-any-return]


def get_population_frequencies(rsid: str, alt_alleles: set[str]) -> dict[str, float | None]:
    url = f"{ENSEMBL_REST}/variation/homo_sapiens/{rsid}"
    r = requests.get(url, headers=HEADERS, params={"pops": 1}, timeout=30)
    if r.status_code != 200:
        return {"1kg_all_af": None, "gnomad_exomes_af": None, "gnomad_genomes_af": None}

    result: dict[str, float | None] = {"1kg_all_af": None, "gnomad_exomes_af": None, "gnomad_genomes_af": None}
    for pop in r.json().get("populations", []):
        population: str = pop.get("population", "")
        allele: str = pop.get("allele", "")
        freq: float | None = pop.get("frequency")

        if allele not in alt_alleles:
            continue

        if population == "1000GENOMES:phase_3:ALL":
            result["1kg_all_af"] = freq
        elif population == "gnomADe:ALL":
            result["gnomad_exomes_af"] = freq
        elif population == "gnomADg:ALL":
            result["gnomad_genomes_af"] = freq

    return result


def load_positions(path: Path) -> set[int]:
    return {int(line.strip()) for line in path.read_text().splitlines() if line.strip()}


def run(positions_file: Path, output_file: Path) -> None:
    positions = load_positions(positions_file)
    print(f"Querying {len(positions)} positions in {PROTEIN_ID}...", file=sys.stderr)

    all_variants = get_translation_variants(PROTEIN_ID)
    relevant = [v for v in all_variants if v.get("start") in positions]
    print(f"Found {len(relevant)} variant(s) at target positions.", file=sys.stderr)

    rows: list[dict[str, Any]] = []
    for i, variant in enumerate(relevant):
        rsid: str = variant.get("id", "")
        if not rsid.startswith("rs"):
            continue  # No rsID — skip (no frequency data available)

        aa_pos: int = variant["start"]
        allele_string: str = variant.get("allele", "")
        consequence: str = variant.get("type", "")
        parts = allele_string.split("/")
        alt_alleles = set(parts[1:]) if len(parts) > 1 else set()

        print(f"  [{i + 1}/{len(relevant)}] {rsid} at aa{aa_pos}...", file=sys.stderr)
        freqs = get_population_frequencies(rsid, alt_alleles)
        time.sleep(0.07)  # Stay well under Ensembl's 15 req/sec limit

        rows.append({
            "aa_position": aa_pos,
            "rsid": rsid,
            "consequence_type": consequence,
            "allele_string": allele_string,
            "1kg_all_af": freqs["1kg_all_af"],
            "gnomad_exomes_af": freqs["gnomad_exomes_af"],
            "gnomad_genomes_af": freqs["gnomad_genomes_af"],
        })

    rows.sort(key=lambda r: (r["aa_position"], r["rsid"]))

    with output_file.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUTPUT_FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Done. {len(rows)} row(s) written to {output_file}", file=sys.stderr)


if __name__ == "__main__":
    positions_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("positions.txt")
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("esr1_maf_results.tsv")
    run(positions_path, output_path)
