# Bridging Participation Gaps with Robotics 
# — Supplementary Materials

This repository contains the supplementary materials for the study **"Bridging Participation Gaps with Robotics: Empirical Evaluation of UDL and Usability Principles in an Educational Robot Prototype for Inclusive Education"**, submitted to *MedienPädagogik – Zeitschrift für Theorie und Praxis der Medienbildung*.

The study evaluates the prototype educational robot TOKADI (*Tool for Collaborative and Adaptive Didactics*) as a designed artefact along three dimensions: conformity with the Universal Design for Learning (UDL) principles, usability, and socio-emotional experience of learners in inclusive primary school classrooms. Data were collected in a mixed-methods design with N = 10 teachers and N = 137 students (aged 8–12) across six inclusive primary school classes at three schools.

The manuscript reports the core results; this repository provides the UDL evaluation grid, the analysis script, and the extended tables that could not be included in the article for reasons of length.

## Repository contents

```
├── README.md                                          this file, including all supplementary tables
├── LICENSE                                            CC BY 4.0
├── instruments/
│   ├── UDL_Grid_TOKADI_DE.docx / .pdf                 UDL evaluation grid (26 items, German original)
│   └── UDL_Grid_TOKADI_EN.docx / .pdf                 English translation
└── analysis/
    └── TOKADI_Analysis.py                          full analysis script (Python 3.11)
```

## The UDL evaluation grid (`instruments/`)

The UDL evaluation grid used in the teacher survey was derived from the 35 considerations of the **UDL Guidelines 3.0** (CAST 2024) by reviewing each consideration against the criterion of direct technological addressability. Nine considerations concerning purely curricular or pedagogical aspects were excluded, yielding 26 items across the three UDL principles: Engagement (9), Representation (7), and Action & Expression (10). Items are rated on a five-point Likert scale (1 = does not apply, 5 = fully applies). Overall internal consistency in the present sample is acceptable (α = .802); subscale reliabilities are limited (Engagement α = .317, Representation α = .544, Action & Expression α = .726) and are interpreted descriptively in the manuscript.

The German file is the original instrument as administered; the English version is a translation for international readers. Both include construction rationale, rating scale, and the two limitations noted in the manuscript (five checkpoint numbers assigned twice; N = 10 does not permit formal psychometric validation).

## The analysis script (`analysis/`)

`TOKADI_Analysis.py` reproduces all values reported in the article and all tables below. It reads the consolidated de-identified dataset and computes the descriptive statistics, reliability coefficients, inferential tests, and robustness analyses. The dataset itself is not published here (see *Data availability* below).

Required environment:

- Python 3.11
- `pandas` >= 2.0
- `numpy` >= 1.26
- `scipy` >= 1.11
- `openpyxl` (for reading the dataset)

## Supplementary tables

All tables reproduce from the consolidated dataset with a random seed of 42 for bootstrap procedures.

### Table S3. UDL principle descriptives (N = 10 teachers)

Aggregated per teacher across the considerations of each principle.

| UDL principle | Items | M | SD | Min | Max | Cronbach's α |
|---|---|---|---|---|---|---|
| Engagement | 9 | 4.31 | 0.26 | 3.89 | 4.78 | 0.317 |
| Representation | 7 | 4.56 | 0.26 | 4.00 | 4.71 | 0.544 |
| Action & Expression | 10 | 4.08 | 0.36 | 3.40 | 4.50 | 0.726 |

### Table S5. All 26 considerations (N = 10 teachers)

Ordered by principle, then by descending mean. «(2nd)» marks the second item mapped to the same consideration number; the manuscript notes this in the Limitations section (five checkpoint numbers assigned twice).

| Principle | Consideration | M | SD |
|---|---|---|---|
| Action & Expression | 6.4 | 4.60 | 0.52 |
| Action & Expression | 6.1 | 4.60 | 0.52 |
| Action & Expression | 4.2 | 4.60 | 0.70 |
| Action & Expression | 4.1 | 4.40 | 0.52 |
| Action & Expression | 5.1 | 4.40 | 0.52 |
| Action & Expression | 6.5 | 3.90 | 0.99 |
| Action & Expression | 5.2 | 3.90 | 0.74 |
| Action & Expression | 6.4 (2nd) | 3.80 | 0.42 |
| Action & Expression | 4.1 (2nd) | 3.40 | 0.84 |
| Action & Expression | 4.2 (2nd) | 3.20 | 0.79 |
| Engagement | 9.1 | 4.70 | 0.48 |
| Engagement | 9.2 | 4.70 | 0.48 |
| Engagement | 8.3 (2nd) | 4.60 | 0.52 |
| Engagement | 7.1 | 4.50 | 0.85 |
| Engagement | 8.4 | 4.40 | 0.52 |
| Engagement | 9.3 | 4.30 | 0.48 |
| Engagement | 7.2 | 4.30 | 0.48 |
| Engagement | 7.3 | 3.70 | 1.06 |
| Engagement | 8.3 | 3.60 | 0.70 |
| Representation | 3.2 | 4.80 | 0.42 |
| Representation | 1.1 | 4.80 | 0.42 |
| Representation | 1.2 (2nd) | 4.80 | 0.42 |
| Representation | 2.5 | 4.70 | 0.48 |
| Representation | 1.2 | 4.40 | 0.52 |
| Representation | 2.1 | 4.20 | 0.79 |
| Representation | 2.3/2.4 | 4.20 | 0.42 |

### Table S7. Socio-emotional experience — dimensional structure (N = 139)

Four a-priori dimensions and the overall scale. The a-priori dimensional structure was not supported by factor analysis (see manuscript, Instruments); the instrument is therefore reported as an essentially unidimensional scale (α = .837).

| Dimension | Items | M | SD | Median | Cronbach's α |
|---|---|---|---|---|---|
| Intrinsic motivation & emotional response (Items 1, 5) | 2 | 0.60 | 0.49 | 1.00 | 0.571 |
| Social embeddedness (Items 2, 3, 4) | 3 | 0.51 | 0.51 | 0.67 | 0.580 |
| Voice and participation (Items 6, 7) | 2 | 0.56 | 0.54 | 0.50 | 0.348 |
| Openness to new / self-efficacy (Items 8, 9) | 2 | 0.57 | 0.56 | 1.00 | 0.609 |
| Overall (all 9 items) | 9 | 0.55 | 0.44 | 0.67 | 0.837 |

### Table S8. Subgroup comparisons on students' overall intervention rating (N = 137)

Welch's t on the five-item overall satisfaction scale.

| Comparison | n₁ | n₂ | M₁ | M₂ | Welch t | p | Cohen's d |
|---|---|---|---|---|---|---|---|
| Girls vs. boys | 67 | 70 | 4.19 | 4.30 | -0.75 | 0.457 | -0.13 |
| Migration bg vs. not | 77 | 60 | 4.24 | 4.26 | -0.15 | 0.884 | -0.03 |
| SEN (definition B) vs. not | 13 | 124 | 3.80 | 4.30 | -1.98 | 0.068 | -0.60 |
| Grade 3 vs. Grade 4 | 94 | 43 | 4.20 | 4.34 | -0.98 | 0.331 | -0.17 |
| Owns tech vs. not | 119 | 18 | 4.24 | 4.28 | -0.14 | 0.887 | -0.04 |
| Prior robotics vs. none | 16 | 121 | 4.51 | 4.21 | 2.35 | 0.024 | 0.36 |

### Table S9. Sensitivity analysis: alternative operationalisations of SEN (N = 137)

Effect of the SEN comparison on students' overall satisfaction under four defensible operationalisations, from a narrow (documented special educational need only) to a broad (any support need, including migration background) definition. Bootstrap 95 % CIs of the mean difference, 10,000 resamples, seed = 42.

| Operationalisation | n with | M with | M without | Welch t | p | Cohen's d | 95 % CI |
|---|---|---|---|---|---|---|---|
| A: SEN (Def. B, narrow) | 13 | 3.80 | 4.30 | -1.98 | 0.068 | -0.60 | [-0.98, -0.04] |
| B: SEN + language support | 19 | 3.93 | 4.30 | -1.97 | 0.059 | -0.45 | [-0.75, -0.02] |
| C: SEN + migration bg | 83 | 4.17 | 4.36 | -1.32 | 0.188 | -0.23 | [-0.46, 0.1] |
| D: broad support need | 83 | 4.17 | 4.36 | -1.32 | 0.188 | -0.23 | [-0.46, 0.1] |

### Table S10. Student intervention items — descriptives (N = 137)

Five-item motivation questionnaire, six-point scale (0 = not at all, 5 = very much), Cronbach's α = .886.

| Item | M | SD | N |
|---|---|---|---|
| Enjoyed playing with TOKADI | 4.42 | 0.86 | 137 |
| Enjoyed playing together with classmates | 4.29 | 1.05 | 137 |
| Would like to play with TOKADI again | 4.40 | 0.97 | 137 |
| Learned something new | 3.88 | 1.08 | 137 |
| Felt good during the activity | 4.25 | 1.03 | 137 |

### Table S11. Teacher intervention outcome items (N = 10)

*Note:* the individual-item teacher intervention data is stored in a separate teacher questionnaire file and is not included in the consolidated dataset used by the analysis script. The values below are the summary statistics as reported in the manuscript, together with the scale midpoints and interpretation ranges. The consolidated teacher questionnaire dataset will be provided together with the primary dataset on request.

| Item | Scale | M | Note |
|---|---|---|---|
| Overall usefulness of the programme | 0–10 | 8.70 | reported in manuscript |
| Likelihood of continuing the programme | 0–10 | 8.70 | reported in manuscript |
| Perceived student motivation | 1–5 | 4.20 | «sehr motiviert» |
| Helpfulness for students with SEN | 1–6 (+ n/a) | — | inclusion-cluster item, not individually reported |
| Helpfulness for students usually excluded | 1–6 (+ n/a) | 2.80 | «wenig-etwas hilfreich» |
| Promotion of group cohesion | 1–5 | — | inclusion-cluster item (α = .182); not individually reported |
| Promotion of inclusion in the class | 1–5 | 2.10 | one-sample t against midpoint: p = .004, d = −1.22 («geringe Wirkung») |

## Data availability

The consolidated de-identified dataset that underlies all analyses is not published in this repository. Anonymised access can be arranged on reasonable request; contact information is provided in the published version of the article.

## Notes on the reconstruction of the UDL grid

The instruments in this repository reflect the wording used in the study. The German UDL grid was reconstructed from the codebook of the consolidated dataset; the item ordering follows the sequence recorded in the survey. Item wording for consideration 9.1 in the Engagement principle (Item f) was not stored verbatim in the codebook; the phrasing used here reflects the underlying consideration and matches how it was administered. The English version is a translation of the German original.

## Citation

If you use materials from this repository, please cite the article. Full citation will be added once the article is published.

For the UDL Guidelines referenced by the grid:

> CAST. 2024. *Universal Design for Learning Guidelines Version 3.0.* Wakefield, MA: CAST. https://udlguidelines.cast.org/

## Licence

All materials in this repository are made available under the **Creative Commons Attribution 4.0 International Licence (CC BY 4.0)**. You may share and adapt the materials for any purpose, including commercially, provided you give appropriate credit and indicate any changes.
