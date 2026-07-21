# Bridging Participation Gaps with Robotics 
# — Supplementary Materials

This repository contains the supplementary materials for the study **"Bridging Participation Gaps with Robotics: Empirical Evaluation of UDL and Usability Principles in an Educational Robot Prototype for Inclusive Education"**, submitted to *MedienPädagogik – Zeitschrift für Theorie und Praxis der Medienbildung*.

The study evaluates the prototype educational robot TOKADI (*Tool for Collaborative and Adaptive Didactics*) as a designed artefact along three dimensions: conformity with the Universal Design for Learning (UDL) principles, usability, and socio-emotional experience of learners in inclusive primary school classrooms. Data were collected in a mixed-methods design with N = 10 teachers and N = 137 students (aged 8–12) across six inclusive primary school classes at three schools.

The manuscript reports the core results; this repository provides the full instruments, analysis code, and detailed tables that could not be included in the article for reasons of length.

## Repository structure

```
├── README.md                                          this file
├── LICENSE                                            CC BY 4.0
├── instruments/
│   ├── UDL_Grid_TOKADI_DE.docx / .pdf                 UDL evaluation grid (26 items, German original)
│   └── UDL_Grid_TOKADI_EN.docx / .pdf                 English translation
├── tables/
│   ├── Table_S3_UDL_principle_descriptives.csv       aggregated per teacher (N = 10)
│   ├── Table_S5_UDL_considerations_all.csv           all 26 considerations, means and SDs
│   ├── Table_S7_socio_emotional_dimensions.csv       four a-priori dimensions + total (N = 139)
│   ├── Table_S8_subgroup_analyses.csv                Welch t comparisons on overall satisfaction (N = 137)
│   ├── Table_S9_SEN_operationalisations.csv          sensitivity analysis across four SEN definitions
│   ├── Table_S10_student_intervention_items.csv      five motivation items (N = 137)
│   └── Table_S11_teacher_intervention_outcomes.csv   seven items (N = 10) — see note below
└── analysis/
    ├── TOKADI_Analysis_v4.py                          full analysis script
    └── TOKADI_Analysis_v4_output.txt                  console output for reference
```

## What is in each folder

### `instruments/`

The UDL evaluation grid used in the teacher survey. It was derived from the 35 considerations of the **UDL Guidelines 3.0** (CAST 2024) by reviewing each consideration against the criterion of direct technological addressability. Nine considerations concerning purely curricular or pedagogical aspects were excluded, yielding 26 items across the three UDL principles: Engagement (9), Representation (7), and Action & Expression (10). Items are rated on a five-point Likert scale (1 = does not apply, 5 = fully applies). Overall internal consistency in the present sample was acceptable (α = .802); subscale-level reliabilities are reported in the manuscript and should be interpreted cautiously (Engagement α = .317, Representation α = .544, Action & Expression α = .726).

The German file is the original instrument as administered; the English version is a translation for international readers. Both include construction rationale, rating scale, and the two limitations noted in the manuscript (five checkpoint numbers assigned twice; N = 10 does not permit formal psychometric validation).

### `tables/`

Aggregated summary tables referenced in the manuscript by number. They contain the full descriptives and inferential results that the article reports only in condensed form. All CSVs are UTF-8 encoded with comma separators. Where multiple statistics are provided, the reference for each column is the analysis script.

- **Table S3** — Descriptive statistics of the three UDL principles at the aggregated per-teacher level (N = 10), including Cronbach's alpha per principle.
- **Table S5** — Descriptives for all 26 considerations individually (M, SD), sorted by principle and then descending mean rating.
- **Table S7** — Socio-emotional experience of the group activity: means, SDs, and medians for each of the four a-priori dimensions and for the total scale (N = 139). Cronbach's alpha is provided for context, though the a-priori dimensional structure was not supported by factor analysis and the instrument is reported unidimensionally in the manuscript.
- **Table S8** — Subgroup comparisons on students' overall intervention rating (Welch's t): gender, migration background, SEN, grade level, technology ownership, and prior robotics experience. Only the SEN comparison and prior-robotics comparison reach conventional significance thresholds; see the manuscript for the multiple-testing discussion.
- **Table S9** — Sensitivity analysis of the SEN subgroup effect across four operationalisations of educational need (from narrow to broad), with bootstrap 95 % CIs of the mean difference (10,000 resamples, seed = 42).
- **Table S10** — Descriptives for the five student motivation items (N = 137).
- **Table S11** — Teacher intervention outcome items (N = 10). *Note:* the individual-item teacher intervention data is stored in a separate teacher questionnaire file and is not included in the consolidated dataset used by the analysis script. The values shown in this CSV are therefore the summary statistics as reported in the manuscript, together with the scale midpoints and interpretation ranges. The one-sample t-test values reported in the manuscript (p = .004, d = -1.22 for the inclusion item) are noted in the source column. The consolidated teacher questionnaire dataset with row-level data will be provided together with the primary dataset on request.

### `analysis/`

The analysis script that reproduces all values reported in the article and all CSV tables above (except Table S11, see note). The script is written in Python 3.11 and reads the consolidated dataset, which is not part of this public repository. Anonymised access to the dataset is available on reasonable request in accordance with the participants' informed consent.

## Reproducibility

The analysis was run with **Python 3.11** and the following packages:

- `pandas` >= 2.0
- `numpy` >= 1.26
- `scipy` >= 1.11
- `openpyxl` (for reading the dataset)

All descriptive and inferential values reported in the manuscript reproduce exactly from the dataset when the script is executed. This includes SUS, UMUX, and Cronbach's α (overall and by subscale), the Friedman test on the UDL principles (χ²(2) = 11.40, p = .003; Kendall's W = .570), pairwise Wilcoxon comparisons (Representation − Action & Expression: MD = +0.48, T = 0.0, p = .002), the leave-one-out robustness analysis, the considerations-level Mann-Whitney comparison (U = 56.0, p = .044), the SEN subgroup comparison (t = -2.07, p = .040, d = -0.60) with its full robustness battery (Welch, Mann-Whitney U, bootstrap, leave-one-out, Benjamini-Hochberg FDR correction), the intraclass correlation and design effect for class-level clustering (ICC = .074; design effect 2.65), and the class-level ANOVA (F(5, 133) = 2.86, p = .017).

## Data availability

The consolidated de-identified dataset that underlies all analyses is not published in this repository. Anonymised access can be arranged on reasonable request; contact information is provided in the published version of the article.

## Notes on the reconstruction of the UDL grid

The instruments in this repository reflect the wording used in the study. The German UDL grid was reconstructed from the codebook of the consolidated dataset (sheet `00_Codebuch`); the item ordering follows the sequence recorded in the survey. Item wording for consideration 9.1 in the Engagement principle (Item f) was not stored verbatim in the codebook; the phrasing used here reflects the underlying consideration and matches how it was administered. The English version is a translation of the German original.

## Citation

If you use materials from this repository, please cite the article. Full citation will be added once the article is published.

For the UDL Guidelines referenced by the grid:

> CAST. 2024. *Universal Design for Learning Guidelines Version 3.0.* Wakefield, MA: CAST. https://udlguidelines.cast.org/

## Licence

All materials in this repository are made available under the **Creative Commons Attribution 4.0 International Licence (CC BY 4.0)**. You may share and adapt the materials for any purpose, including commercially, provided you give appropriate credit and indicate any changes.
