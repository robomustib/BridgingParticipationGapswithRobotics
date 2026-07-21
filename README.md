# Bridging Participation Gaps with Robotics — Supplementary Materials

This repository contains the supplementary materials for the study **"Bridging Participation Gaps with Robotics: Empirical Evaluation of UDL and Usability Principles in an Educational Robot Prototype for Inclusive Education"**, submitted to *MedienPädagogik – Zeitschrift für Theorie und Praxis der Medienbildung*.

The study evaluates the prototype educational robot TOKADI (*Tool for Collaborative and Adaptive Didactics*) as a designed artefact along three dimensions: conformity with the Universal Design for Learning (UDL) principles, usability, and socio-emotional experience of learners in inclusive primary school classrooms. Data were collected in a mixed-methods design with N = 10 teachers and N = 137 students (aged 8–12; N = 139 for the group-activity survey) across six inclusive primary school classes at three schools.

The manuscript reports the core results; this repository provides the UDL evaluation grid, the analysis script, and the extended tables that could not be included in the article for reasons of length.

## Repository contents

```
├── README.md                                          this file, including all supplementary tables
├── LICENSE                                            CC BY 4.0
├── instruments/
│   ├── UDL_Grid_TOKADI_DE.docx / .pdf                 UDL evaluation grid (26 items, German original)
│   └── UDL_Grid_TOKADI_EN.docx / .pdf                 English translation
└── analysis/
    └── TOKADI_Analysis_v4.py                          full analysis script (Python 3.11)
```

## The UDL evaluation grid (`instruments/`)

The UDL evaluation grid used in the teacher survey was derived from the 35 considerations of the **UDL Guidelines 3.0** (CAST 2024) by reviewing each consideration against the criterion of direct technological addressability. Nine considerations concerning purely curricular or pedagogical aspects were excluded, yielding 26 items across the three UDL principles: Engagement (9), Representation (7), and Action & Expression (10). Items are rated on a five-point Likert scale (1 = does not apply, 5 = fully applies). Overall internal consistency in the present sample is acceptable (α = .802); subscale reliabilities are limited (Engagement α = .317, Representation α = .544, Action & Expression α = .726) and are interpreted descriptively in the manuscript.

The German file is the original instrument as administered; the English version is a translation for international readers. Both include construction rationale, rating scale, and the two limitations noted in the manuscript (five checkpoint numbers assigned twice; N = 10 does not permit formal psychometric validation).

## The analysis script (`analysis/`)

`TOKADI_Analysis_v4.py` reproduces the values reported in the article and the tables below, with three exceptions noted at the respective tables: Table S11 (teacher intervention items, not in the consolidated dataset), the STEM-interest row of Table S8, and the n = 14 operationalisation in Table S9. It reads the consolidated de-identified dataset and computes the descriptive statistics, reliability coefficients, inferential tests, and robustness analyses. The dataset itself is not published here (see *Data availability* below).

Required environment:

- Python 3.11
- `pandas` >= 2.0
- `numpy` >= 1.26
- `scipy` >= 1.11
- `openpyxl` (for reading the dataset)

## Supplementary tables

The tables below are reproduced verbatim from the manuscript before shortening and keep their original table numbers with an "S" prefix. Tables 1, 2, 6, and 12 remain in the article (there renumbered as Tables 1–4), hence the gaps in the sequence (no S1, S2, S6, S12).

### Table S3. Descriptive statistics of the UDL principle ratings (N = 10)

| UDL principle | Items | M | SD | Range | 95 % CI |
|---|---|---|---|---|---|
| Engagement | 9 | 4.31 | 0.26 | 3.89–4.78 | [4.13, 4.49] |
| Representation | 7 | 4.56 | 0.26 | 4.00–4.71 | [4.37, 4.75] |
| Action & Expression | 10 | 4.08 | 0.36 | 3.40–4.50 | [3.82, 4.34] |

### Table S4. Pairwise comparisons of the UDL principles

Wilcoxon signed-rank tests with Bonferroni correction (α = .0167).

| Comparison | MD | T | p | Significant (α = .0167) |
|---|---|---|---|---|
| Representation − Action & Expression | +0.477 | 0.0 | .002 | yes |
| Representation − Engagement | +0.246 | 7.0 | .037 | no |
| Engagement − Action & Expression | +0.231 | 12.0 | .123 | no |

### Table S5. All 26 considerations, ordered by mean (N = 10)

Five consideration numbers are assigned twice to different items (1.2, 4.1, 4.2, 6.4, 8.3); the manuscript notes this in the Limitations section. The full item wording is provided in the grid documents in `instruments/`.

| Principle / Consideration | Item (abbreviated) | M | SD |
|---|---|---|---|
| Representation 3.2 | Consistent response to input, cause-effect relations | 4.80 | 0.42 |
| Representation 1.1 | Adjustable perceptual settings (volume, light intensity) | 4.80 | 0.42 |
| Representation 1.2 | Tactile components (buttons, 3D-printed parts) | 4.80 | 0.42 |
| Engagement 9.1 | Successful work strengthens confidence and self-efficacy | 4.70 | 0.48 |
| Engagement 9.2 | Anthropomorphic design facilitates emotional bond | 4.70 | 0.48 |
| Representation 2.5 | Clear status feedback via LED matrix | 4.70 | 0.48 |
| Engagement 8.3 | Shared use fosters a sense of community | 4.60 | 0.52 |
| Action & Expr. 6.4 | Encourages trying out and developing strategies | 4.60 | 0.52 |
| Action & Expr. 6.1 | Recording function fosters strategic planning | 4.60 | 0.52 |
| Action & Expr. 4.2 | Compatible with additional materials (symbol, role cards) | 4.60 | 0.70 |
| Engagement 7.1 | Varied input options (buttons, clapping, whistling) | 4.50 | 0.85 |
| Engagement 8.4 | Feedback (LEDs, sounds, movement) motivating | 4.40 | 0.52 |
| Representation 1.2 | Multimodal presentation (visual, acoustic, tactile) | 4.40 | 0.52 |
| Action & Expr. 4.1 | Varied modes of operation | 4.40 | 0.52 |
| Action & Expr. 5.1 | Language-independent control via symbols | 4.40 | 0.52 |
| Engagement 9.3 | Prompts reflection on own actions | 4.30 | 0.48 |
| Engagement 7.2 | Feedback prompts reflection | 4.30 | 0.48 |
| Representation 2.1 | Symbols, lights, sounds intuitively designed | 4.20 | 0.79 |
| Representation 2.3 / 2.4 | Non-verbal elements independent of language | 4.20 | 0.42 |
| Action & Expr. 6.5 | Modular technology reduces barriers | 3.90 | 0.99 |
| Action & Expr. 5.2 | Functions adaptable to different learning goals | 3.90 | 0.74 |
| Action & Expr. 6.4 | Progress and actions clearly displayed | 3.80 | 0.42 |
| Engagement 7.3 | Assembly/reconstruction fosters playful learning | 3.70 | 1.06 |
| Engagement 8.3 | Supports collaborative learning with several students | 3.60 | 0.70 |
| Action & Expr. 4.1 | Modular construction eases adaptation | 3.40 | 0.84 |
| Action & Expr. 4.2 | Open-source documentation and build instructions | 3.20 | 0.79 |

### Table S7. Dimensions of learning motivation and social interaction (N = 137)

Five-item motivation questionnaire, six-point scale (0 = not at all, 5 = very much), Cronbach's α = .886.

| Dimension | Items | M | SD | Median |
|---|---|---|---|---|
| Intrinsic motivation & emotional response | 1, 5 | 4.34 | 0.86 | 4.5 |
| Social involvement & collaboration | 2 | 4.29 | 1.05 | 5.0 |
| Sustained learning effectiveness & transfer | 3, 4 | 4.14 | 0.89 | 4.5 |
| Overall satisfaction | 1–5 | 4.25 | 0.83 | 4.6 |

### Table S8. Group comparisons in overall satisfaction

Independent-samples t-tests on the five-item overall satisfaction scale; * p < .05. The special-educational-needs comparison is examined further in Table S9 and in the robustness analyses reported in the manuscript. The STEM-interest row is not part of the script's group-comparison module and is reproduced from the manuscript.

| Characteristic | Group 1 | Group 2 | t | p | d |
|---|---|---|---|---|---|
| Gender | girls (67) 4.19 | boys (70) 4.30 | −0.75 | .457 | −0.13 |
| Migration background | with (77) 4.24 | without (60) 4.26 | −0.15 | .883 | −0.03 |
| Special educational needs | with (13) 3.80 | without (124) 4.30 | −2.07 | .040 * | −0.60 |
| Grade level | Grade 3 (94) 4.20 | Grade 4 (43) 4.34 | −0.92 | .361 | −0.17 |
| Technology ownership | with (119) 4.24 | without (18) 4.28 | −0.16 | .872 | −0.04 |
| Prior robotics experience | with (16) 4.51 | without (121) 4.21 | +1.36 | .176 | +0.36 |
| STEM interest | with (34) 4.19 | without (103) 4.27 | −0.48 | .629 | −0.10 |

### Table S9. Sensitivity analysis: alternative operationalisations of support need

p-values for Student's t, Welch's t, and Mann-Whitney U on students' overall satisfaction under four operationalisations of support need. The manuscript's primary operationalisation is B (documented Förderschwerpunkte, n = 13); its bootstrap 95 % CI of the mean difference is [−0.98, −0.03] (10,000 resamples; bootstrap intervals vary marginally between runs). The direction is consistent across all operationalisations, with the strongest effect under the narrowest definition (C). The script's sensitivity module labels the operationalisations in a different order and replaces the n = 14 operationalisation with a broader one (support need including migration background, n = 83); the rows with n = 19, 13, and 8 reproduce directly from the script.

| Operationalisation | n | M with | M without | Student p | Welch p | Mann-Whitney p | d |
|---|---|---|---|---|---|---|---|
| A: any documented entry | 19 | 3.93 | 4.30 | .068 | .059 | .008 | −0.45 |
| B: Förderschwerpunkte (reported) | 13 | 3.80 | 4.30 | .040 | .068 | .020 | −0.60 |
| C: formally established only | 8 | 3.47 | 4.30 | .006 | .033 | .007 | −1.01 |
| D: excluding provisional designations | 14 | 3.79 | 4.30 | .027 | .032 | .004 | −0.63 |

### Table S10. Socio-emotional experience, item level (N = 139, scale −1/0/+1)

Nine items on a three-point smiley scale, ordered by mean; «% "+1"» is the share of children giving the most positive response.

| Item | M | SD | % "+1" |
|---|---|---|---|
| We helped each other | +0.32 | 0.74 | 49 % |
| I felt comfortable in my team | +0.45 | 0.68 | 55 % |
| I enjoyed working with my teammates | +0.51 | 0.72 | 64 % |
| I felt good | +0.53 | 0.70 | 64 % |
| I listened well and felt heard | +0.57 | 0.69 | 68 % |
| I liked programming the robot | +0.59 | 0.69 | 71 % |
| I had fun with the activity | +0.63 | 0.64 | 71 % |
| I found it exciting to do a new kind of activity | +0.63 | 0.59 | 69 % |
| I liked the activity | +0.76 | 0.48 | 78 % |

### Table S11. Teacher assessment of intervention outcomes (N = 10, one-sample tests against the scale midpoint)

* p < .05. The two helpfulness items offered an explicit «not applicable» option; no teacher selected it. The individual-item teacher intervention data is stored in a separate teacher questionnaire file and is not included in the consolidated dataset used by the analysis script; the values below are reproduced from the manuscript. The teacher questionnaire dataset will be provided together with the primary dataset on request.

| Item | Scale | M | SD | Midpoint | t(9) | p | d |
|---|---|---|---|---|---|---|---|
| Perceived usefulness for students | 0–10 | 8.70 | 1.64 | 5.0 | +7.15 | < .001 * | +2.26 |
| Likelihood of continuing the programme | 0–10 | 8.70 | 1.95 | 5.0 | +6.01 | < .001 * | +1.90 |
| Student motivation | 1–5 | 4.20 | 0.63 | 3.0 | +6.00 | < .001 * | +1.90 |
| Helpfulness for students with SEN | 1–6 | 3.40 | 0.70 | 3.5 | −0.45 | .662 | −0.14 |
| Helpfulness for usually excluded students | 1–6 | 2.80 | 0.79 | 3.5 | −2.81 | .021 * | −0.89 |
| Promotion of group cohesion | 1–5 | 2.70 | 0.67 | 3.0 | −1.41 | .193 | −0.44 |
| Promotion of inclusion in the class | 1–5 | 2.10 | 0.74 | 3.0 | −3.86 | .004 * | −1.22 |

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
