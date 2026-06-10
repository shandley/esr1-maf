"""
Calculates minimum distance from ESR1 residue 190 to estradiol.

Residue 190 is in the DBD, absent from LBD-only crystal structures.
Strategy: superimpose the AlphaFold full-length model (residues 1-595)
onto 3UUD (LBD + estradiol, residues 305-549) using shared Cα atoms,
then measure the distance from residue 190 to EST in the common frame.
"""

from pathlib import Path

import numpy as np
from Bio.PDB.Atom import Atom  # type: ignore[import-untyped]
from Bio.PDB.PDBParser import PDBParser  # type: ignore[import-untyped]
from Bio.PDB.Superimposer import Superimposer  # type: ignore[import-untyped]

STRUCTURE_DIR = Path("structure_data")
CRYSTAL_PDB = STRUCTURE_DIR / "3UUD.pdb"
ALPHAFOLD_PDB = STRUCTURE_DIR / "AF-P03372-F1.pdb"

TARGET_RESIDUE = 190
LIGAND_RESNUM = 600
ALIGN_RANGE = range(305, 550)  # LBD overlap between 3UUD and AlphaFold


def get_matched_ca(crystal_chain: object, af_chain: object) -> tuple[list[Atom], list[Atom]]:
    crystal_ca: list[Atom] = []
    af_ca: list[Atom] = []
    for resnum in ALIGN_RANGE:
        try:
            cr = crystal_chain[(" ", resnum, " ")]  # type: ignore[index]
            ar = af_chain[(" ", resnum, " ")]  # type: ignore[index]
            if cr.has_id("CA") and ar.has_id("CA"):
                crystal_ca.append(cr["CA"])
                af_ca.append(ar["CA"])
        except KeyError:
            pass
    return crystal_ca, af_ca


def min_residue_distance(res1: object, res2: object) -> tuple[float, str, str]:
    min_d = float("inf")
    min_a1 = min_a2 = ""
    for a1 in res1.get_atoms():  # type: ignore[union-attr]
        for a2 in res2.get_atoms():  # type: ignore[union-attr]
            d = float(np.linalg.norm(a1.get_vector().get_array() - a2.get_vector().get_array()))
            if d < min_d:
                min_d, min_a1, min_a2 = d, a1.get_name(), a2.get_name()
    return min_d, min_a1, min_a2


def main() -> None:
    parser = PDBParser(QUIET=True)

    crystal = parser.get_structure("crystal", CRYSTAL_PDB)
    alphafold = parser.get_structure("alphafold", ALPHAFOLD_PDB)

    crystal_chain = crystal[0]["A"]
    af_chain = alphafold[0]["A"]

    crystal_ca, af_ca = get_matched_ca(crystal_chain, af_chain)
    print(f"Superimposing on {len(crystal_ca)} matched Cα atoms (LBD residues 305-549)...")

    sup = Superimposer()
    sup.set_atoms(crystal_ca, af_ca)
    sup.apply(list(af_chain.get_atoms()))
    print(f"Superimposition RMSD: {sup.rms:.2f} Å")

    try:
        res_190 = af_chain[(" ", TARGET_RESIDUE, " ")]
    except KeyError:
        print(f"ERROR: Residue {TARGET_RESIDUE} not found in AlphaFold model.")
        return

    try:
        est = crystal_chain[("H_EST", LIGAND_RESNUM, " ")]
    except KeyError:
        print(f"ERROR: EST (residue {LIGAND_RESNUM}) not found in 3UUD chain A.")
        return

    min_d, atom_190, atom_est = min_residue_distance(res_190, est)

    print(f"\nESR1 residue {TARGET_RESIDUE} ({res_190.get_resname()}) → estradiol (EST)")
    print(f"  Minimum distance : {min_d:.2f} Å")
    print(f"  Closest atoms    : res190:{atom_190}  ↔  EST:{atom_est}")
    print(f"\nContext: residue 190 is in the DNA-binding domain; estradiol binds")
    print(f"the ligand-binding domain (~305-549). A distance > 30 Å is expected.")


if __name__ == "__main__":
    main()
