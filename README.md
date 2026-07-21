# Bridging Participation Gaps with Robotics — Supplementary Materials

This repository contains the supplementary materials for the study **"Bridging Participation Gaps with Robotics: Empirical Evaluation of UDL and Usability Principles in an Educational Robot Prototype for Inclusive Education"**, submitted to *MedienPädagogik – Zeitschrift für Theorie und Praxis der Medienbildung*.

The study evaluates the prototype educational robot TOKADI (*Tool for Collaborative and Adaptive Didactics*) as a designed artefact along three dimensions: conformity with the Universal Design for Learning (UDL) principles, usability, and socio-emotional experience of learners in inclusive primary school classrooms. Data were collected in a mixed-methods design with N = 10 teachers and N = 137 students (ages 8–12) across six inclusive primary school classes.

The manuscript reports the core results; this repository provides the full instruments, analysis code, and detailed tables that could not be included in the article for reasons of length.

## Repository structure

```
├── README.md                                 this file
├── instruments/
│   ├── UDL_Grid_TOKADI_DE.docx               the UDL evaluation grid (26 items, German original)
│   └── UDL_Grid_TOKADI_EN.docx               English translation of the grid
├── tables/
│   ├── Table_03_UDL_principle_descriptives.csv
│   ├── Table_05_UDL_considerations_all.csv
│   ├── Table_07_socio_emotional_dimensions.csv
│   ├── Table_08_subgroup_analyses.csv
│   ├── Table_09_SEN_operationalisations.csv
│   ├── Table_10_student_intervention_items.csv
│   └── Table_11_teacher_intervention_outcomes.csv
└── analysis/
    ├── TOKADI_Analyse_v4.py                  full analysis script
    └── TOKADI_Analysis_v4_output.txt         console output for reference
```

## What is in each folder

### `instruments/`

The UDL evaluation grid used in the teacher survey. It was derived from the 35 considerations of the **UDL Guidelines 3.0** (CAST 2024) by reviewing each consideration against the criterion of direct technological addressability. Nine considerations concerning purely curricular or pedagogical aspects were excluded, yielding 26 items across the three UDL principles: Engagement (9), Representation (7), and Action & Expression (10). Items are rated on a five-point Likert scale (1 = does not apply, 5 = fully applies). Overall internal consistency in the present sample was acceptable (α = .802); subscale-level reliabilities are reported in the manuscript and should be interpreted cautiously (Engagement α = .317, Representation α = .544, Action & Expression α = .726).

The German file is the original instrument as administered; the English version is a translation for international readers. Both include construction rationale, rating scale, and the two limitations noted in the manuscript (five checkpoint numbers assigned twice; N = 10 does not permit formal psychometric validation).

### `tables/`

Tables referenced in the manuscript by number. They contain the full descriptives and inferential results that the article reports only in condensed form.

- **Table 3** — Descriptive statistics of the three UDL principles at the aggregated level (N = 10).
- **Table 5** — Descriptives for all 26 considerations individually, ordered from highest to lowest mean rating.
- **Table 7** — Socio-emotional experience of the group activity: means, SDs, and medians for each of the four a-priori dimensions and for the total scale (N = 139).
- **Table 8** — Subgroup comparisons on students' overall intervention rating (Welch t-tests and Mann-Whitney U): gender, migration background, SEN, grade level, technology ownership, prior robotics experience.
- **Table 9** — Sensitivity analysis of the SEN subgroup effect across four operationalisations of educational need (from a narrow to a broad definition), with bootstrap 95 % CIs of the mean difference (10,000 resamples).
- **Table 10** — Descriptives for the ten student intervention items (N = 137).
- **Table 11** — Descriptives, one-sample t-tests against the scale midpoint, and effect sizes for the eight teacher intervention outcome items (N = 10), including the two items on which the manuscript's central dissociation finding rests (perceived usefulness and perceived contribution to inclusion).

### `analysis/`

The analysis script that reproduces all values reported in the article and in this repository. The script is written in Python 3 and reads the consolidated dataset (which is not part of this public repository; anonymised access is available on request in accordance with the participants' informed consent).

## Reproducibility

The analysis was run with **Python 3.11** and the following packages:

- `pandas` ≥ 2.0
- `numpy` ≥ 1.26
- `scipy` ≥ 1.11
- `openpyxl` (for reading the dataset)

All descriptive and inferential values reported in the manuscript reproduce exactly from the dataset when the script is executed. This includes SUS, UMUX, and Cronbach's α (overall and by subscale), the Friedman test on the UDL principles (χ²(2) = 11.40, p = .003; Kendall's W = .570), the SEN subgroup comparison (t = −2.07, p = .040, d = −0.60), the intraclass correlation and design effect for the class-level clustering (ICC = .074; deff = 2.65), and the class-level ANOVA (F(5,133) = 2.86, p = .017), together with the robustness analyses (Welch, Mann-Whitney, bootstrap, leave-one-out, Benjamini-Hochberg FDR correction, and the considerations-level Mann-Whitney U = 56.0, p = .044).

## Data availability

The consolidated dataset that underlies all analyses is not published in this repository. Anonymised access can be arranged on reasonable request; contact information is provided in the published version of the article.

## Citation

If you use materials from this repository, please cite the article:

> *Full citation will be added once the article is published.*

For the UDL Guidelines referenced by the grid:

> CAST. 2024. *Universal Design for Learning Guidelines Version 3.0.* Wakefield, MA: CAST. https://udlguidelines.cast.org/

## Licence

All materials in this repository are made available under the **Creative Commons Attribution 4.0 International Licence (CC BY 4.0)**, consistent with the journal's open-access policy. You may share and adapt the materials for any purpose, including commercially, provided you give appropriate credit and indicate any changes.
