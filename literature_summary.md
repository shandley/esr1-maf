# ESR1 DBD Variants (185-210) and Estradiol Signaling: Literature Summary

## Background

Structural analysis places ESR1 residue 190 (Asp190) 52.45 Å from estradiol in the ligand-binding
domain (LBD), based on superimposition of the AlphaFold full-length model (AF-P03372-F1) onto the
3UUD crystal structure. Residue 190 sits in the DNA-binding domain (DBD, ~residues 185-253), which
is structurally separated from the LBD (~302-552) where estradiol binds.

This distance rules out direct contact between Asp190 and estradiol. However, the literature
supports indirect effects on estradiol-dependent transcription through a confirmed allosteric
mechanism operating at the DBD-LBD interface.

## Confirmed Findings

**Sources:** 22 primary literature sources fetched; 81 claims extracted; 25 verified (17 confirmed,
8 refuted by adversarial panel).

### 1. Residues around Asp190 form a critical DBD-LBD allosteric interface

Residues Y191, Y195, W200, G198, and V199 form a hydrophobic cluster at the DBD-LBD interface.
In the full-length receptor, W200 becomes substantially more buried than in isolated domains
(logPF = 2.14, hydroxyl radical protein footprinting). Asp190 sits within this cluster.

*Sources: Huang et al. 2018 (Nat Commun, PMC6117352); reviewed in J Lipid Res 2023 (PMC10388211)*

### 2. A bidirectional allosteric channel connects the LBD to this interface

LBD mutation N407A causes ~30% reduction in W200 fluorescence in the DBD. Disrupting this
interface via mutagenesis (I326A, Y328A, P406A, L409A) or small molecules suppresses
estradiol-induced transcription without altering estradiol binding affinity or coactivator binding.
The small molecule mitoxantrone (Kd ~1.6 uM) binds this same interface and suppresses transcription
including in constitutively active Y537S and D538G LBD mutants.

*Sources: PMC6117352; PMC12496009 (2025 extension); PMID 23737157 (computational support)*

### 3. Y191H (one position from Asp190) is a cancer-associated DBD variant with functional consequences

The Y191H mutation increases DNA-binding affinity ~3-fold (Kd: 9.2 nM to 3.2 nM by fluorescence
anisotropy) and elevates E2-induced transcriptional activity in luciferase reporter assays. Found in
endometrial cancer samples via TCGA/cBioPortal. Oncogenic function is not yet established.

*Source: Huang et al. 2018 (Nat Commun, PMC6117352)*

### 4. Other positions in the 185-210 window have large, verified effects on E2 transcription

| Residue | Variant | Effect | Source |
|---------|---------|--------|--------|
| K206 | K206A/G | Up to 200-fold super-activation at AP-1 sites with E2 | Nuclear Receptor 2004 (PMC446215) |
| K210 | K210A | 60% higher ERE transactivation than WT despite 5-10x lower DNA affinity | EMBO J (PMC1904296) |
| E203 | E203H | ~6-fold lower transactivation on AT vs. consensus ERE; ERE sequence-context dependent | EMBO J (PMC1904296) |
| DBD 2nd ZF | Various | Alter E2 and anti-estrogen responses at AP-1 collagenase promoter; required for ER-Stat5b cross-talk | JBC 2002 (PMID 12411447) |

### 5. The DBD is therapeutically validated in estradiol-dependent tumor biology

Electrophilic compounds targeting DBD zinc fingers inhibit estradiol-stimulated MCF-7 breast cancer
proliferation in vitro and reduce xenograft tumor mass in vivo.

*Source: Klinge et al. (Nat Med 2004, PMID 14702633)*

## What Is Not Confirmed

- No functional studies of **Asp190 specifically** were found. Evidence covers Y191 (adjacent) and
  the surrounding cluster. Whether D190 variants independently affect function is an open question.
- No GWAS or clinical association studies link DBD-region common polymorphisms (positions 185-210)
  to estrogen-related phenotypes (breast cancer risk, tamoxifen response, bone density, menopause
  timing). The only clinical data is the TCGA observation of Y191H in endometrial cancer (descriptive).

## Interpretation

The ultra-rare frequency of variants at positions 190-200 in our MAF query (gnomAD exome singletons
or absent; only rs776069453 at 5.7e-5 in 1KG) is consistent with strong purifying selection on this
region. These residues are not just structurally important for DNA binding but sit at a functionally
critical allosteric interface. Perturbations here can disrupt the hormonal signal relay from the LBD
to the transcriptional machinery without changing estradiol binding affinity.

The 52 Å distance between Asp190 and estradiol is accurate but not biologically sufficient as an
explanation. "Near the ligand" and "affects estradiol-dependent signaling" measure different things.

## Open Questions

1. Are there functional studies specifically characterizing Asp190 variants, or only adjacent Y191H?
2. Do common DBD-region polymorphisms in ESR1 associate with estrogen-related clinical phenotypes
   at the population level?
3. Is DBD-LBD allosteric communication intramolecular only, or can it operate in trans through the
   receptor homodimer interface?
4. Do DBD variants in this region alter SERM responses (tamoxifen, raloxifene) differently than
   estradiol responses?

## Methods

Deep research workflow: 5 parallel search angles (functional DBD studies, structural allostery,
Asp190-specific variants, population genetics, acquired cancer mutations), 22 sources fetched,
81 claims extracted, top 25 adversarially verified (3-vote panel per claim, 2/3 required to
confirm or refute).
