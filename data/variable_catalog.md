# PISA 2018 Variable Catalog

Generated from `data/raw/PISA2018_codebook.xlsx`. Covers student (`SPSS_STU_QQQ.zip`), school (`SPSS_SCH_QQQ.zip`), and teacher (`SPSS_TCH_QQQ.zip`) questionnaires.
**Total variables: 1664**

## Category Summary

| Category | Count |
|----------|-------|
| Identifiers | 26 |
| Test administration | 17 |
| Weights | 87 |
| Plausible values – Reading | 60 |
| Plausible values – Math | 10 |
| Plausible values – Science | 10 |
| Plausible values – Global competence | 10 |
| Demographics & background | 18 |
| Socioeconomic & parental background | 17 |
| Student background items | 306 |
| Parental background items | 152 |
| School context items (student-reported) | 163 |
| ICT familiarity items | 114 |
| Expected occupation items | 82 |
| Well-being items | 83 |
| Well-being & motivation | 1 |
| Derived index (WLE) | 85 |
| Derived index (sum/other) | 5 |
| Test-taking motivation | 2 |
| Learning time | 15 |
| Financial literacy items | 89 |
| School structure & resources | 26 |
| Teacher questionnaire items | 286 |

---

## Identifiers

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `CNTRYID` | Country Identifier | Student questionnaire |
| `CNT` | Country code 3-character | Student questionnaire |
| `CNTSCHID` | Intl. School ID | Student questionnaire |
| `CNTSTUID` | Intl. Student ID | Student questionnaire |
| `CYC` | PISA Assessment Cycle (2 digits + 2 character Assessment type - MS/FT) | Student questionnaire |
| `NatCen` | National Centre 6-digit Code | Student questionnaire |
| `SUBNATIO` | Adjudicated sub-region code 7-digit code (3-digit country code + region ID + stratum ID) | Student questionnaire |
| `OECD` | OECD country | Student questionnaire |
| `CNTRYID` | Country Identifier | School questionnaire |
| `CNT` | Country code 3-character | School questionnaire |
| `CNTSCHID` | Intl. School ID | School questionnaire |
| `CYC` | PISA Assessment Cycle (2 digits + 2 character Assessment type - MS/FT) | School questionnaire |
| `NatCen` | National Centre 6-digit Code | School questionnaire |
| `Region` | Region | School questionnaire |
| `SUBNATIO` | Adjudicated sub-region code 7-digit code (3-digit country code + region ID + stratum ID) | School questionnaire |
| `OECD` | OECD country | School questionnaire |
| `CNTRYID` | Country Identifier | Teacher questionnaire |
| `CNT` | Country code 3-character | Teacher questionnaire |
| `CNTSCHID` | Intl. School ID | Teacher questionnaire |
| `CNTTCHID` | Intl. Teacher ID | Teacher questionnaire |
| `TEACHERID` | Teacher identification code | Teacher questionnaire |
| `CYC` | PISA Assessment Cycle (2 digits + 2 character Assessment type - MS/FT) | Teacher questionnaire |
| `NatCen` | National Centre 6-digit Code | Teacher questionnaire |
| `Region` | Region | Teacher questionnaire |
| `SUBNATIO` | Adjudicated sub-region code 7-digit code (3-digit country code + region ID + stratum ID) | Teacher questionnaire |
| `OECD` | OECD country | Teacher questionnaire |

## Test administration

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `STRATUM` | Stratum ID 7-character (cnt + region ID + original stratum ID) | Student questionnaire |
| `ADMINMODE` | Mode of Respondent | Student questionnaire |
| `LANGTEST_QQQ` | Language of Questionnaire | Student questionnaire |
| `LANGTEST_COG` | Language of Assessment | Student questionnaire |
| `LANGTEST_PAQ` | Language of Assessment (PAQ) | Student questionnaire |
| `BOOKID` | Form Identifier | Student questionnaire |
| `UNIT` | REP_BWGT: RANDOMLY ASSIGNED UNIT NUMBER | Student questionnaire |
| `WVARSTRR` | RANDOMIZED FINAL VARIANCE STRATUM (1-80) | Student questionnaire |
| `VER_DAT` | Date of the database creation | Student questionnaire |
| `STRATUM` | Stratum ID 7-character (cnt + region ID + original stratum ID) | School questionnaire |
| `ADMINMODE` | Mode of Respondent | School questionnaire |
| `LANGTEST` | Language of Questionnaire/Assessment | School questionnaire |
| `VER_DAT` | Date of the database creation | School questionnaire |
| `STRATUM` | Stratum ID 7-character (cnt + region ID + original stratum ID) | Teacher questionnaire |
| `ADMINMODE` | Mode of Respondent | Teacher questionnaire |
| `LANGTEST` | Language of Questionnaire/Assessment | Teacher questionnaire |
| `VER_DAT` | Date of the database creation | Teacher questionnaire |

## Weights

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `W_FSTUWT` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT WEIGHT | Student questionnaire |
| `W_FSTURWT1` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 1 | Student questionnaire |
| `W_FSTURWT2` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 2 | Student questionnaire |
| `W_FSTURWT3` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 3 | Student questionnaire |
| `W_FSTURWT4` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 4 | Student questionnaire |
| `W_FSTURWT5` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 5 | Student questionnaire |
| `W_FSTURWT6` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 6 | Student questionnaire |
| `W_FSTURWT7` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 7 | Student questionnaire |
| `W_FSTURWT8` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 8 | Student questionnaire |
| `W_FSTURWT9` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 9 | Student questionnaire |
| `W_FSTURWT10` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 10 | Student questionnaire |
| `W_FSTURWT11` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 11 | Student questionnaire |
| `W_FSTURWT12` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 12 | Student questionnaire |
| `W_FSTURWT13` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 13 | Student questionnaire |
| `W_FSTURWT14` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 14 | Student questionnaire |
| `W_FSTURWT15` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 15 | Student questionnaire |
| `W_FSTURWT16` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 16 | Student questionnaire |
| `W_FSTURWT17` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 17 | Student questionnaire |
| `W_FSTURWT18` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 18 | Student questionnaire |
| `W_FSTURWT19` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 19 | Student questionnaire |
| `W_FSTURWT20` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 20 | Student questionnaire |
| `W_FSTURWT21` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 21 | Student questionnaire |
| `W_FSTURWT22` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 22 | Student questionnaire |
| `W_FSTURWT23` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 23 | Student questionnaire |
| `W_FSTURWT24` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 24 | Student questionnaire |
| `W_FSTURWT25` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 25 | Student questionnaire |
| `W_FSTURWT26` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 26 | Student questionnaire |
| `W_FSTURWT27` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 27 | Student questionnaire |
| `W_FSTURWT28` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 28 | Student questionnaire |
| `W_FSTURWT29` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 29 | Student questionnaire |
| `W_FSTURWT30` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 30 | Student questionnaire |
| `W_FSTURWT31` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 31 | Student questionnaire |
| `W_FSTURWT32` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 32 | Student questionnaire |
| `W_FSTURWT33` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 33 | Student questionnaire |
| `W_FSTURWT34` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 34 | Student questionnaire |
| `W_FSTURWT35` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 35 | Student questionnaire |
| `W_FSTURWT36` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 36 | Student questionnaire |
| `W_FSTURWT37` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 37 | Student questionnaire |
| `W_FSTURWT38` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 38 | Student questionnaire |
| `W_FSTURWT39` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 39 | Student questionnaire |
| `W_FSTURWT40` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 40 | Student questionnaire |
| `W_FSTURWT41` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 41 | Student questionnaire |
| `W_FSTURWT42` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 42 | Student questionnaire |
| `W_FSTURWT43` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 43 | Student questionnaire |
| `W_FSTURWT44` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 44 | Student questionnaire |
| `W_FSTURWT45` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 45 | Student questionnaire |
| `W_FSTURWT46` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 46 | Student questionnaire |
| `W_FSTURWT47` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 47 | Student questionnaire |
| `W_FSTURWT48` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 48 | Student questionnaire |
| `W_FSTURWT49` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 49 | Student questionnaire |
| `W_FSTURWT50` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 50 | Student questionnaire |
| `W_FSTURWT51` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 51 | Student questionnaire |
| `W_FSTURWT52` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 52 | Student questionnaire |
| `W_FSTURWT53` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 53 | Student questionnaire |
| `W_FSTURWT54` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 54 | Student questionnaire |
| `W_FSTURWT55` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 55 | Student questionnaire |
| `W_FSTURWT56` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 56 | Student questionnaire |
| `W_FSTURWT57` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 57 | Student questionnaire |
| `W_FSTURWT58` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 58 | Student questionnaire |
| `W_FSTURWT59` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 59 | Student questionnaire |
| `W_FSTURWT60` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 60 | Student questionnaire |
| `W_FSTURWT61` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 61 | Student questionnaire |
| `W_FSTURWT62` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 62 | Student questionnaire |
| `W_FSTURWT63` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 63 | Student questionnaire |
| `W_FSTURWT64` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 64 | Student questionnaire |
| `W_FSTURWT65` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 65 | Student questionnaire |
| `W_FSTURWT66` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 66 | Student questionnaire |
| `W_FSTURWT67` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 67 | Student questionnaire |
| `W_FSTURWT68` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 68 | Student questionnaire |
| `W_FSTURWT69` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 69 | Student questionnaire |
| `W_FSTURWT70` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 70 | Student questionnaire |
| `W_FSTURWT71` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 71 | Student questionnaire |
| `W_FSTURWT72` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 72 | Student questionnaire |
| `W_FSTURWT73` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 73 | Student questionnaire |
| `W_FSTURWT74` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 74 | Student questionnaire |
| `W_FSTURWT75` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 75 | Student questionnaire |
| `W_FSTURWT76` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 76 | Student questionnaire |
| `W_FSTURWT77` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 77 | Student questionnaire |
| `W_FSTURWT78` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 78 | Student questionnaire |
| `W_FSTURWT79` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 79 | Student questionnaire |
| `W_FSTURWT80` | FINAL TRIMMED NONRESPONSE ADJUSTED STUDENT REPLICATE BRR-FAY WEIGHTS 80 | Student questionnaire |
| `SENWT` | Senate Weight (sum of 5000 per country) | Student questionnaire |
| `W_SCHGRNRABWT` | GRADE NONRESPONSE ADJUSTED SCHOOL BASE WEIGHT | School questionnaire |
| `W_FSTUWT_SCH_SUM` | Sum of W_FSTUWT | School questionnaire |
| `SENWT` | Senate Weight (sum of 5000 per country) | School questionnaire |
| `W_SCHGRNRABWT` | GRADE NONRESPONSE ADJUSTED SCHOOL BASE WEIGHT | Teacher questionnaire |
| `W_FSTUWT_SCH_SUM` | Sum of W_FSTUWT | Teacher questionnaire |

## Plausible values – Reading

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `PV1READ` | Plausible Value 1 in Reading | Student questionnaire |
| `PV2READ` | Plausible Value 2 in Reading | Student questionnaire |
| `PV3READ` | Plausible Value 3 in Reading | Student questionnaire |
| `PV4READ` | Plausible Value 4 in Reading | Student questionnaire |
| `PV5READ` | Plausible Value 5 in Reading | Student questionnaire |
| `PV6READ` | Plausible Value 6 in Reading | Student questionnaire |
| `PV7READ` | Plausible Value 7 in Reading | Student questionnaire |
| `PV8READ` | Plausible Value 8 in Reading | Student questionnaire |
| `PV9READ` | Plausible Value 9 in Reading | Student questionnaire |
| `PV10READ` | Plausible Value 10 in Reading | Student questionnaire |
| `PV1RCLI` | Plausible Value 1 in Cognitive Process Subscale of Reading - Locate Information | Student questionnaire |
| `PV2RCLI` | Plausible Value 2 in Cognitive Process Subscale of Reading - Locate Information | Student questionnaire |
| `PV3RCLI` | Plausible Value 3 in Cognitive Process Subscale of Reading - Locate Information | Student questionnaire |
| `PV4RCLI` | Plausible Value 4 in Cognitive Process Subscale of Reading - Locate Information | Student questionnaire |
| `PV5RCLI` | Plausible Value 5 in Cognitive Process Subscale of Reading - Locate Information | Student questionnaire |
| `PV6RCLI` | Plausible Value 6 in Cognitive Process Subscale of Reading - Locate Information | Student questionnaire |
| `PV7RCLI` | Plausible Value 7 in Cognitive Process Subscale of Reading - Locate Information | Student questionnaire |
| `PV8RCLI` | Plausible Value 8 in Cognitive Process Subscale of Reading - Locate Information | Student questionnaire |
| `PV9RCLI` | Plausible Value 9 in Cognitive Process Subscale of Reading - Locate Information | Student questionnaire |
| `PV10RCLI` | Plausible Value 10 in Cognitive Process Subscale of Reading - Locate Information | Student questionnaire |
| `PV1RCUN` | Plausible Value 1 in Cognitive Process Subscale of Reading - Understand | Student questionnaire |
| `PV2RCUN` | Plausible Value 2 in Cognitive Process Subscale of Reading - Understand | Student questionnaire |
| `PV3RCUN` | Plausible Value 3 in Cognitive Process Subscale of Reading - Understand | Student questionnaire |
| `PV4RCUN` | Plausible Value 4 in Cognitive Process Subscale of Reading - Understand | Student questionnaire |
| `PV5RCUN` | Plausible Value 5 in Cognitive Process Subscale of Reading - Understand | Student questionnaire |
| `PV6RCUN` | Plausible Value 6 in Cognitive Process Subscale of Reading - Understand | Student questionnaire |
| `PV7RCUN` | Plausible Value 7 in Cognitive Process Subscale of Reading - Understand | Student questionnaire |
| `PV8RCUN` | Plausible Value 8 in Cognitive Process Subscale of Reading - Understand | Student questionnaire |
| `PV9RCUN` | Plausible Value 9 in Cognitive Process Subscale of Reading - Understand | Student questionnaire |
| `PV10RCUN` | Plausible Value 10 in Cognitive Process Subscale of Reading - Understand | Student questionnaire |
| `PV1RCER` | Plausible Value 1 in Cognitive Process Subscale of Reading - Evaluate and Reflect | Student questionnaire |
| `PV2RCER` | Plausible Value 2 in Cognitive Process Subscale of Reading - Evaluate and Reflect | Student questionnaire |
| `PV3RCER` | Plausible Value 3 in Cognitive Process Subscale of Reading - Evaluate and Reflect | Student questionnaire |
| `PV4RCER` | Plausible Value 4 in Cognitive Process Subscale of Reading - Evaluate and Reflect | Student questionnaire |
| `PV5RCER` | Plausible Value 5 in Cognitive Process Subscale of Reading - Evaluate and Reflect | Student questionnaire |
| `PV6RCER` | Plausible Value 6 in Cognitive Process Subscale of Reading - Evaluate and Reflect | Student questionnaire |
| `PV7RCER` | Plausible Value 7 in Cognitive Process Subscale of Reading - Evaluate and Reflect | Student questionnaire |
| `PV8RCER` | Plausible Value 8 in Cognitive Process Subscale of Reading - Evaluate and Reflect | Student questionnaire |
| `PV9RCER` | Plausible Value 9 in Cognitive Process Subscale of Reading - Evaluate and Reflect | Student questionnaire |
| `PV10RCER` | Plausible Value 10 in Cognitive Process Subscale of Reading - Evaluate and Reflect | Student questionnaire |
| `PV1RTSN` | Plausible Value 1 in Text Structure Subscale of Reading - Single | Student questionnaire |
| `PV2RTSN` | Plausible Value 2 in Text Structure Subscale of Reading - Single | Student questionnaire |
| `PV3RTSN` | Plausible Value 3 in Text Structure Subscale of Reading - Single | Student questionnaire |
| `PV4RTSN` | Plausible Value 4 in Text Structure Subscale of Reading - Single | Student questionnaire |
| `PV5RTSN` | Plausible Value 5 in Text Structure Subscale of Reading - Single | Student questionnaire |
| `PV6RTSN` | Plausible Value 6 in Text Structure Subscale of Reading - Single | Student questionnaire |
| `PV7RTSN` | Plausible Value 7 in Text Structure Subscale of Reading - Single | Student questionnaire |
| `PV8RTSN` | Plausible Value 8 in Text Structure Subscale of Reading - Single | Student questionnaire |
| `PV9RTSN` | Plausible Value 9 in Text Structure Subscale of Reading - Single | Student questionnaire |
| `PV10RTSN` | Plausible Value 10 in Text Structure Subscale of Reading - Single | Student questionnaire |
| `PV1RTML` | Plausible Value 1 in Text Structure Subscale of Reading - Multiple | Student questionnaire |
| `PV2RTML` | Plausible Value 2 in Text Structure Subscale of Reading - Multiple | Student questionnaire |
| `PV3RTML` | Plausible Value 3 in Text Structure Subscale of Reading - Multiple | Student questionnaire |
| `PV4RTML` | Plausible Value 4 in Text Structure Subscale of Reading - Multiple | Student questionnaire |
| `PV5RTML` | Plausible Value 5 in Text Structure Subscale of Reading - Multiple | Student questionnaire |
| `PV6RTML` | Plausible Value 6 in Text Structure Subscale of Reading - Multiple | Student questionnaire |
| `PV7RTML` | Plausible Value 7 in Text Structure Subscale of Reading - Multiple | Student questionnaire |
| `PV8RTML` | Plausible Value 8 in Text Structure Subscale of Reading - Multiple | Student questionnaire |
| `PV9RTML` | Plausible Value 9 in Text Structure Subscale of Reading - Multiple | Student questionnaire |
| `PV10RTML` | Plausible Value 10 in Text Structure Subscale of Reading - Multiple | Student questionnaire |

## Plausible values – Math

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `PV1MATH` | Plausible Value 1 in Mathematics | Student questionnaire |
| `PV2MATH` | Plausible Value 2 in Mathematics | Student questionnaire |
| `PV3MATH` | Plausible Value 3 in Mathematics | Student questionnaire |
| `PV4MATH` | Plausible Value 4 in Mathematics | Student questionnaire |
| `PV5MATH` | Plausible Value 5 in Mathematics | Student questionnaire |
| `PV6MATH` | Plausible Value 6 in Mathematics | Student questionnaire |
| `PV7MATH` | Plausible Value 7 in Mathematics | Student questionnaire |
| `PV8MATH` | Plausible Value 8 in Mathematics | Student questionnaire |
| `PV9MATH` | Plausible Value 9 in Mathematics | Student questionnaire |
| `PV10MATH` | Plausible Value 10 in Mathematics | Student questionnaire |

## Plausible values – Science

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `PV1SCIE` | Plausible Value 1 in Science | Student questionnaire |
| `PV2SCIE` | Plausible Value 2 in Science | Student questionnaire |
| `PV3SCIE` | Plausible Value 3 in Science | Student questionnaire |
| `PV4SCIE` | Plausible Value 4 in Science | Student questionnaire |
| `PV5SCIE` | Plausible Value 5 in Science | Student questionnaire |
| `PV6SCIE` | Plausible Value 6 in Science | Student questionnaire |
| `PV7SCIE` | Plausible Value 7 in Science | Student questionnaire |
| `PV8SCIE` | Plausible Value 8 in Science | Student questionnaire |
| `PV9SCIE` | Plausible Value 9 in Science | Student questionnaire |
| `PV10SCIE` | Plausible Value 10 in Science | Student questionnaire |

## Plausible values – Global competence

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `PV1GLCM` | Plausible Value 1 in Global Competency | Student questionnaire |
| `PV2GLCM` | Plausible Value 2 in Global Competency | Student questionnaire |
| `PV3GLCM` | Plausible Value 3 in Global Competency | Student questionnaire |
| `PV4GLCM` | Plausible Value 4 in Global Competency | Student questionnaire |
| `PV5GLCM` | Plausible Value 5 in Global Competency | Student questionnaire |
| `PV6GLCM` | Plausible Value 6 in Global Competency | Student questionnaire |
| `PV7GLCM` | Plausible Value 7 in Global Competency | Student questionnaire |
| `PV8GLCM` | Plausible Value 8 in Global Competency | Student questionnaire |
| `PV9GLCM` | Plausible Value 9 in Global Competency | Student questionnaire |
| `PV10GLCM` | Plausible Value 10 in Global Competency | Student questionnaire |

## Demographics & background

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `GRADE` | Grade compared to modal grade in country | Student questionnaire |
| `AGE` | Age | Student questionnaire |
| `COBN_S` | Country of Birth National Categories- Self | Student questionnaire |
| `COBN_M` | Country of Birth National Categories- Mother | Student questionnaire |
| `COBN_F` | Country of Birth National Categories- Father | Student questionnaire |
| `LANGN` | Language at home (3-digit code) | Student questionnaire |
| `LANGMOTHER` | Language spoken with their mother for students who do not speak the test language at home | Student questionnaire |
| `LANGFATHER` | Language spoken with their father for students who do not speak the test language at home | Student questionnaire |
| `LANGSIBLINGS` | Language spoken with their brother(s) and/or sister(s) for students who do not speak the test language at home | Student questionnaire |
| `LANGFRIEND` | Language spoken with their best friend for students who do not speak the test language at home | Student questionnaire |
| `LANGSCHMATES` | Language spoken with their school mates for students who do not speak the test language at home | Student questionnaire |
| `IMMIG` | Index Immigration status | Student questionnaire |
| `DURECEC` | Duration in early childhood education and care | Student questionnaire |
| `REPEAT` | Grade Repetition | Student questionnaire |
| `SCCHANGE` | Number of school changes | Student questionnaire |
| `CHANGE` | Number of changes in educational biography (Sum) | Student questionnaire |
| `COBN_T` | Country of birth national categories - Teacher | Teacher questionnaire |
| `EMPLTIM` | Teacher employment time - dichotomous | Teacher questionnaire |

## Socioeconomic & parental background

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `OCOD1` | ISCO-08 Occupation code - Mother | Student questionnaire |
| `OCOD2` | ISCO-08 Occupation code - Father | Student questionnaire |
| `OCOD3` | ISCO-08 Occupation code - Self | Student questionnaire |
| `ISCEDL` | ISCED level | Student questionnaire |
| `ISCEDD` | ISCED designation | Student questionnaire |
| `ISCEDO` | ISCED orientation | Student questionnaire |
| `MISCED` | Mothers Education (ISCED) | Student questionnaire |
| `FISCED` | Fathers Education (ISCED) | Student questionnaire |
| `HISCED` | Highest Education of parents (ISCED) | Student questionnaire |
| `MISCED_D` | Mothers Education - alternate definition (ISCED) | Student questionnaire |
| `FISCED_D` | Fathers Education - alternate definition (ISCED) | Student questionnaire |
| `HISCED_D` | Highest Education of parents - alternate definition (ISCED) | Student questionnaire |
| `BMMJ1` | ISEI of mother | Student questionnaire |
| `BFMJ2` | ISEI of father | Student questionnaire |
| `HISEI` | Index highest parental occupational status | Student questionnaire |
| `BSMJ` | Students expected occupational status (SEI) | Student questionnaire |
| `ESCS` | Index of economic, social and cultural status | Student questionnaire |

## Student background items

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `ST001D01T` | Student International Grade (Derived) | Student questionnaire |
| `ST003D02T` | Student (Standardized) Birth - Month | Student questionnaire |
| `ST003D03T` | Student (Standardized) Birth -Year | Student questionnaire |
| `ST004D01T` | Student (Standardized) Gender | Student questionnaire |
| `ST005Q01TA` | What is the <highest level of schooling> completed by your mother? | Student questionnaire |
| `ST006Q01TA` | Does your mother have this qualification? <ISCED level 6> (incl. higher qualifications at level 5A in some countries) | Student questionnaire |
| `ST006Q02TA` | Does your mother have this qualification? <ISCED level 5A> (excl. higher qualifications at level 5A in some countries) | Student questionnaire |
| `ST006Q03TA` | Does your mother have any of the following qualifications? <ISCED level 5B> | Student questionnaire |
| `ST006Q04TA` | Does your mother have any of the following qualifications? <ISCED level 4> | Student questionnaire |
| `ST007Q01TA` | What is the <highest level of schooling> completed by your father? | Student questionnaire |
| `ST008Q01TA` | Does your father have this qualification? <ISCED level 6> (incl. higher qualifications at level 5A in some countries) | Student questionnaire |
| `ST008Q02TA` | Does your father have this qualification? <ISCED level 5A> (excl. higher qualifications at level 5A in some countries) | Student questionnaire |
| `ST008Q03TA` | Does your father have any of the following qualifications? <ISCED level 5B> | Student questionnaire |
| `ST008Q04TA` | Does your father have any of the following qualifications? <ISCED level 4> | Student questionnaire |
| `ST011Q01TA` | In your home: A desk to study at | Student questionnaire |
| `ST011Q02TA` | In your home: A room of your own | Student questionnaire |
| `ST011Q03TA` | In your home: A quiet place to study | Student questionnaire |
| `ST011Q04TA` | In your home: A computer you can use for school work | Student questionnaire |
| `ST011Q05TA` | In your home: Educational software | Student questionnaire |
| `ST011Q06TA` | In your home: A link to the Internet | Student questionnaire |
| `ST011Q07TA` | In your home: Classic literature (e.g. <Shakespeare>) | Student questionnaire |
| `ST011Q08TA` | In your home: Books of poetry | Student questionnaire |
| `ST011Q09TA` | In your home: Works of art (e.g. paintings) | Student questionnaire |
| `ST011Q10TA` | In your home: Books to help with your school work | Student questionnaire |
| `ST011Q11TA` | In your home: <Technical reference books> | Student questionnaire |
| `ST011Q12TA` | In your home: A dictionary | Student questionnaire |
| `ST011Q16NA` | In your home: Books on art, music, or design | Student questionnaire |
| `ST011D17TA` | In your home: <Country-specific wealth item 1> | Student questionnaire |
| `ST011D18TA` | In your home: <Country-specific wealth item 2> | Student questionnaire |
| `ST011D19TA` | In your home: <Country-specific wealth item 3> | Student questionnaire |
| `ST012Q01TA` | How many in your home: Televisions | Student questionnaire |
| `ST012Q02TA` | How many in your home: Cars | Student questionnaire |
| `ST012Q03TA` | How many in your home: Rooms with a bath or shower | Student questionnaire |
| `ST012Q05NA` | How many in your home: <Cell phones> with Internet access (e.g. smartphones) | Student questionnaire |
| `ST012Q06NA` | How many in your home: Computers (desktop computer, portable laptop, or notebook) | Student questionnaire |
| `ST012Q07NA` | How many in your home: <Tablet computers> (e.g. <iPad>, <BlackBerry PlayBook>) | Student questionnaire |
| `ST012Q08NA` | How many in your home: E-book readers (e.g. <Kindle>, <Kobo>, <Bookeen>) | Student questionnaire |
| `ST012Q09NA` | How many in your home: Musical instruments (e.g. guitar, piano) | Student questionnaire |
| `ST013Q01TA` | How many books are there in your home? | Student questionnaire |
| `ST019AQ01T` | In what country were you and your parents born? You | Student questionnaire |
| `ST019BQ01T` | In what country were you and your parents born? Mother | Student questionnaire |
| `ST019CQ01T` | In what country were you and your parents born? Father | Student questionnaire |
| `ST021Q01TA` | How old were you when you arrived in <country of test>? | Student questionnaire |
| `ST125Q01NA` | How old were you when you started <ISCED 0>? Years | Student questionnaire |
| `ST126Q01TA` | How old were you when you started <ISCED 1>? Years | Student questionnaire |
| `ST127Q01TA` | Have you ever repeated a <grade>? At <ISCED 1> | Student questionnaire |
| `ST127Q02TA` | Have you ever repeated a <grade>? At <ISCED 2> | Student questionnaire |
| `ST127Q03TA` | Have you ever repeated a <grade>? At <ISCED 3> | Student questionnaire |
| `ST022Q01TA` | What language do you speak at home most of the time? | Student questionnaire |
| `ST023Q01TA` | Which language do you usually speak with: My mother | Student questionnaire |
| `ST023Q02TA` | Which language do you usually speak with: My father | Student questionnaire |
| `ST023Q03TA` | Which language do you usually speak with: My brother(s) and/or sister(s) | Student questionnaire |
| `ST023Q04TA` | Which language do you usually speak with: My best friend | Student questionnaire |
| `ST023Q05TA` | Which language do you usually speak with: My schoolmates | Student questionnaire |
| `ST097Q01TA` | How often during <test language lessons>: Students don't listen to what the teacher says. | Student questionnaire |
| `ST097Q02TA` | How often during <test language lessons>: There is noise and disorder. | Student questionnaire |
| `ST097Q03TA` | How often during <test language lessons>: The teacher waits long for students to quiet down. | Student questionnaire |
| `ST097Q04TA` | How often during <test language lessons>: Students cannot work well. | Student questionnaire |
| `ST097Q05TA` | How often during <test language lessons>: Students don't start working for a long time after the lesson begins. | Student questionnaire |
| `ST100Q01TA` | How often during <test language lessons>: The teacher shows aninterest in every student's learning. | Student questionnaire |
| `ST100Q02TA` | How often during <test language lessons>: The teacher gives extra help when students need it. | Student questionnaire |
| `ST100Q03TA` | How often during <test language lessons>: The teacher helps students with their learning. | Student questionnaire |
| `ST100Q04TA` | How often during <test language lessons>: The teacher continues teaching until the students understands. | Student questionnaire |
| `ST102Q01TA` | How often during <test language lessons>: The teacher sets clear goals for our learning. | Student questionnaire |
| `ST102Q02TA` | How often during <test language lessons>: The teacher asks questions to check whether we have understood what was taught | Student questionnaire |
| `ST102Q03TA` | How often during <test language lessons>: [...] the teacher presents a short summary of the previous lesson. | Student questionnaire |
| `ST102Q04TA` | How often during <test language lessons>: The teacher tells us what we have to learn. | Student questionnaire |
| `ST211Q01HA` | Thinking of past two <test language lessons>: The teacher made me feel confident in my ability to do well in the course. | Student questionnaire |
| `ST211Q02HA` | Thinking of past two <test language lessons>: The teacher listened to my view on how to do things. | Student questionnaire |
| `ST211Q03HA` | Thinking of past two <test language lessons>: I felt that my teacher understood me. | Student questionnaire |
| `ST212Q01HA` | How often in <test language lessons>: The teacher adapts the lesson to my classs needs and knowledge. | Student questionnaire |
| `ST212Q02HA` | How often in <test language lessons>: The teacher provides individual help when a student has difficulties [...] | Student questionnaire |
| `ST212Q03HA` | How often in <test language lessons>: The teacher changes the structure of the lesson on a topic that most [...] | Student questionnaire |
| `ST104Q02NA` | How often during <test language lessons>: The teacher gives me feedback on my strengths in this subject. | Student questionnaire |
| `ST104Q03NA` | How often during <test language lessons>: The teacher tells me in which areas I can still improve. | Student questionnaire |
| `ST104Q04NA` | How often during <test language lessons>: The teacher tells me how I can improve my performance. | Student questionnaire |
| `ST213Q01HA` | Thinking of past two <test language lessons>: It was clear to me that the teacher liked teaching us. | Student questionnaire |
| `ST213Q02HA` | Thinking of past two <test language lessons>: The enthusiasm of the teacher inspired me. | Student questionnaire |
| `ST213Q03HA` | Thinking of past two <test language lessons>: It was clear that the teacher likes to deal with the topic of the lesson. | Student questionnaire |
| `ST213Q04HA` | Thinking of past two <test language lessons>: The teacher showed enjoyment in teaching. | Student questionnaire |
| `ST150Q01IA` | During the last month, how often did you have to read for school: Texts that include diagrams or maps | Student questionnaire |
| `ST150Q02IA` | During the last month, how often did you have to read for school: Fiction (e.g., novels, short stories) | Student questionnaire |
| `ST150Q03IA` | During the last month, how often did you have to read for school: Texts that include tables or graphs | Student questionnaire |
| `ST150Q04HA` | During the last month, how often did you have to read for school: Digital texts including links | Student questionnaire |
| `ST152Q05IA` | In your <test language lessons>, how often: The teacher encourages students to express their opinion about a text. | Student questionnaire |
| `ST152Q06IA` | In your <test language lessons>, how often: The teacher helps students relate the stories they read to their lives. | Student questionnaire |
| `ST152Q07IA` | In your <test language lessons>, how often: The teacher shows students how the information in texts builds on [...] | Student questionnaire |
| `ST152Q08IA` | In your <test language lessons>, how often: The teacher poses questions that motivate students to participate actively. | Student questionnaire |
| `ST154Q01HA` | <this academic year>, how many pages was the longest piece of text you had to read for your <test language lessons>? | Student questionnaire |
| `ST153Q01HA` | When you have to read, does the teacher ask you to: Write a summary of the book or the chapter | Student questionnaire |
| `ST153Q02HA` | When you have to read, does the teacher ask you to: List and write a short description of the main characters | Student questionnaire |
| `ST153Q03HA` | When you have to read, does the teacher ask you to: Discuss in small groups with other students who read the same [...] | Student questionnaire |
| `ST153Q04HA` | When you have to read, does the teacher ask you to: Give your personal thoughts about the book or the chapter [...] | Student questionnaire |
| `ST153Q05HA` | When you have to read, does the teacher ask you to: Answer questions about the book or the chapter | Student questionnaire |
| `ST153Q06HA` | When you have to read, does the teacher ask you to: Compare the content of the book or the chapter with your own [...] | Student questionnaire |
| `ST153Q08HA` | When you have to read, does the teacher ask you to: Compare the book with other books or texts on a similar topic | Student questionnaire |
| `ST153Q09HA` | When you have to read, does the teacher ask you to: Select a passage you liked or disliked and explain why | Student questionnaire |
| `ST153Q10HA` | When you have to read, does the teacher ask you to: Write a text related to what you have read | Student questionnaire |
| `ST158Q01HA` | Taught at school: How to use keywords when using a search engine such as <Google>, <Yahoo>, etc. | Student questionnaire |
| `ST158Q02HA` | Taught at school: How to decide whether to trust information from the Internet | Student questionnaire |
| `ST158Q03HA` | Taught at school: How to compare different web pages and decide what information is more relevant for your school work | Student questionnaire |
| `ST158Q04HA` | Taught at school: To understand the consequences of making information publicly available online on <Facebook>, [...] | Student questionnaire |
| `ST158Q05HA` | Taught at school: How to use the short description below the links in the list of results of a search | Student questionnaire |
| `ST158Q06HA` | Taught at school: How to detect whether the information is subjective or biased | Student questionnaire |
| `ST158Q07HA` | Taught at school: How to detect phishing or spam emails | Student questionnaire |
| `ST160Q01IA` | How much do you agree or disagree? I read only if I have to. | Student questionnaire |
| `ST160Q02IA` | How much do you agree or disagree? Reading is one of my favourite hobbies. | Student questionnaire |
| `ST160Q03IA` | How much do you agree or disagree? I like talking about books with other people. | Student questionnaire |
| `ST160Q04IA` | How much do you agree or disagree? For me, reading is a waste of time. | Student questionnaire |
| `ST160Q05IA` | How much do you agree or disagree? I read only to get information that I need. | Student questionnaire |
| `ST167Q01IA` | How often do you read these materials because you want to? Magazines | Student questionnaire |
| `ST167Q02IA` | How often do you read these materials because you want to? Comic books | Student questionnaire |
| `ST167Q03IA` | How often do you read these materials because you want to? Fiction (novels, narratives, stories) | Student questionnaire |
| `ST167Q04IA` | How often do you read these materials because you want to? Non-fiction books (informational, documentary) | Student questionnaire |
| `ST167Q05IA` | How often do you read these materials because you want to? Newspapers | Student questionnaire |
| `ST168Q01HA` | Which of the following statements best describes how you read books (on any topic)? | Student questionnaire |
| `ST175Q01IA` | About how much time do you usually spend reading for enjoyment? | Student questionnaire |
| `ST176Q01IA` | How often involved in: Reading emails | Student questionnaire |
| `ST176Q02IA` | How often involved in: <Chat on line> (e.g. <Whatsapp>, <Messenger>) | Student questionnaire |
| `ST176Q03IA` | How often involved in: Reading online news | Student questionnaire |
| `ST176Q05IA` | How often involved in: Searching information online to learn about a particular topic | Student questionnaire |
| `ST176Q06IA` | How often involved in: Taking part in online group discussions or forums | Student questionnaire |
| `ST176Q07IA` | How often involved in: Searching for practical information online (e.g. schedules, events, tips, recipes) | Student questionnaire |
| `ST161Q01HA` | Agree: I am a good reader. | Student questionnaire |
| `ST161Q02HA` | Agree: I am able to understand difficult texts. | Student questionnaire |
| `ST161Q03HA` | Agree: I read fluently. | Student questionnaire |
| `ST161Q06HA` | Agree: I have always had difficulty with reading. | Student questionnaire |
| `ST161Q07HA` | Agree: I have to read a text several times before completely understanding it. | Student questionnaire |
| `ST161Q08HA` | Agree: I find it difficult to answer questions about a text. | Student questionnaire |
| `ST163Q02HA` | In the PISA test, how do you feel about the reading tasks: There were many words I could not understand. | Student questionnaire |
| `ST163Q03HA` | In the PISA test, how do you feel about the reading tasks: Many texts were too difficult for me. | Student questionnaire |
| `ST163Q04HA` | In the PISA test, how do you feel about the reading tasks: I was lost when I had to navigate between different pages. | Student questionnaire |
| `ST164Q01IA` | Usefulness for understanding and memorising text: I concentrate on the parts of the text that are easy to understand. | Student questionnaire |
| `ST164Q02IA` | Usefulness for understanding and memorising text: I quickly read through the text twice. | Student questionnaire |
| `ST164Q03IA` | Usefulness for understanding and memorising text: After reading the text, I discuss its content with other people. | Student questionnaire |
| `ST164Q04IA` | Usefulness for understanding and memorising text: I underline important parts of the text. | Student questionnaire |
| `ST164Q05IA` | Usefulness for understanding and memorising text: I summarise the text in my own words. | Student questionnaire |
| `ST164Q06IA` | Usefulness for understanding and memorising text: I read the text aloud to another person. | Student questionnaire |
| `ST165Q01IA` | Usefulness for writing a summary: I write a summary. Then I check that each paragraph is covered in the summary, [...] | Student questionnaire |
| `ST165Q02IA` | Usefulness for writing a summary: I try to copy out accurately as many sentences as possible. | Student questionnaire |
| `ST165Q03IA` | Usefulness for writing a summary: Before writing the summary, I read the text as many times as possible. | Student questionnaire |
| `ST165Q04IA` | Usefulness for writing a summary: I carefully check whether the most important facts in the text are represented [...] | Student questionnaire |
| `ST165Q05IA` | Usefulness for writing a summary: I read through the text, underlining the most important sentences. Then I write [...] | Student questionnaire |
| `ST166Q01HA` | How appropriate in reaction to this email: Answer the email and ask for more information about the smartphone | Student questionnaire |
| `ST166Q02HA` | How appropriate in reaction to this email: Check the sender's email address | Student questionnaire |
| `ST166Q03HA` | How appropriate in reaction to this email: Click on the link to fill out the form as soon as possible | Student questionnaire |
| `ST166Q04HA` | How appropriate in reaction to this email: Delete the email without clicking on the link | Student questionnaire |
| `ST166Q05HA` | How appropriate in reaction to this email: Check the website of the mobile phone operator to see whether [...] | Student questionnaire |
| `ST016Q01NA` | Overall, how satisfied are you with your life as a whole these days? | Student questionnaire |
| `ST036Q05TA` | Thinking about your school: Trying hard at school will help me get a good job. | Student questionnaire |
| `ST036Q06TA` | Thinking about your school: Trying hard at school will help me get into a good <college>. | Student questionnaire |
| `ST036Q08TA` | Thinking about your school: Trying hard at school is important. | Student questionnaire |
| `ST225Q01HA` | Do you expect to complete? <ISCED level 2> | Student questionnaire |
| `ST225Q02HA` | Do you expect to complete? <ISCED level 3B or C> | Student questionnaire |
| `ST225Q03HA` | Do you expect to complete? <ISCED level 3A> | Student questionnaire |
| `ST225Q04HA` | Do you expect to complete? <ISCED level 4> | Student questionnaire |
| `ST225Q05HA` | Do you expect to complete? <ISCED level 5B> | Student questionnaire |
| `ST225Q06HA` | Do you expect to complete? <ISCED level 5A or 6> | Student questionnaire |
| `ST181Q02HA` | Agree: I enjoy working in situations involving competition with others. | Student questionnaire |
| `ST181Q03HA` | Agree: It is important for me to perform better than other people on a task. | Student questionnaire |
| `ST181Q04HA` | Agree: I try harder when Im in competition with other people. | Student questionnaire |
| `ST182Q03HA` | Agree: I find satisfaction in working as hard as I can. | Student questionnaire |
| `ST182Q04HA` | Agree: Once I start a task, I persist until it is finished. | Student questionnaire |
| `ST182Q05HA` | Agree: Part of the enjoyment I get from doing things is when I improve on my past performance. | Student questionnaire |
| `ST182Q06HA` | Agree: If I am not good at something, I would rather keep struggling to master it than move on to something I may [...] | Student questionnaire |
| `ST183Q01HA` | Agree: When I am failing, I worry about what others think of me. | Student questionnaire |
| `ST183Q02HA` | Agree: When I am failing, I am afraid that I might not have enough talent. | Student questionnaire |
| `ST183Q03HA` | Agree: When I am failing, this makes me doubt my plans for the future. | Student questionnaire |
| `ST184Q01HA` | Agree: Your intelligence is something about you that you can't change very much. | Student questionnaire |
| `ST185Q01HA` | Agree: My life has clear meaning or purpose. | Student questionnaire |
| `ST185Q02HA` | Agree: I have discovered a satisfactory meaning in life. | Student questionnaire |
| `ST185Q03HA` | Agree: I have a clear sense of what gives meaning to my life. | Student questionnaire |
| `ST186Q05HA` | Thinking about yourself and how you normally feel: how often do you feel as described below? Happy | Student questionnaire |
| `ST186Q06HA` | Thinking about yourself and how you normally feel: how often do you feel as described below? Scared | Student questionnaire |
| `ST186Q07HA` | Thinking about yourself and how you normally feel: how often do you feel as described below? Lively | Student questionnaire |
| `ST186Q10HA` | Thinking about yourself and how you normally feel: how often do you feel as described below? Miserable | Student questionnaire |
| `ST186Q09HA` | Thinking about yourself and how you normally feel: how often do you feel as described below? Proud | Student questionnaire |
| `ST186Q02HA` | Thinking about yourself and how you normally feel: how often do you feel as described below? Afraid | Student questionnaire |
| `ST186Q01HA` | Thinking about yourself and how you normally feel: how often do you feel as described below? Joyful | Student questionnaire |
| `ST186Q08HA` | Thinking about yourself and how you normally feel: how often do you feel as described below? Sad | Student questionnaire |
| `ST186Q03HA` | Thinking about yourself and how you normally feel: how often do you feel as described below? Cheerful | Student questionnaire |
| `ST208Q01HA` | How true for you: My goal is to learn as much as possible. | Student questionnaire |
| `ST208Q02HA` | How true for you: My goal is to completely master the material presented in my classes. | Student questionnaire |
| `ST208Q04HA` | How true for you: My goal is to understand the content of my classes as thoroughly as possible. | Student questionnaire |
| `ST188Q01HA` | Agree: I usually manage one way or another. | Student questionnaire |
| `ST188Q02HA` | Agree: I feel proud that I have accomplished things. | Student questionnaire |
| `ST188Q03HA` | Agree: I feel that I can handle many things at a time. | Student questionnaire |
| `ST188Q06HA` | Agree: My belief in myself gets me through hard times. | Student questionnaire |
| `ST188Q07HA` | Agree: When Im in a difficult situation, I can usually find my way out of it. | Student questionnaire |
| `ST034Q01TA` | Thinking about your school: I feel like an outsider (or left out of things) at school. | Student questionnaire |
| `ST034Q02TA` | Thinking about your school: I make friends easily at school. | Student questionnaire |
| `ST034Q03TA` | Thinking about your school: I feel like I belong at school. | Student questionnaire |
| `ST034Q04TA` | Thinking about your school: I feel awkward and out of place in my school. | Student questionnaire |
| `ST034Q05TA` | Thinking about your school: Other students seem to like me. | Student questionnaire |
| `ST034Q06TA` | Thinking about your school: I feel lonely at school. | Student questionnaire |
| `ST196Q02HA` | How easy to perform on your own: Explain how carbon-dioxide emissions affect global climate change | Student questionnaire |
| `ST196Q03HA` | How easy to perform on your own: Establish a connection between prices of textiles and working conditions in the [...] | Student questionnaire |
| `ST196Q04HA` | How easy to perform on your own: Discuss the different reasons why people become refugees | Student questionnaire |
| `ST196Q05HA` | How easy to perform on your own: Explain why some countries suffer more from global climate change than others | Student questionnaire |
| `ST196Q06HA` | How easy to perform on your own: Explain how economic crises in single countries affect the global economy | Student questionnaire |
| `ST196Q07HA` | How easy to perform on your own: Discuss the consequences of economic development on the environment | Student questionnaire |
| `ST197Q01HA` | How informed are you about the following topics? Climate change and global warming | Student questionnaire |
| `ST197Q02HA` | How informed are you about the following topics? Global health (e.g. epidemics) | Student questionnaire |
| `ST197Q04HA` | How informed are you about the following topics? Migration (movement of people) | Student questionnaire |
| `ST197Q07HA` | How informed are you about the following topics? International conflicts | Student questionnaire |
| `ST197Q08HA` | How informed are you about the following topics? Hunger or malnutrition in different parts of the world | Student questionnaire |
| `ST197Q09HA` | How informed are you about the following topics? Causes of poverty | Student questionnaire |
| `ST197Q12HA` | How informed are you about the following topics? Equality between men and women in different parts of the world | Student questionnaire |
| `ST215Q01HA` | How well does the following describe you: I try to look at everybody's side of a disagreement before I make a decision. | Student questionnaire |
| `ST215Q02HA` | How well does the following describe you: I believe that there are two sides to every question and try to look at [...] | Student questionnaire |
| `ST215Q03HA` | How well does the following describe you: I sometimes try to understand my friends better by imagining how things [...] | Student questionnaire |
| `ST215Q04HA` | How well does the following describe you: Before criticizing somebody, I try to imagine how I would feel if I were [...] | Student questionnaire |
| `ST215Q05HA` | How well does the following describe you: When I'm upset at someone, I try to take the perspective of that person [...] | Student questionnaire |
| `ST216Q01HA` | How well does the following describe you: I can deal with unusual situations. | Student questionnaire |
| `ST216Q02HA` | How well does the following describe you: I can change my behaviour to meet the needs of new situations. | Student questionnaire |
| `ST216Q03HA` | How well does the following describe you: I can adapt to different situations even when under stress or pressure. | Student questionnaire |
| `ST216Q04HA` | How well does the following describe you: I can adapt easily to a new culture. | Student questionnaire |
| `ST216Q05HA` | How well does the following describe you: When encountering difficult situations with other people, I can think of [...] | Student questionnaire |
| `ST216Q06HA` | How well does the following describe you: I am capable of overcoming my difficulties in interacting with people [...] | Student questionnaire |
| `ST218Q01HA` | Intercultural communication: I carefully observe their reactions. | Student questionnaire |
| `ST218Q02HA` | Intercultural communication: I frequently check that we are understanding each other correctly. | Student questionnaire |
| `ST218Q03HA` | Intercultural communication: I listen carefully to what they say. | Student questionnaire |
| `ST218Q04HA` | Intercultural communication: I choose my words carefully. | Student questionnaire |
| `ST218Q05HA` | Intercultural communication: I give concrete examples to explain my ideas. | Student questionnaire |
| `ST218Q06HA` | Intercultural communication: I explain things very carefully. | Student questionnaire |
| `ST218Q07HA` | Intercultural communication: If there is a problem with communication, I find ways around it [...] | Student questionnaire |
| `ST222Q01HA` | Involved in: I reduce the energy I use at home [...] to protect the environment. | Student questionnaire |
| `ST222Q03HA` | Involved in: I choose certain products for ethical or environmental reasons, even if they are a bit more expensive. | Student questionnaire |
| `ST222Q04HA` | Involved in: I sign environmental or social petitions online. | Student questionnaire |
| `ST222Q05HA` | Involved in: I keep myself informed about world events via <Twitter> or <Facebook>. | Student questionnaire |
| `ST222Q06HA` | Involved in: I boycott products or companies for political, ethical or environmental reasons. | Student questionnaire |
| `ST222Q08HA` | Involved in: I participate in activities promoting equality between men and women. | Student questionnaire |
| `ST222Q09HA` | Involved in: I participate in activities in favour of environmental protection. | Student questionnaire |
| `ST222Q10HA` | Involved in: I regularly read websites on international social issues (e.g. poverty, human rights). | Student questionnaire |
| `ST214Q01HA` | How well does the following describe you: I want to learn how people live in different countries. | Student questionnaire |
| `ST214Q02HA` | How well does the following describe you: I want to learn more about the religions of the world. | Student questionnaire |
| `ST214Q03HA` | How well does the following describe you: I am interested in how people from various cultures see the world. | Student questionnaire |
| `ST214Q06HA` | How well does the following describe you: I am interested in finding out about the traditions of other cultures. | Student questionnaire |
| `ST220Q01HA` | Do you have contact with people from other countries? In your family | Student questionnaire |
| `ST220Q02HA` | Do you have contact with people from other countries? At school | Student questionnaire |
| `ST220Q03HA` | Do you have contact with people from other countries? In your neighbourhood | Student questionnaire |
| `ST220Q04HA` | Do you have contact with people from other countries? In your circle of friends | Student questionnaire |
| `ST217Q01HA` | How well does the following describe you: I respect people from other cultures as equal human beings. | Student questionnaire |
| `ST217Q02HA` | How well does the following describe you: I treat all people with respect regardless of their cultural background. | Student questionnaire |
| `ST217Q03HA` | How well does the following describe you: I give space to people from other cultures to express themselves. | Student questionnaire |
| `ST217Q04HA` | How well does the following describe you: I respect the values of people from different cultures. | Student questionnaire |
| `ST217Q05HA` | How well does the following describe you: I value the opinions of people from different cultures. | Student questionnaire |
| `ST219Q01HA` | Agree: I think of myself as a citizen of the world. | Student questionnaire |
| `ST219Q02HA` | Agree: When I see the poor conditions that some people in the world live under, I feel a responsibility to do [...] | Student questionnaire |
| `ST219Q03HA` | Agree: I think my behaviour can impact people in other countries. | Student questionnaire |
| `ST219Q04HA` | Agree: It is right to boycott companies that are known to provide poor workplace conditions for their employees. | Student questionnaire |
| `ST219Q05HA` | Agree: I can do something about the problems of the world. | Student questionnaire |
| `ST219Q06HA` | Agree: Looking after the global environment is important to me. | Student questionnaire |
| `ST204Q02HA` | Agree: Immigrant children should have the same opportunities for education that other children in the country have. | Student questionnaire |
| `ST204Q03HA` | Agree: Immigrants who live in a country for several years should have the opportunity to vote in elections. | Student questionnaire |
| `ST204Q04HA` | Agree: Immigrants should have the opportunity to continue their own customs and lifestyle. | Student questionnaire |
| `ST204Q05HA` | Agree: Immigrants should have all the same rights that everyone else in the country has. | Student questionnaire |
| `ST177Q01HA` | How many languages [...] do you and your parents speak well enough to converse with others? You | Student questionnaire |
| `ST177Q02HA` | How many languages [...] do you and your parents speak well enough to converse with others? Your mother | Student questionnaire |
| `ST177Q03HA` | How many languages [...] do you and your parents speak well enough to converse with others? Your father | Student questionnaire |
| `ST189Q01HA` | How many foreign languages do you learn at your school this school year? | Student questionnaire |
| `ST221Q01HA` | At school: I learn about the interconnectedness of countries economies. | Student questionnaire |
| `ST221Q02HA` | At school: I learn how to solve conflicts with other people in our classrooms. | Student questionnaire |
| `ST221Q03HA` | At school: I learn about different cultures. | Student questionnaire |
| `ST221Q04HA` | At school: We read newspapers, look for news on the Internet or watch the news together during classes. | Student questionnaire |
| `ST221Q05HA` | At school: I am often invited by my teachers to give my personal opinion about international news. | Student questionnaire |
| `ST221Q06HA` | At school: I participate in events celebrating cultural diversity throughout the school year. | Student questionnaire |
| `ST221Q07HA` | At school: I participate in classroom discussions about world events as part of the regular instruction. | Student questionnaire |
| `ST221Q08HA` | At school: I analyse global issues together with my classmates in small groups during class. | Student questionnaire |
| `ST221Q09HA` | At school: I learn how people from different cultures can have different perspectives on some issues. | Student questionnaire |
| `ST221Q11HA` | At school: I learn how to communicate with people from different backgrounds. | Student questionnaire |
| `ST223Q02HA` | Teachers inyour school: They have misconceptions about the history of some cultural groups. | Student questionnaire |
| `ST223Q04HA` | Teachers in your school: They say negative things about people of some cultural groups. | Student questionnaire |
| `ST223Q05HA` | Teachers inyour school: They blame people of some cultural groups for problems faced by <country of test>. | Student questionnaire |
| `ST223Q08HA` | Teachers inyour school: They have lower academic expectations for students of some cultural groups. | Student questionnaire |
| `ST123Q02NA` | Thinking about <this academic year>: My parents support my educational efforts and achievements. | Student questionnaire |
| `ST123Q03NA` | Thinking about <this academic year>: My parents support me when I am facing difficulties at school. | Student questionnaire |
| `ST123Q04NA` | Thinking about <this academic year>: My parents encourage me to be confident. | Student questionnaire |
| `ST205Q01HA` | Think about your school, how true: Students seem to value competition. | Student questionnaire |
| `ST205Q02HA` | Think about your school, how true: It seems that students are competing with each other. | Student questionnaire |
| `ST205Q03HA` | Think about your school, how true: Students seem to share the feeling that competing with each other is important. | Student questionnaire |
| `ST205Q04HA` | Think about your school, how true: Students feel that they are being compared with others. | Student questionnaire |
| `ST059Q01TA` | Typically required to attend: Number of <class periods> per week in <test language lessons> | Student questionnaire |
| `ST059Q02TA` | Typically required to attend: Number of <class periods> per week in mathematics | Student questionnaire |
| `ST059Q03TA` | Typically required to attend: Number of <class periods> per week in <science> | Student questionnaire |
| `ST059Q04HA` | Typically required to attend: Number of <class periods> per week in foreign language | Student questionnaire |
| `ST060Q01NA` | In a normal, full week at school, how many <class periods> are you required to attend in total? | Student questionnaire |
| `ST061Q01NA` | How many minutes, on average, are there in a <class period>? | Student questionnaire |
| `ST062Q01TA` | In the last two full weeks of school, how often: I <skipped> a whole school day. | Student questionnaire |
| `ST062Q02TA` | In the last two full weeks of school, how often: I <skipped> some classes. | Student questionnaire |
| `ST062Q03TA` | In the last two full weeks of school, how often: I arrived late for school. | Student questionnaire |
| `ST038Q03NA` | During the past 12 months, how often: Other students left me out of things on purpose. | Student questionnaire |
| `ST038Q04NA` | During the past 12 months, how often: Other students made fun of me. | Student questionnaire |
| `ST038Q05NA` | During the past 12 months, how often: I was threatened by other students. | Student questionnaire |
| `ST038Q06NA` | During the past 12 months, how often: Other students took away or destroyed things that belonged to me. | Student questionnaire |
| `ST038Q07NA` | During the past 12 months, how often: I got hit or pushed around by other students. | Student questionnaire |
| `ST038Q08NA` | During the past 12 months, how often: Other students spread nasty rumours about me. | Student questionnaire |
| `ST207Q01HA` | Agree: It irritates me when nobody defends bullied students. | Student questionnaire |
| `ST207Q02HA` | Agree: It is a good thing to help students who can't defend themselves. | Student questionnaire |
| `ST207Q03HA` | Agree: It is a wrong thing to join in bullying. | Student questionnaire |
| `ST207Q04HA` | Agree: I feel bad seeing other students bullied. | Student questionnaire |
| `ST207Q05HA` | Agree: I like it when someone stands up for other students who are being bullied. | Student questionnaire |
| `ST206Q01HA` | Think about your school, how true: Students seem to value cooperation. | Student questionnaire |
| `ST206Q02HA` | Think about your school, how true: It seems that students are cooperating with each other. | Student questionnaire |
| `ST206Q03HA` | Think about your school, how true: Students seem to share the feeling that cooperating with each other is important. | Student questionnaire |
| `ST206Q04HA` | Think about your school, how true: Students feel that they are encouraged to cooperate with others. | Student questionnaire |

## Parental background items

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `PA001Q01TA` | Who will complete this questionnaire? Mother or other female guardian | Student questionnaire |
| `PA001Q02TA` | Who will complete this questionnaire? Father or other male guardian | Student questionnaire |
| `PA001Q03TA` | Who will complete this questionnaire? Other | Student questionnaire |
| `PA003Q01TA` | Activities with your child, how often: Discuss how well my child is doing at school | Student questionnaire |
| `PA003Q02TA` | Activities with your child, how often: Eat <the main meal> with my child around a table | Student questionnaire |
| `PA003Q03TA` | Activities with your child, how often: Spend time just talking to my child | Student questionnaire |
| `PA003Q04HA` | Activities with your child, how often: Help my child with his/her reading and writing homework | Student questionnaire |
| `PA003Q05IA` | Activities with your child, how often: Discuss political or social issues | Student questionnaire |
| `PA003Q06IA` | Activities with your child, how often: Go to a bookstore or library with my child | Student questionnaire |
| `PA003Q07IA` | Activities with your child, how often: Talk with my child about what he/she is reading on his/her own | Student questionnaire |
| `PA154Q01IA` | When child attended the first year of <ISCED 1>, how often: Read books | Student questionnaire |
| `PA154Q02IA` | When child attended the first year of <ISCED 1>, how often: Tell stories | Student questionnaire |
| `PA154Q03IA` | When child attended the first year of <ISCED 1>, how often: Sing songs | Student questionnaire |
| `PA154Q04IA` | When child attended the first year of <ISCED 1>, how often: Play with alphabet toys [...] | Student questionnaire |
| `PA154Q05IA` | When child attended the first year of <ISCED 1>, how often: Talk about things you had done | Student questionnaire |
| `PA154Q06IA` | When child attended the first year of <ISCED 1>, how often: Talk about what you had read | Student questionnaire |
| `PA154Q07IA` | When child attended the first year of <ISCED 1>, how often: Play word games | Student questionnaire |
| `PA154Q08IA` | When child attended the first year of <ISCED 1>, how often: Write letters or words | Student questionnaire |
| `PA154Q09IA` | When child attended the first year of <ISCED 1>, how often: Read aloud signs and labels | Student questionnaire |
| `PA154Q10HA` | When child attended the first year of <ISCED 1>, how often: Say counting rhymes or sing counting songs | Student questionnaire |
| `PA155Q01IA` | In what language did most of the activities in the previous question take place? | Student questionnaire |
| `PA156Q01HA` | Thinking back to when your child was about 10 years old, how often would he or she read the following? Comic books | Student questionnaire |
| `PA156Q02HA` | Thinking back to when your child was about 10 years old, how often would he or she read the following? Magazines | Student questionnaire |
| `PA156Q03HA` | Thinking back to when your child was about 10 years old, how often would he or she read the following? Books | Student questionnaire |
| `PA156Q04HA` | Thinking back to when your child was about 10 years old, how often would he or she read the following? Newspapers | Student questionnaire |
| `PA004Q02NA` | Thinking about <the last academic year>: I am supportive of my child's efforts at school and his/her achievements. | Student questionnaire |
| `PA004Q03NA` | Thinking about <the last academic year>: I support my child when he/she is facing difficulties at school. | Student questionnaire |
| `PA004Q04NA` | Thinking about <the last academic year>: I encourage my child to be confident. | Student questionnaire |
| `PA008Q01TA` | <the last academic year>: Discussed my child's behaviour with a teacher on my own initiative. | Student questionnaire |
| `PA008Q02TA` | <the last academic year>: Discussed my child's behaviour on the initiative of one of his/her teachers. | Student questionnaire |
| `PA008Q03TA` | <the last academic year>: Discussed my child's progress with a teacher on my own initiative. | Student questionnaire |
| `PA008Q04TA` | <the last academic year>: Discussed my child's progress on the initiative of one of their teachers. | Student questionnaire |
| `PA008Q05TA` | <the last academic year>: Participated in local school government, e.g. parent council or school management committee. | Student questionnaire |
| `PA008Q06NA` | <the last academic year>: Volunteered in physical or extra-curricular activities [...] | Student questionnaire |
| `PA008Q07NA` | <the last academic year>: Volunteered to support school activities [...] | Student questionnaire |
| `PA008Q08NA` | <the last academic year>: Attended a scheduled meeting or conferences for parents. | Student questionnaire |
| `PA008Q09NA` | <the last academic year>: Talked about how to support learning at home and homework with my child's teachers. | Student questionnaire |
| `PA008Q10NA` | <the last academic year>: Exchanged ideas on parenting [...] or the child's development with my child's teachers. | Student questionnaire |
| `PA009Q01NA` | <the last academic year>, participation hindered: The meeting times were inconvenient. | Student questionnaire |
| `PA009Q02NA` | <the last academic year>, participation hindered: I was not able to get off from work. | Student questionnaire |
| `PA009Q03NA` | <the last academic year>, participation hindered: I had no one to take care of my child/ children. | Student questionnaire |
| `PA009Q04NA` | <the last academic year>, participation hindered: The way to school is unsafe. | Student questionnaire |
| `PA009Q05NA` | <the last academic year>, participation hindered: I had problems with transportation. | Student questionnaire |
| `PA009Q06NA` | <the last academic year>, participation hindered: I felt unwelcome at my child's school. | Student questionnaire |
| `PA009Q07NA` | <the last academic year>, participation hindered: I feel generally awkward in a school. | Student questionnaire |
| `PA009Q08NA` | <the last academic year>, participation hindered: My <language skills> were not sufficient. | Student questionnaire |
| `PA009Q09NA` | <the last academic year>, participation hindered: I think participation is not relevant for my child's development. | Student questionnaire |
| `PA009Q10NA` | <the last academic year>, participation hindered: I do not know how I could participate in school activities. | Student questionnaire |
| `PA009Q11NA` | <the last academic year>, participation hindered: My child does not want me to participate. | Student questionnaire |
| `PA007Q01TA` | Agree: Most of my child's school teachers seem competent and dedicated. | Student questionnaire |
| `PA007Q02TA` | Agree: Standards of achievement are high in my child's school. | Student questionnaire |
| `PA007Q03TA` | Agree: I am happy with the content taught and the instructional methods used in my child's school. | Student questionnaire |
| `PA007Q04TA` | Agree: I am satisfied with the disciplinary atmosphere in my child's school. | Student questionnaire |
| `PA007Q05TA` | Agree: My child's progress is carefully monitored by the school. | Student questionnaire |
| `PA007Q06TA` | Agree: My child's school provides regular and useful information on my child's progress. | Student questionnaire |
| `PA007Q07TA` | Agree: My child's school does a good job in educating students. | Student questionnaire |
| `PA007Q09NA` | Agree: My child's school provides an inviting atmosphere for parents to get involved. | Student questionnaire |
| `PA007Q11NA` | Agree: My child's school provides effective communication between the school and families. | Student questionnaire |
| `PA007Q12NA` | Agree: My child's school involves parents in the school's decision-making process. | Student questionnaire |
| `PA007Q13NA` | Agree: My child's school offers parent education [...] or family support programmes [...] | Student questionnaire |
| `PA007Q14NA` | Agree: My child's school informs families about how to help students with homework and other school-related activities. | Student questionnaire |
| `PA007Q15NA` | Agree: My child's school cooperates with <community services> to strengthen school programmes and student development. | Student questionnaire |
| `PA005Q01TA` | Which of the following statements best describes the schooling available to students in your location? | Student questionnaire |
| `PA006Q01TA` | Importance for choosing a school: The school is at a short distance to home. | Student questionnaire |
| `PA006Q02TA` | Importance for choosing a school: The school has a good reputation. | Student questionnaire |
| `PA006Q03TA` | Importance for choosing a school: The school offers particular courses or school subjects. | Student questionnaire |
| `PA006Q04TA` | Importance for choosing a school: The school adheres to a particular <religious philosophy>. | Student questionnaire |
| `PA006Q05TA` | Importance for choosing a school: The school has a particular approach to <pedagogy/didactics, e.g. example>. | Student questionnaire |
| `PA006Q06TA` | Importance for choosing a school: Other family members attended the school. | Student questionnaire |
| `PA006Q07TA` | Importance for choosing a school: Expenses are low (e.g. tuition, books, room and board). | Student questionnaire |
| `PA006Q08TA` | Importance for choosing a school: The school has financial aid available, such as a school loan, scholarship, or grant. | Student questionnaire |
| `PA006Q09TA` | Importance for choosing a school: The school has an active and pleasant school climate. | Student questionnaire |
| `PA006Q10TA` | Importance for choosing a school: The academic achievements of students in the school are high. | Student questionnaire |
| `PA006Q11TA` | Importance for choosing a school: There is a safe school environment. | Student questionnaire |
| `PA006Q12HA` | Importance for choosing a school: The school has an international student body. | Student questionnaire |
| `PA006Q13HA` | Importance for choosing a school: The school offers exchange programmes with schools in other countries. | Student questionnaire |
| `PA006Q14HA` | Importance for choosing a school: The school has a focus on foreign language instruction. | Student questionnaire |
| `PA158Q01HA` | Statements about reading? I read only if I have to | Student questionnaire |
| `PA158Q02IA` | Statements about reading? Reading is one of my favourite hobbies | Student questionnaire |
| `PA158Q03HA` | Statements about reading? I like talking about books with other people | Student questionnaire |
| `PA158Q04IA` | Statements about reading? For me, reading is a waste of time | Student questionnaire |
| `PA158Q05HA` | Statements about reading? I read only to get information that I need | Student questionnaire |
| `PA159Q01HA` | About how much time do you usually spend reading for enjoyment? | Student questionnaire |
| `PA160Q01HA` | How often do you read these types of texts because you want to? Magazines | Student questionnaire |
| `PA160Q02HA` | How often do you read these types of texts because you want to? Comic books | Student questionnaire |
| `PA160Q03HA` | How often do you read these types of texts because you want to? Fiction (novels, narratives, stories) | Student questionnaire |
| `PA160Q04HA` | How often do you read these types of texts because you want to? Non-fiction books (informational, documentary) | Student questionnaire |
| `PA160Q05HA` | How often do you read these types of texts because you want to? Newspapers | Student questionnaire |
| `PA161Q01HA` | How often are you involved in reading activities: Reading emails | Student questionnaire |
| `PA161Q02HA` | How often are you involved in reading activities: <Chat on line> (e.g. <Whatsapp> , <Messenger>) | Student questionnaire |
| `PA161Q03HA` | How often are you involved in reading activities: Reading online news | Student questionnaire |
| `PA161Q05HA` | How often are you involved in reading activities: Searching information online to learn about a particular topic | Student questionnaire |
| `PA161Q06HA` | How often are you involved in reading activities: Taking part in online group discussions or forums | Student questionnaire |
| `PA161Q07HA` | How often are you involved in reading activities: Searching for practical information online [...] | Student questionnaire |
| `PA162Q01HA` | Which of the following statements best describes how you read books (on any topic)? | Student questionnaire |
| `PA163Q01HA` | Which of the following statements best describes how you read the news (e.g. politics, culture, sport, local news)? | Student questionnaire |
| `PA166Q01HA` | How many languages, including the language(s) you speak at home, do you speak well enough to converse with others? | Student questionnaire |
| `PA167Q02HA` | Agree: Immigrant children should have the same opportunities for education that other children in the country have. | Student questionnaire |
| `PA167Q03HA` | Agree: Immigrants who live in a country for several years should have the opportunity to vote in elections. | Student questionnaire |
| `PA167Q04HA` | Agree: Immigrants should have the opportunity to continue their own customs and lifestyle. | Student questionnaire |
| `PA167Q05HA` | Agree: Immigrants should have all the same rights that everyone else in the country has. | Student questionnaire |
| `PA168Q01HA` | How well does the following describe you: I want to learn how people live in different countries. | Student questionnaire |
| `PA168Q02HA` | How well does the following describe you: I want to learn more about the religions of the world. | Student questionnaire |
| `PA168Q03HA` | How well does the following describe you: I am interested in how people from various cultures see the world. | Student questionnaire |
| `PA168Q06HA` | How well does the following describe you: I am interested in finding out about the traditions of other cultures. | Student questionnaire |
| `PA169Q01HA` | How interested are you in the following issues? Political or social issues in your country | Student questionnaire |
| `PA169Q02HA` | How interested are you in the following issues? Political or social issues in other countries | Student questionnaire |
| `PA169Q03HA` | How interested are you in the following issues? Environmental issues in your country | Student questionnaire |
| `PA169Q04HA` | How interested are you in the following issues? Environmental issues in other countries | Student questionnaire |
| `PA169Q05HA` | How interested are you in the following issues? History, culture and arts of your country | Student questionnaire |
| `PA169Q06HA` | How interested are you in the following issues? History, culture and arts of other countries | Student questionnaire |
| `PA170Q01HA` | How informed are you about the following topics?Climate change and global warming | Student questionnaire |
| `PA170Q02HA` | How informed are you about the following topics?Global health (e.g. epidemics) | Student questionnaire |
| `PA170Q04HA` | How informed are you about the following topics?Migration (movement of people) | Student questionnaire |
| `PA170Q07HA` | How informed are you about the following topics?International conflicts | Student questionnaire |
| `PA170Q08HA` | How informed are you about the following topics?Hunger or malnutrition in different parts of the world | Student questionnaire |
| `PA170Q09HA` | How informed are you about the following topics?Causes of poverty | Student questionnaire |
| `PA170Q12HA` | How informed are you about the following topics?Equality between men and women in different parts of the world | Student questionnaire |
| `PA171Q01HA` | Involved in: I reduce the energy I use at home [...] to protect the environment. | Student questionnaire |
| `PA171Q03HA` | Involved in: I choose certain products for ethical or environmental reasons, even if they are a bit more expensive. | Student questionnaire |
| `PA171Q04HA` | Involved in: I sign environmental or social petitions online. | Student questionnaire |
| `PA171Q05HA` | Involved in: I keep myself informed about world events instantly via <Twitter> or <Facebook>. | Student questionnaire |
| `PA171Q06HA` | Involved in: I boycott products or companies for political, ethical or environmental reasons. | Student questionnaire |
| `PA171Q08HA` | Involved in: I participate in activities promoting equality between men and women. | Student questionnaire |
| `PA171Q09HA` | Involved in: I participate in activities in favour of environmental protection. | Student questionnaire |
| `PA171Q10HA` | Involved in: I regularly read websites on international social issues (e.g. poverty, human rights). | Student questionnaire |
| `PA172Q01WA` | Which of the following do you expect your child to complete? [ISCED level 2] | Student questionnaire |
| `PA172Q02WA` | Which of the following do you expect your child to complete? [ISCED level 3B or C] | Student questionnaire |
| `PA172Q03WA` | Which of the following do you expect your child to complete? [ISCED level 3A] | Student questionnaire |
| `PA172Q04WA` | Which of the following do you expect your child to complete? [ISCED level 4] | Student questionnaire |
| `PA172Q05WA` | Which of the following do you expect your child to complete? [ISCED level 5B] | Student questionnaire |
| `PA172Q06WA` | Which of the following do you expect your child to complete? [ISCED level 5A or 6] | Student questionnaire |
| `PA018Q01NA` | Child regularly attended prior to <grade 1 in ISCED 1>: Supervision and care [...] | Student questionnaire |
| `PA018Q02NA` | Child regularly attended prior to <grade 1 in ISCED 1>: Early childhood educational development [...] | Student questionnaire |
| `PA018Q03NA` | Child regularly attended prior to <grade 1 in ISCED 1>: Pre-primary education [...] | Student questionnaire |
| `PA177Q01HA` | Ages child attended <early childhood education and care arrangement> prior to <grade 1 in ISCED 1>: Up to age 1 | Student questionnaire |
| `PA177Q02HA` | Ages child attended <early childhood education and care arrangement> prior to <grade 1 in ISCED 1>: Age 1 | Student questionnaire |
| `PA177Q03HA` | Ages child attended <early childhood education and care arrangement> prior to <grade 1 in ISCED 1>: Age 2 | Student questionnaire |
| `PA177Q04HA` | Ages child attended <early childhood education and care arrangement> prior to <grade 1 in ISCED 1>: Age 3 | Student questionnaire |
| `PA177Q05HA` | Ages child attended <early childhood education and care arrangement> prior to <grade 1 in ISCED 1>: Age 4 | Student questionnaire |
| `PA177Q06HA` | Ages child attended <early childhood education and care arrangement> prior to <grade 1 in ISCED 1>: Age 5 | Student questionnaire |
| `PA177Q07HA` | Ages child attended <early childhood education and care arrangement> prior to <grade 1 in ISCED 1>: Age 6 | Student questionnaire |
| `PA177Q08HA` | Ages child attended <early childhood education and care arrangement> prior to <grade 1 in ISCED 1>: Age 7 | Student questionnaire |
| `PA180Q01HA` | What was the most important reason why your child attended an [early childhood education and care arrangement]? | Student questionnaire |
| `PA182Q01HA` | Hours per week child attended a <early childhood education and care arrangement> at the age of three years | Student questionnaire |
| `PA175Q01HA` | Did your child attend the following additional instructions during [ISCED 1]? [Enrichment lessons] in [test language] | Student questionnaire |
| `PA175Q02HA` | Did your child attend the following additional instructions during [ISCED 1]? [Remedial lessons] in [test language] | Student questionnaire |
| `PA041Q01TA` | In the last twelve months, about how much would you have paid to educational providers for services? | Student questionnaire |
| `PA042Q01TA` | What is your annual household income? | Student questionnaire |
| `PARED` | Index highest parental education in years of schooling | Student questionnaire |
| `PAREDINT` | Index highest parental education (international years of schooling scale) | Student questionnaire |
| `PASCHPOL` | School policies for parental involvement (WLE) | Student questionnaire |

## School context items (student-reported)

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `SC001Q01TA` | Which of the following definitions best describes the community in which your school is located? | School questionnaire |
| `SC013Q01TA` | Is your school a public or a private school? | School questionnaire |
| `SC016Q01TA` | Percentage of total funding for school year from: Government | School questionnaire |
| `SC016Q02TA` | Percentage of total funding for school year from: Student fees or school charges paid by parents | School questionnaire |
| `SC016Q03TA` | Percentage of total funding for school year from: Benefactors, donations, bequests, sponsorships, parent fundraising | School questionnaire |
| `SC016Q04TA` | Percentage of total funding for school year from: Other | School questionnaire |
| `SC017Q01NA` | School's instruction hindered by: A lack of teaching staff. | School questionnaire |
| `SC017Q02NA` | School's instruction hindered by: Inadequate or poorly qualified teaching staff. | School questionnaire |
| `SC017Q03NA` | School's instruction hindered by: A lack of assisting staff. | School questionnaire |
| `SC017Q04NA` | School's instruction hindered by: Inadequate or poorly qualified assisting staff. | School questionnaire |
| `SC017Q05NA` | School's instruction hindered by: A lack of educational material [...] | School questionnaire |
| `SC017Q06NA` | School's instruction hindered by: Inadequate or poor quality educational material [...] | School questionnaire |
| `SC017Q07NA` | School's instruction hindered by: A lack of physical infrastructure [...] | School questionnaire |
| `SC017Q08NA` | School's instruction hindered by: Inadequate or poor quality physical infrastructure [...] | School questionnaire |
| `SC161Q01SA` | Main responsibility for career guidance at school: Not applicable, career guidance is not available in this school | School questionnaire |
| `SC161Q02SA` | Main responsibility for career guidance at school: All teachers share the responsibility for career guidance | School questionnaire |
| `SC161Q03SA` | Main responsibility for career guidance at school: Specific teachers have the main responsibility for career guidance | School questionnaire |
| `SC161Q04SA` | Main responsibility for career guidance at school: We have [...] career guidance counsellors employed at school | School questionnaire |
| `SC161Q05SA` | Main responsibility for career guidance at school: We have [...] career guidance counsellors who regularly visit [...] | School questionnaire |
| `SC162Q01SA` | If career guidance is available at your school, which of the statements below best describes the situation for [...] | School questionnaire |
| `SC155Q01HA` | School's capacity using digital devices: The number of digital devices connected to the Internet is sufficient | School questionnaire |
| `SC155Q02HA` | School's capacity using digital devices: The school's Internet bandwidth or speed is sufficient | School questionnaire |
| `SC155Q03HA` | School's capacity using digital devices: The number of digital devices for instruction is sufficient | School questionnaire |
| `SC155Q04HA` | School's capacity using digital devices: Digital devices [...] are sufficiently powerful in terms of computing capacity | School questionnaire |
| `SC155Q05HA` | School's capacity using digital devices: The availability of adequate software is sufficient | School questionnaire |
| `SC155Q06HA` | School's capacity using digital devices: Teachers have the [...] skills to integrate digital devices in instruction | School questionnaire |
| `SC155Q07HA` | School's capacity using digital devices: Teachers have sufficient time to prepare lessons integrating digital devices | School questionnaire |
| `SC155Q08HA` | School's capacity using digital devices: Effective professional resources for teachers to learn how to use digital [...] | School questionnaire |
| `SC155Q09HA` | School's capacity using digital devices: An effective online learning support platform is available | School questionnaire |
| `SC155Q10HA` | School's capacity using digital devices: Teachers are provided with incentives to integrate digital devices in [...] | School questionnaire |
| `SC155Q11HA` | School's capacity using digital devices: The school has sufficient qualified technical assistant staff | School questionnaire |
| `SC156Q01HA` | At school: Its own written statement about the use of digital devices | School questionnaire |
| `SC156Q02HA` | At school: Its own written statement specifically about the use of digital devices for pedagogical purposes | School questionnaire |
| `SC156Q03HA` | At school: A programme to use digital devices for teaching and learning in specific subjects | School questionnaire |
| `SC156Q04HA` | At school: Regular discussions with teaching staff about the use of digital devices for pedagogical purposes | School questionnaire |
| `SC156Q05HA` | At school: A specific programme to prepare students for responsible Internet behaviour | School questionnaire |
| `SC156Q06HA` | At school: A specific policy about using Social Networks (<Facebook>, etc.) in teaching and learning | School questionnaire |
| `SC156Q07HA` | At school: A specific programme to promote collaboration on the use of digital devices among teachers | School questionnaire |
| `SC156Q08HA` | At school: Scheduled time for teachers to meet to share, evaluate or develop instructional materials and [...] | School questionnaire |
| `SC011Q01TA` | Which of the following statements best describes the schooling available to students in your location? | School questionnaire |
| `SC012Q01TA` | Student admission to school: Student's record of academic performance (including placement tests) | School questionnaire |
| `SC012Q02TA` | Student admission to school: Recommendation of feeder schools | School questionnaire |
| `SC012Q03TA` | Student admission to school: Parents' endorsement of the instructional or religious philosophy of the school | School questionnaire |
| `SC012Q04TA` | Student admission to school: Whether the student requires or is interested in a special programme | School questionnaire |
| `SC012Q05TA` | Student admission to school: Preference given to family members of current or former students | School questionnaire |
| `SC012Q06TA` | Student admission to school: Residence in a particular area | School questionnaire |
| `SC012Q07TA` | Student admission to school: Other | School questionnaire |
| `SC042Q01TA` | School's policy for <national modal grade for 15-year-olds>: Students are grouped by ability into different classes. | School questionnaire |
| `SC042Q02TA` | School's policy for <national modal grade for 15-year-olds>: Students are grouped by ability within their classes. | School questionnaire |
| `SC154Q01HA` | School's use of assessments of students: To guide students' learning | School questionnaire |
| `SC154Q02WA` | School's use of assessments of students: To inform parents about their child's progress | School questionnaire |
| `SC154Q03WA` | School's use of assessments of students: To make decisions about students' retention or promotion | School questionnaire |
| `SC154Q04WA` | School's use of assessments of students: To group students for instructional purposes | School questionnaire |
| `SC154Q05WA` | School's use of assessments of students: To compare the school to <district or national> performance | School questionnaire |
| `SC154Q06WA` | School's use of assessments of students: To monitor the schools progress from year to year | School questionnaire |
| `SC154Q07WA` | School's use of assessments of students: To make judgements about teachers' effectiveness | School questionnaire |
| `SC154Q08WA` | School's use of assessments of students: To identify aspects of instruction or the curriculum that could be improved | School questionnaire |
| `SC154Q09HA` | School's use of assessments of students: To adapt teaching to the students' needs | School questionnaire |
| `SC154Q10WA` | School's use of assessments of students: To compare the school with other schools | School questionnaire |
| `SC154Q11HA` | School's use of assessments of students: To award certificates to students | School questionnaire |
| `SC036Q01TA` | Use of achievement data in school: Achievement data are posted publicly (e.g. in the media) | School questionnaire |
| `SC036Q02TA` | Use of achievement data in school: Achievement data are tracked over time by an administrative authority | School questionnaire |
| `SC036Q03NA` | Use of achievement data in school: Achievement data are provided directly to parents | School questionnaire |
| `SC037Q01TA` | Quality assurance at school: Internal evaluation/Self-evaluation | School questionnaire |
| `SC037Q02TA` | Quality assurance at school: External evaluation | School questionnaire |
| `SC037Q03TA` | Quality assurance at school: Written specification of the school's curricular profile and educational goals | School questionnaire |
| `SC037Q04TA` | Quality assurance at school: Written specification of student performance standards | School questionnaire |
| `SC037Q05NA` | Quality assurance at school: Systematic recording of data such as [...] attendance and professional development | School questionnaire |
| `SC037Q06NA` | Quality assurance at school: Systematic recording of student test results and graduation rates | School questionnaire |
| `SC037Q07TA` | Quality assurance at school: Seeking written feedback from students (e.g. regarding lessons, teachers or resources) | School questionnaire |
| `SC037Q08TA` | Quality assurance at school: Teacher mentoring | School questionnaire |
| `SC037Q09TA` | Quality assurance at school: Regular consultation aimed at school improvement [...] over a period of at least six months | School questionnaire |
| `SC037Q10NA` | Quality assurance at school: Implementation of a standardised policy for reading subjects [...] | School questionnaire |
| `SC165Q01HA` | Teachers' practices: [...] students learn about the histories of diverse cultural groups that live in <country of test>. | School questionnaire |
| `SC165Q02HA` | Teachers' practices: [...] students learn about the histories of diverse cultural groups that live in other countries. | School questionnaire |
| `SC165Q03HA` | Teachers' practices: [...] students learn about the cultures [...] of [...] groups that live in <country of test> | School questionnaire |
| `SC165Q04HA` | Teachers' practices: [...] students learn about different cultural perspectives on historical and social events. | School questionnaire |
| `SC165Q05HA` | Teachers' practices: Our school supports activities that encourage students expression of diverse identities [...] | School questionnaire |
| `SC165Q06HA` | Teachers' practices: Our school offers an exchange programme with schools in other countries. | School questionnaire |
| `SC165Q07HA` | Teachers' practices: Our school organises multicultural events (e.g. cultural diversity day). | School questionnaire |
| `SC165Q08HA` | Teachers' practices: In our school, we celebrate festivities from other cultures. | School questionnaire |
| `SC165Q09HA` | Teachers' practices: In our school, students are encouraged to communicate with people from other cultures via [...] | School questionnaire |
| `SC165Q10HA` | Teachers' practices: Our school adopts different approaches to educate students about cultural differences [...] | School questionnaire |
| `SC166Q02HA` | Opinion shared by teaching staff: It is important for students to learn that people from other cultures can have [...] | School questionnaire |
| `SC166Q03HA` | Opinion shared by teaching staff: Respecting other cultures is something that students should learn as early as possible | School questionnaire |
| `SC166Q05HA` | Opinion shared by teaching staff: In the classroom, it is important that students of different origins recognise [...] | School questionnaire |
| `SC166Q06HA` | Opinion shared by teaching staff: When there are conflicts between students of different origins, they should be [...] | School questionnaire |
| `SC167Q01HA` | Curriculum for the following in <national modal grade for 15-year-olds>: Communicating with people from different [...] | School questionnaire |
| `SC167Q02HA` | Curriculum for the following in <national modal grade for 15-year-olds>: Knowledge of different cultures | School questionnaire |
| `SC167Q03HA` | Curriculum for the following in <national modal grade for 15-year-olds>: Openness to intercultural experiences | School questionnaire |
| `SC167Q04HA` | Curriculum for the following in <national modal grade for 15-year-olds>: Respect for cultural diversity | School questionnaire |
| `SC167Q05HA` | Curriculum for the following in <national modal grade for 15-year-olds>: Foreign languages | School questionnaire |
| `SC167Q06HA` | Curriculum for the following in <national modal grade for 15-year-olds>: Critical thinking skills | School questionnaire |
| `SC158Q01HA` | Formal curriculum in <national modal grade for 15-year-olds>: Climate change and global warming | School questionnaire |
| `SC158Q02HA` | Formal curriculum in <national modal grade for 15-year-olds>: Global health (e.g. epidemics) | School questionnaire |
| `SC158Q04HA` | Formal curriculum in <national modal grade for 15-year-olds>: Migration (movement of people) | School questionnaire |
| `SC158Q07HA` | Formal curriculum in <national modal grade for 15-year-olds>: International conflicts | School questionnaire |
| `SC158Q08HA` | Formal curriculum in <national modal grade for 15-year-olds>: Hunger or malnutrition in different parts of the world | School questionnaire |
| `SC158Q09HA` | Formal curriculum in <national modal grade for 15-year-olds>: Causes of poverty | School questionnaire |
| `SC158Q12HA` | Formal curriculum in <national modal grade for 15-year-olds>: Equality between men and women in [...] the world | School questionnaire |
| `SC061Q01TA` | Extent to which student learning is hindered by: Student truancy | School questionnaire |
| `SC061Q02TA` | Extent to which student learning is hindered by: Students skipping classes | School questionnaire |
| `SC061Q03TA` | Extent to which student learning is hindered by: Students lacking respect for teachers | School questionnaire |
| `SC061Q04TA` | Extent to which student learning is hindered by: Student use of alcohol or illegal drugs | School questionnaire |
| `SC061Q05TA` | Extent to which student learning is hindered by: Students intimidating or bullying other students | School questionnaire |
| `SC061Q11HA` | Extent to which student learning is hindered by: Students not being attentive | School questionnaire |
| `SC061Q06TA` | Extent to which student learning is hindered by: Teachers not meeting individual students' needs | School questionnaire |
| `SC061Q07TA` | Extent to which student learning is hindered by: Teacher absenteeism | School questionnaire |
| `SC061Q08TA` | Extent to which student learning is hindered by: Staff resisting change | School questionnaire |
| `SC061Q09TA` | Extent to which student learning is hindered by: Teachers being too strict with students | School questionnaire |
| `SC061Q10TA` | Extent to which student learning is hindered by: Teachers not being well prepared for classes | School questionnaire |
| `SC002Q01TA` | As of <February 1, 2018>, what was the total school enrolment (number of students)? Number of boys | School questionnaire |
| `SC002Q02TA` | As of <February 1, 2018>, what was the total school enrolment (number of students)? Number of girls | School questionnaire |
| `SC048Q01NA` | Percentage <national modal grade for 15-year-olds>: Students whose <heritage language> is different from <test language> | School questionnaire |
| `SC048Q02NA` | Percentage <national modal grade for 15-year-olds>: Students with special needs | School questionnaire |
| `SC048Q03NA` | Percentage <national modal grade for 15-year-olds>: Students from socioeconomically disadvantaged homes | School questionnaire |
| `SC004Q01TA` | At your school, what is the total number of students in the <national modal grade for 15-year-olds>? | School questionnaire |
| `SC004Q02TA` | Approximately, how many computers are available for these students for educational purposes? | School questionnaire |
| `SC004Q03TA` | Approximately, how many of these computers are connected to Internet/World Wide Web? | School questionnaire |
| `SC004Q04NA` | Approximately, how many of these computers are portable (e.g. laptop, tablet)? | School questionnaire |
| `SC004Q05NA` | Approximately, how many interactive Whiteboards are available in the school altogether? | School questionnaire |
| `SC004Q06NA` | Approximately, how many data projectors are available in the school altogether? | School questionnaire |
| `SC004Q07NA` | Approximately, how many computers with Internet connection are available for teachers in your school? | School questionnaire |
| `SC018Q01TA01` | Teachers in TOTAL: Full-time | School questionnaire |
| `SC018Q01TA02` | Teachers in TOTAL: Part-time | School questionnaire |
| `SC018Q02TA01` | Teachers <fully certified> by <the appropriate authority>: Full-time | School questionnaire |
| `SC018Q02TA02` | Teachers <fully certified> by <the appropriate authority>: Part-time | School questionnaire |
| `SC018Q05NA01` | Teachers with an <ISCED Level 5A Bachelor degree> qualification: Full-time | School questionnaire |
| `SC018Q05NA02` | Teachers with an <ISCED Level 5A Bachelor degree> qualification: Part-time | School questionnaire |
| `SC018Q06NA01` | Teachers with an <ISCED Level 5A Master's degree> qualification: Full-time | School questionnaire |
| `SC018Q06NA02` | Teachers with an <ISCED Level 5A Master's degree> qualification: Part-time | School questionnaire |
| `SC018Q07NA01` | Teachers with an <ISCED Level 6> qualification: Full-time | School questionnaire |
| `SC018Q07NA02` | Teachers with an <ISCED Level 6> qualification: Part-time | School questionnaire |
| `SC025Q01NA` | During the last three months, what percentage of teaching staff [...] attended a programme of professional development? | School questionnaire |
| `SC159Q01HA` | Does your school host visiting teachers from other countries? | School questionnaire |
| `SC003Q01TA` | What is the average size of <test language> classes in <national modal grade for 15-year-olds> in your school? | School questionnaire |
| `SC053Q01TA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: Band, orchestra or choir | School questionnaire |
| `SC053Q02TA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: School play or school musical | School questionnaire |
| `SC053Q03TA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: School yearbook, newspaper [...] | School questionnaire |
| `SC053Q04TA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: Volunteering [...] | School questionnaire |
| `SC053Q12IA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: Book club | School questionnaire |
| `SC053Q13IA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: Debating club or debating [...] | School questionnaire |
| `SC053Q09TA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: Art club or art activities | School questionnaire |
| `SC053Q10TA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: Sporting team or sporting [...] | School questionnaire |
| `SC053Q14IA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: Lectures and/or seminars [...] | School questionnaire |
| `SC053Q15IA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: Collaboration with local libraries | School questionnaire |
| `SC053Q16IA` | <This academic year>, activities offered to <national modal grade for 15-year-olds>: Collaboration with local newspapers | School questionnaire |
| `SC053D11TA` | <This academic year>,follow. activities/school offers<national modal grade for 15-year-olds>? <country specific item> | School questionnaire |
| `SC150Q01IA` | School's equity-oriented policies: These students attend regular classes and receive additional periods of [...] | School questionnaire |
| `SC150Q02IA` | School's equity-oriented policies: Before transferring to regular classes, [...] preparatory programme aimed at [...] | School questionnaire |
| `SC150Q03IA` | School's equity-oriented policies: Before transferring to regular classes, [...] instruction in school subjects [...] | School questionnaire |
| `SC150Q04IA` | School's equity-oriented policies: These students receive [...] amounts of instruction in their <heritage language> | School questionnaire |
| `SC150Q05IA` | Schools equity-oriented policies: Class size is reduced to cater to the special needs of these students. | School questionnaire |
| `SC164Q01HA` | In the last full academic year, what proportion of students in [...] final grade left school without a <certificate>? | School questionnaire |
| `SC064Q01TA` | Proportion of parents: Discussed their child's progress with a teacher on their own initiative | School questionnaire |
| `SC064Q02TA` | Proportion of parents: Discussed their child's progress on the initiative of one of their child's teachers | School questionnaire |
| `SC064Q03TA` | Proportion of parents: Participated in local school government (e.g. parent council or school management committee) | School questionnaire |
| `SC064Q04NA` | Proportion of parents: Volunteered in physical or extra-curricular activities [...] | School questionnaire |
| `SC152Q01HA` | Does your school offer additional <test language> lessons [...] during the usual school hours? | School questionnaire |
| `SC160Q01WA` | What is the purpose of these additional <test language> lessons? | School questionnaire |
| `SC052Q01NA` | For 15-year old students, school provides study help: Room(s) where the students can do their homework | School questionnaire |
| `SC052Q02NA` | For 15-year old students, school provides study help: Staff help with homework | School questionnaire |
| `SC052Q03HA` | For 15-year old students, school provides study help: Peer-to-peer tutoring | School questionnaire |

## ICT familiarity items

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `IC001Q01TA` | Available for you to use at home: Desktop computer | Student questionnaire |
| `IC001Q02TA` | Available for you to use at home: Portable laptop, or notebook | Student questionnaire |
| `IC001Q03TA` | Available for you to use at home: <Tablet computer> (e.g. <iPad>, <BlackBerry PlayBook>) | Student questionnaire |
| `IC001Q04TA` | Available for you to use at home: Internet connection | Student questionnaire |
| `IC001Q05TA` | Available for you to use at home: <Video games console>, e.g. <Sony PlayStation> | Student questionnaire |
| `IC001Q06TA` | Available for you to use at home: <Cell phone> (without Internet access) | Student questionnaire |
| `IC001Q07TA` | Available for you to use at home: <Cell phone> (with Internet access) | Student questionnaire |
| `IC001Q08TA` | Available for you to use at home: Portable music player (Mp3/Mp4 player, iPod or similar) | Student questionnaire |
| `IC001Q09TA` | Available for you to use at home: Printer | Student questionnaire |
| `IC001Q10TA` | Available for you to use at home: USB (memory) stick | Student questionnaire |
| `IC001Q11TA` | Available for you to use at home: <ebook reader>, e.g. <Amazon Kindle> | Student questionnaire |
| `IC009Q01TA` | Available for you to use at school: Desktop computer | Student questionnaire |
| `IC009Q02TA` | Available for you to use at school: Portable laptop or notebook | Student questionnaire |
| `IC009Q03TA` | Available for you to use at school: <Tablet computer> (e.g. <iPad>, <BlackBerry PlayBook>) | Student questionnaire |
| `IC009Q05NA` | Available for you to use at school: Internet connected school computers | Student questionnaire |
| `IC009Q06NA` | Available for you to use at school: Internet connection via wireless network | Student questionnaire |
| `IC009Q07NA` | Available for you to use at school: Storage space for school-related data, e.g. a folder for own documents | Student questionnaire |
| `IC009Q08TA` | Available for you to use at school: USB (memory) stick | Student questionnaire |
| `IC009Q09TA` | Available for you to use at school: <ebook reader>, e.g. <Amazon Kindle> | Student questionnaire |
| `IC009Q10NA` | Available for you to use at school: Data projector, e.g. for slide presentations | Student questionnaire |
| `IC009Q11NA` | Available for you to use at school: Interactive Whiteboard, e.g. <Smartboard> | Student questionnaire |
| `IC002Q01HA` | How old were you when you first used a digital device? | Student questionnaire |
| `IC004Q01HA` | How old were you when you first accessed the Internet? | Student questionnaire |
| `IC005Q01TA` | During a typical weekday, for how long do you use the Internet at school? | Student questionnaire |
| `IC006Q01TA` | During a typical weekday, for how long do you use the Internet outside of school? | Student questionnaire |
| `IC007Q01TA` | On a typical weekend day, for how long do you use the Internet outside of school? | Student questionnaire |
| `IC150Q01HA` | Time spent using digital devices during classroom lessons in a typical school week: <Test language lessons> | Student questionnaire |
| `IC150Q02HA` | Time spent using digital devices during classroom lessons in a typical school week: <Mathematics> | Student questionnaire |
| `IC150Q03HA` | Time spent using digital devices during classroom lessons in a typical school week: <Science> | Student questionnaire |
| `IC150Q04HA` | Time spent using digital devices during classroom lessons in a typical school week: <Foreign language> | Student questionnaire |
| `IC150Q05HA` | Time spent using digital devices during classroom lessons in a typical school week: <Social sciences> | Student questionnaire |
| `IC150Q06HA` | Time spent using digital devices during classroom lessons in a typical school week: Music | Student questionnaire |
| `IC150Q07HA` | Time spent using digital devices during classroom lessons in a typical school week: Sports | Student questionnaire |
| `IC150Q08HA` | Time spent using digital devices during classroom lessons in a typical school week: <Performing arts> | Student questionnaire |
| `IC150Q09HA` | Time spent using digital devices during classroom lessons in a typical school week: <Visual arts> | Student questionnaire |
| `IC151Q01HA` | Time spent using digital devices outside of classroom lessons in a typical school week: <Test language lessons> | Student questionnaire |
| `IC151Q02HA` | Time spent using digital devices outside of classroom lessons in a typical school week: <Mathematics> | Student questionnaire |
| `IC151Q03HA` | Time spent using digital devices outside of classroom lessons in a typical school week: <Science> | Student questionnaire |
| `IC151Q04HA` | Time spent using digital devices outside of classroom lessons in a typical school week: <Foreign language> | Student questionnaire |
| `IC151Q05HA` | Time spent using digital devices outside of classroom lessons in a typical school week: <Social sciences> | Student questionnaire |
| `IC151Q06HA` | Time spent using digital devices outside of classroom lessons in a typical school week: Music | Student questionnaire |
| `IC151Q07HA` | Time spent using digital devices outside of classroom lessons in a typical school week: Sports | Student questionnaire |
| `IC151Q08HA` | Time spent using digital devices outside of classroom lessons in a typical school week: <Performing arts> | Student questionnaire |
| `IC151Q09HA` | Time spent using digital devices outside of classroom lessons in a typical school week: <Visual arts> | Student questionnaire |
| `IC152Q01HA` | Digital device used for learning or teaching during lessons within the last month: <Test language lessons> | Student questionnaire |
| `IC152Q02HA` | Digital device used for learning or teaching during lessons within the last month: <Mathematics> | Student questionnaire |
| `IC152Q03HA` | Digital device used for learning or teaching during lessons within the last month: <Science> | Student questionnaire |
| `IC152Q04HA` | Digital device used for learning or teaching during lessons within the last month: <Foreign language> | Student questionnaire |
| `IC152Q05HA` | Digital device used for learning or teaching during lessons within the last month: <Social sciences> | Student questionnaire |
| `IC152Q06HA` | Digital device used for learning or teaching during lessons within the last month: Music | Student questionnaire |
| `IC152Q07HA` | Digital device used for learning or teaching during lessons within the last month: Sports | Student questionnaire |
| `IC152Q08HA` | Digital device used for learning or teaching during lessons within the last month: <Performing arts> | Student questionnaire |
| `IC152Q09HA` | Digital device used for learning or teaching during lessons within the last month: <Visual arts> | Student questionnaire |
| `IC008Q01TA` | Use digital devices outside of school: Playing one-player games. | Student questionnaire |
| `IC008Q02TA` | Use digital devices outside of school: Playing collaborative online games. | Student questionnaire |
| `IC008Q03TA` | Use digital devices outside of school: Using email. | Student questionnaire |
| `IC008Q04TA` | Use digital devices outside of school: <Chatting online> (e.g. <MSN>). | Student questionnaire |
| `IC008Q05TA` | Use digital devices outside of school: Participating in Social Networks (e.g. <Facebook>, <MySpace>). | Student questionnaire |
| `IC008Q07NA` | Use digital devices outside of school: Playing online games via Social Networks (e.g. <Farmville>, <The Sims Social>). | Student questionnaire |
| `IC008Q08TA` | Use digital devices outside of school: Browsing the Internet for fun (such as watching videos, e.g. <YouTube>). | Student questionnaire |
| `IC008Q09TA` | Use digital devices outside of school: Reading news on the Internet (e.g. current affairs). | Student questionnaire |
| `IC008Q10TA` | Use digital devices outside of school: Obtaining practical information from the Internet [...] | Student questionnaire |
| `IC008Q11TA` | Use digital devices outside of school: Downloading music, films, games or software from the Internet. | Student questionnaire |
| `IC008Q12TA` | Use digital devices outside of school: Uploading your own created contents for sharing [...] | Student questionnaire |
| `IC008Q13NA` | Use digital devices outside of school: Downloading new apps on a mobile device. | Student questionnaire |
| `IC010Q01TA` | Use digital devices outside of school: Browsing the Internet for schoolwork [...] | Student questionnaire |
| `IC010Q02NA` | Use digital devices outside of school: Browsing the Internet to follow up lessons, e.g. for finding explanations. | Student questionnaire |
| `IC010Q03TA` | Use digital devices outside of school: Using email for communication with other students about schoolwork. | Student questionnaire |
| `IC010Q04TA` | Use digital devices outside of school: Using email for communication with teachers and submission of homework or [...] | Student questionnaire |
| `IC010Q05NA` | Use digital devices outside of school: Using Social Networks for communication with other students about schoolwork. | Student questionnaire |
| `IC010Q06NA` | Use digital devices outside of school: Using Social Networks for communication with teachers [...] | Student questionnaire |
| `IC010Q07TA` | Use digital devices outside of school: Downloading, uploading or browsing material from my school's website [...] | Student questionnaire |
| `IC010Q08TA` | Use digital devices outside of school: Checking the school's website for announcements, e.g. absence of teachers. | Student questionnaire |
| `IC010Q09NA` | Use digital devices outside of school: Doing homework on a computer. | Student questionnaire |
| `IC010Q10NA` | Use digital devices outside of school: Doing homework on a mobile device. | Student questionnaire |
| `IC010Q11HA` | Use digital devices outside of school: Using learning apps or learning websites on a computer. | Student questionnaire |
| `IC010Q12HA` | Use digital devices outside of school: Using learning apps or learning websites on a mobile device. | Student questionnaire |
| `IC011Q01TA` | Use digital devices at school: <Chatting on line> at school. | Student questionnaire |
| `IC011Q02TA` | Use digital devices at school: Using email at school. | Student questionnaire |
| `IC011Q03TA` | Use digital devices at school: Browsing the Internet for schoolwork. | Student questionnaire |
| `IC011Q04TA` | Use digital devices at school: Downloading, uploading or browsing material from the school's website (e.g. <intranet>). | Student questionnaire |
| `IC011Q05TA` | Use digital devices at school: Posting my work on the school's website. | Student questionnaire |
| `IC011Q06TA` | Use digital devices at school: Playing simulations at school. | Student questionnaire |
| `IC011Q07TA` | Use digital devices at school: Practicing and drilling, foreign language learning or math. | Student questionnaire |
| `IC011Q08TA` | Use digital devices at school: Doing homework on a school computer. | Student questionnaire |
| `IC011Q09TA` | Use digital devices at school: Using school computers for group work and communication with other students. | Student questionnaire |
| `IC011Q10HA` | Use digital devices at school: Using learning apps or learning websites. | Student questionnaire |
| `IC013Q01NA` | Agree: I forget about time when I'm using digital devices. | Student questionnaire |
| `IC013Q04NA` | Agree: The Internet is a great resource for obtaining information I am interested in (e.g. news, sports, dictionary). | Student questionnaire |
| `IC013Q05NA` | Agree: It is very useful to have Social Networks on the Internet. | Student questionnaire |
| `IC013Q11NA` | Agree: I am really excited discovering new digital devices or applications. | Student questionnaire |
| `IC013Q12NA` | Agree: I really feel bad if no Internet connection is possible. | Student questionnaire |
| `IC013Q13NA` | Agree: I like using digital devices. | Student questionnaire |
| `IC014Q03NA` | Agree: I feel comfortable using digital devices that I am less familiar with. | Student questionnaire |
| `IC014Q04NA` | Agree: If my friends and relatives want to buy new digital devices or applications, I can give them advice. | Student questionnaire |
| `IC014Q06NA` | Agree: I feel comfortable using my digital devices at home. | Student questionnaire |
| `IC014Q08NA` | Agree: When I come across problems with digital devices, I think I can solve them. | Student questionnaire |
| `IC014Q09NA` | Agree: If my friends and relatives have a problem with digital devices, I can help them. | Student questionnaire |
| `IC015Q02NA` | Agree: If I need new software, I install it by myself. | Student questionnaire |
| `IC015Q03NA` | Agree: I read information about digital devices to be independent. | Student questionnaire |
| `IC015Q05NA` | Agree: I use digital devices as I want to use them. | Student questionnaire |
| `IC015Q07NA` | Agree: If I have a problem with digital devices I start to solve it on my own. | Student questionnaire |
| `IC015Q09NA` | Agree: If I need a new application, I choose it by myself. | Student questionnaire |
| `IC016Q01NA` | Agree: To learn something new about digital devices, I like to talk about them with my friends. | Student questionnaire |
| `IC016Q02NA` | Agree: I like to exchange solutions to problems with digital devices with others on the Internet. | Student questionnaire |
| `IC016Q04NA` | Agree: I like to meet friends and play computer and video games with them. | Student questionnaire |
| `IC016Q05NA` | Agree: I like to share information about digital devices with my friends. | Student questionnaire |
| `IC016Q07NA` | Agree: I learn a lot about digital media by discussing with my friends and relatives. | Student questionnaire |
| `IC169Q01HA` | Which of the following statements best describes how you read the news (e.g. politics, culture, sport, local news)? | Student questionnaire |
| `ICTHOME` | ICT available at home | Student questionnaire |
| `ICTSCH` | ICT available at school | Student questionnaire |
| `ICTRES` | ICT resources (WLE) | Student questionnaire |
| `ICTCLASS` | Subject-related ICT use during lessons (WLE) | Student questionnaire |
| `ICTOUTSIDE` | Subject-related ICT use outside of lessons (WLE) | Student questionnaire |

## Expected occupation items

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `EC031Q01TA` | Did you change schools when you were attending <ISCED 1>? | Student questionnaire |
| `EC032Q01TA` | Did you change schools when you were attending <ISCED 2>? | Student questionnaire |
| `EC033Q01NA` | Have you ever changed your <study programme>? | Student questionnaire |
| `EC150Q01WA` | Find out about future study or types of work: I did an internship. | Student questionnaire |
| `EC150Q02WA` | Find out about future study or types of work: I attended <job shadowing or work-site visits>. | Student questionnaire |
| `EC150Q03WA` | Find out about future study or types of work: I visited a <job fair>. | Student questionnaire |
| `EC150Q04WA` | Find out about future study or types of work: I spoke to a <career advisor> at my school. | Student questionnaire |
| `EC150Q05WA` | Find out about future study or types of work: I spoke to a <career advisor> outside of my school. | Student questionnaire |
| `EC150Q06WA` | Find out about future study or types of work: I completed a questionnaire to find out about my interests and abilities. | Student questionnaire |
| `EC150Q07WA` | Find out about future study or types of work: I researched the Internet for information about careers. | Student questionnaire |
| `EC150Q08WA` | Find out about future study or types of work: I went to an organised tour in an <ISCED 3-5> institution. | Student questionnaire |
| `EC150Q09WA` | Find out about future study or types of work: I researched the Internet for information about <ISCED 3-5> programmes. | Student questionnaire |
| `EC150Q10WA` | Find out about future study or types of work: <country specific item> | Student questionnaire |
| `EC151Q01WA` | Acquired skills: How to find information on jobs I am interested in. Yes, at school | Student questionnaire |
| `EC151Q01WB` | Acquired skills: How to find information on jobs I am interested in. Yes, out of school | Student questionnaire |
| `EC151Q01WC` | Acquired skills: How to find information on jobs I am interested in. No, never | Student questionnaire |
| `EC151Q02WA` | Acquired skills: How to search for a job. Yes, at school | Student questionnaire |
| `EC151Q02WB` | Acquired skills: How to search for a job. Yes, out of school | Student questionnaire |
| `EC151Q02WC` | Acquired skills: How to search for a job. No, never | Student questionnaire |
| `EC151Q03WA` | Acquired skills: How to write a <rsum> or a summary of my qualifications. Yes, at school | Student questionnaire |
| `EC151Q03WB` | Acquired skills: How to write a <rsum> or a summary of my qualifications. Yes, out of school | Student questionnaire |
| `EC151Q03WC` | Acquired skills: How to write a <rsum> or a summary of my qualifications. No, never | Student questionnaire |
| `EC151Q04WA` | Acquired skills: How to prepare for a job interview. Yes, at school | Student questionnaire |
| `EC151Q04WB` | Acquired skills: How to prepare for a job interview. Yes, out of school | Student questionnaire |
| `EC151Q04WC` | Acquired skills: How to prepare for a job interview. No, never | Student questionnaire |
| `EC151Q05WA` | Acquired skills: How to find information on student financing (e.g. student loans or grants). Yes, at school | Student questionnaire |
| `EC151Q05WB` | Acquired skills: How to find information on student financing (e.g. student loans or grants). Yes, out of school | Student questionnaire |
| `EC151Q05WC` | Acquired skills: How to find information on student financing (e.g. student loans or grants). No, never | Student questionnaire |
| `EC152Q01HA` | What do you think you will be doing 5 years from now? | Student questionnaire |
| `EC153Q01HA` | Importance for decisions about future occupation: My parents' or guardians' expectations about my occupation | Student questionnaire |
| `EC153Q02HA` | Importance for decisions about future occupation: The plans my close friends have for their future | Student questionnaire |
| `EC153Q03HA` | Importance for decisions about future occupation: My school grades | Student questionnaire |
| `EC153Q04HA` | Importance for decisions about future occupation: The school subjects I am good at | Student questionnaire |
| `EC153Q05HA` | Importance for decisions about future occupation: My special talents | Student questionnaire |
| `EC153Q06HA` | Importance for decisions about future occupation: My hobbies | Student questionnaire |
| `EC153Q07HA` | Importance for decisions about future occupation: The social status of the occupation I want | Student questionnaire |
| `EC153Q08HA` | Importance for decisions about future occupation: Financial support for education or training | Student questionnaire |
| `EC153Q09HA` | Importance for decisions about future occupation: Education or training options for the occupation I want | Student questionnaire |
| `EC153Q10HA` | Importance for decisions about future occupation: Employment opportunities for the occupation I want | Student questionnaire |
| `EC153Q11HA` | Importance for decisions about future occupation: The expected salary of the occupation I want | Student questionnaire |
| `EC160Q01HA` | If you had the opportunity to participate in a student exchange programme [...], would you like to take part? | Student questionnaire |
| `EC158Q01HA` | On the most recent day you attended school, how long did you study in the morning before going to school? Hours | Student questionnaire |
| `EC158Q02HA` | On the most recent day you attended school, how long did you study in the morning before going to school? Minutes | Student questionnaire |
| `EC159Q01HA` | On the most recent day you attended school, how long did you study after leaving school? Hours | Student questionnaire |
| `EC159Q02HA` | On the most recent day you attended school, how long did you study after leaving school? Minutes | Student questionnaire |
| `EC163Q01HA` | Why did you study before or after school? I was interested in the content. | Student questionnaire |
| `EC163Q02HA` | Why did you study before or after school? We have a test coming up soon. | Student questionnaire |
| `EC163Q03HA` | Why did you study before or after school? My parents think studying is important. | Student questionnaire |
| `EC163Q04HA` | Why did you study before or after school? I had a homework assignment. | Student questionnaire |
| `EC163Q05HA` | Why did you study before or after school? All my classmates study before or after school. | Student questionnaire |
| `EC163Q06HA` | Why did you study before or after school? I always study. | Student questionnaire |
| `EC163Q07HA` | Why did you study before or after school? Other reason. | Student questionnaire |
| `EC162Q01HA` | Why didn't you study before or after school? I had no time to study. | Student questionnaire |
| `EC162Q02HA` | Why didn't you study before or after school? I was not interested in the content. | Student questionnaire |
| `EC162Q03HA` | Why didn't you study before or after school? There is no test coming up soon. | Student questionnaire |
| `EC162Q04HA` | Why didn't you study before or after school? Nobody told me I have to study. | Student questionnaire |
| `EC162Q05HA` | Why didn't you study before or after school? I had no homework assignment. | Student questionnaire |
| `EC162Q06HA` | Why didn't you study before or after school? None of my classmates study before or after school. | Student questionnaire |
| `EC162Q07HA` | Why didn't you study before or after school? I never study. | Student questionnaire |
| `EC162Q08HA` | Why didn't you study before or after school? Other reason. | Student questionnaire |
| `EC154Q01IA` | Do you currently attend additional instruction? [Enrichment lessons] in [Test language] | Student questionnaire |
| `EC154Q02IA` | Do you currently attend additional instruction? [Enrichment lessons] in mathematics | Student questionnaire |
| `EC154Q03IA` | Do you currently attend additional instruction? [Enrichment lessons] in [science] | Student questionnaire |
| `EC154Q04HA` | Do you currently attend additional instruction? [Enrichment lessons] in foreign language | Student questionnaire |
| `EC154Q05IA` | Do you currently attend additional instruction? [Remedial lessons] in [Test language] | Student questionnaire |
| `EC154Q06IA` | Do you currently attend additional instruction? [Remedial lessons] in mathematics | Student questionnaire |
| `EC154Q07IA` | Do you currently attend additional instruction? [Remedial lessons] in [science] | Student questionnaire |
| `EC154Q08HA` | Do you currently attend additional instruction? [Remedial lessons] in foreign language | Student questionnaire |
| `EC154Q09IA` | Do you currently attend additional instruction? Lessons to improve your [study skills] | Student questionnaire |
| `EC012Q01NA` | Why do you attend additional instruction in <test language> this school year? I want to learn more. | Student questionnaire |
| `EC012Q02NA` | Why do you attend additional instruction in <test language> this school year? I want to prepare for exams. | Student questionnaire |
| `EC012Q04NA` | Why do you attend additional instruction in <test language> this school year? My parents wanted me to attend. | Student questionnaire |
| `EC012Q06NA` | Why do you attend additional instruction in <test language> this school year? My teachers recommend it. | Student questionnaire |
| `EC012Q07NA` | Why do you attend additional instruction in <test language> this school year? I want to improve my grades. | Student questionnaire |
| `EC012Q08NA` | Why do you attend additional instruction in <test language> this school year? I need to improve my grades. | Student questionnaire |
| `EC012Q13HA` | Why do you attend additional instruction in [Test language] this school year? It was helpful for me in the past. | Student questionnaire |
| `EC012Q12NA` | Why do you attend additional instruction in <test language> this school year? Other reason. | Student questionnaire |
| `EC155Q01DA` | How often do the following people work with you on your schoolwork? Your mother | Student questionnaire |
| `EC155Q02DA` | How often do the following people work with you on your schoolwork? Your father | Student questionnaire |
| `EC155Q03DA` | How often do the following people work with you on your schoolwork? Your brothers and sisters | Student questionnaire |
| `EC155Q04HA` | How often do the following people work with you on your schoolwork? Other relatives | Student questionnaire |
| `EC155Q05HA` | How often do the following people work with you on your schoolwork? Other person | Student questionnaire |

## Well-being items

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `WB150Q01HA` | How is your health? | Student questionnaire |
| `WB151Q01HA` | How much do you weigh? (kilograms) | Student questionnaire |
| `WB152Q01HA` | How tall are you? (centimeters) | Student questionnaire |
| `WB153Q01HA` | Agree: I like my look just the way it is. | Student questionnaire |
| `WB153Q02HA` | Agree: I consider myself to be attractive. | Student questionnaire |
| `WB153Q03HA` | Agree: I am not concerned about my weight. | Student questionnaire |
| `WB153Q04HA` | Agree: I like my body. | Student questionnaire |
| `WB153Q05HA` | Agree: I like the way my clothes fit me. | Student questionnaire |
| `WB154Q01HA` | In the past six months, how often have you had the following? Headache | Student questionnaire |
| `WB154Q02HA` | In the past six months, how often have you had the following? Stomach pain | Student questionnaire |
| `WB154Q03HA` | In the past six months, how often have you had the following? Back pain | Student questionnaire |
| `WB154Q04HA` | In the past six months, how often have you had the following? Feeling depressed | Student questionnaire |
| `WB154Q05HA` | In the past six months, how often have you had the following? Irritability or bad temper | Student questionnaire |
| `WB154Q06HA` | In the past six months, how often have you had the following? Feeling nervous | Student questionnaire |
| `WB154Q07HA` | In the past six months, how often have you had the following? Difficulties in getting to sleep | Student questionnaire |
| `WB154Q08HA` | In the past six months, how often have you had the following? Feeling dizzy | Student questionnaire |
| `WB154Q09HA` | In the past six months, how often have you had the following? Feeling anxious | Student questionnaire |
| `WB155Q01HA` | How satisfied are you with each of the following? Your health | Student questionnaire |
| `WB155Q02HA` | How satisfied are you with each of the following? The way that you look | Student questionnaire |
| `WB155Q03HA` | How satisfied are you with each of the following? What you learn at school | Student questionnaire |
| `WB155Q04HA` | How satisfied are you with each of the following? The friends you have | Student questionnaire |
| `WB155Q05HA` | How satisfied are you with each of the following? The neighbourhood you live in | Student questionnaire |
| `WB155Q06HA` | How satisfied are you with each of the following? All the things you have | Student questionnaire |
| `WB155Q07HA` | How satisfied are you with each of the following? How you use your time | Student questionnaire |
| `WB155Q08HA` | How satisfied are you with each of the following? Your relationship with your parents/guardians | Student questionnaire |
| `WB155Q09HA` | How satisfied are you with each of the following? Your relationship with your teachers | Student questionnaire |
| `WB155Q10HA` | How satisfied are you with each of the following? Your life at school | Student questionnaire |
| `WB156Q01HA` | At present, how many close friends do you have? | Student questionnaire |
| `WB158Q01HA` | How many days a week do you usually spend time with your friends right after school? | Student questionnaire |
| `WB160Q01HA` | How often do you talk to your friends on the phone, send them text messages or have contact through social media? | Student questionnaire |
| `WB161Q01HA` | Are your friends well accepted by your parents or guardians? | Student questionnaire |
| `WB162Q01HA` | How easy is it for you to talk to the following people about things that really bother you? Your father | Student questionnaire |
| `WB162Q02HA` | How easy is it for you to talk to the following people about things that really bother you? Your mother's partner | Student questionnaire |
| `WB162Q03HA` | How easy is it for you to talk to the following people about things that really bother you? Your mother | Student questionnaire |
| `WB162Q04HA` | How easy is it for you to talk to the following people about things that really bother you? Your father's partner | Student questionnaire |
| `WB162Q05HA` | How easy is it for you to talk to the following people about things that really bother you? Your brother(s) | Student questionnaire |
| `WB162Q06HA` | How easy is it for you to talk to the following people about things that really bother you? Your sister(s) | Student questionnaire |
| `WB162Q07HA` | How easy is it for you to talk to the following people about things that really bother you? Your close friend(s) | Student questionnaire |
| `WB162Q08HA` | How easy is it for you to talk to the following people about things that really bother you? Your teachers | Student questionnaire |
| `WB162Q09HA` | How easy is it for you to talk to the following people about things that really bother you? Other family members | Student questionnaire |
| `WB163Q01HA` | Thinking about your parents or guardians, how often do they: Help me as much as I need | Student questionnaire |
| `WB163Q02HA` | Thinking about your parents or guardians, how often do they: Let me do the things I like doing | Student questionnaire |
| `WB163Q03HA` | Thinking about your parents or guardians, how often do they: Show that they care | Student questionnaire |
| `WB163Q04HA` | Thinking about your parents or guardians, how often do they: Try to understand my problems and worries | Student questionnaire |
| `WB163Q05HA` | Thinking about your parents or guardians, how often do they: Encourage me to make my own decisions | Student questionnaire |
| `WB163Q06HA` | Thinking about your parents or guardians, how often do they: Try to control everything I do | Student questionnaire |
| `WB163Q07HA` | Thinking about your parents or guardians, how often do they: Treat me like a baby | Student questionnaire |
| `WB163Q08HA` | Thinking about your parents or guardians, how often do they: Make me feel better when I am upset | Student questionnaire |
| `WB164Q01HA` | How often do you worry about how much money your family has? | Student questionnaire |
| `WB165Q01HA` | When was the last time you attended a mathematics class at school? | Student questionnaire |
| `WB166Q01HA` | How did you feel the last time you attended a mathematics class at school? Bored | Student questionnaire |
| `WB166Q02HA` | How did you feel the last time you attended a mathematics class at school? Challenged | Student questionnaire |
| `WB166Q03HA` | How did you feel the last time you attended a mathematics class at school? Nervous or tense | Student questionnaire |
| `WB166Q04HA` | How did you feel the last time you attended a mathematics class at school? Motivated or inspired | Student questionnaire |
| `WB167Q01HA` | When was the last time you attended a [test language lesson] at school? | Student questionnaire |
| `WB168Q01HA` | How did you feel the last time you attended a [test language lesson] at school? Bored | Student questionnaire |
| `WB168Q02HA` | How did you feel the last time you attended a [test language lesson] at school? Challenged | Student questionnaire |
| `WB168Q03HA` | How did you feel the last time you attended a [test language lesson] at school? Nervous or tense | Student questionnaire |
| `WB168Q04HA` | How did you feel the last time you attended a [test language lesson] at school? Motivated or inspired | Student questionnaire |
| `WB171Q01HA` | Now think of the last time you had a break between classes at school. How did you feel? Happy | Student questionnaire |
| `WB171Q02HA` | Now think of the last time you had a break between classes at school. How did you feel? Lonely | Student questionnaire |
| `WB171Q03HA` | Now think of the last time you had a break between classes at school. How did you feel? Nervous or tense | Student questionnaire |
| `WB171Q04HA` | Now think of the last time you had a break between classes at school. How did you feel? Full of energy | Student questionnaire |
| `WB172Q01HA` | When was the last time you spent time outside your home with your friends? | Student questionnaire |
| `WB173Q01HA` | How did you feel the last time you spent time outside your home with your friends? Bored | Student questionnaire |
| `WB173Q02HA` | How did you feel the last time you spent time outside your home with your friends? Happy | Student questionnaire |
| `WB173Q03HA` | How did you feel the last time you spent time outside your home with your friends? Nervous or tense | Student questionnaire |
| `WB173Q04HA` | How did you feel the last time you spent time outside your home with your friends? Full of energy | Student questionnaire |
| `WB176Q01HA` | When was the very last time you did your homework/studied for school? | Student questionnaire |
| `WB177Q01HA` | How did you feel the last time you did your homework/studied for school? Bored | Student questionnaire |
| `WB177Q02HA` | How did you feel the last time you did your homework/studied for school? Challenged | Student questionnaire |
| `WB177Q03HA` | How did you feel the last time you did your homework/studied for school? Nervous or tense | Student questionnaire |
| `WB177Q04HA` | How did you feel the last time you did your homework/studied for school? Motivated or inspired | Student questionnaire |
| `WB032Q01NA` | Outside of school, during the past 7 days, on how many days did you engage in: Moderate physical activities [...] | Student questionnaire |
| `WB032Q02NA` | Outside of school, during the past 7 days, on how many days did you engage in: Vigorous physical activities [...] | Student questionnaire |
| `WB031Q01NA` | This school year, on average, on how many days do you attend physical education classes each week? | Student questionnaire |
| `WB178Q01HA` | The following questions refer to your day yesterday: Overall, did you feel that you accomplished something yesterday? | Student questionnaire |
| `WB178Q02HA` | The following questions refer to your day yesterday: Were you treated with respect all day yesterday? | Student questionnaire |
| `WB178Q03HA` | The following questions refer to your day yesterday: Did you smile or laugh a lot yesterday? | Student questionnaire |
| `WB178Q04HA` | The following questions refer to your day yesterday: Did you learn or do something interesting yesterday? | Student questionnaire |
| `WB178Q05HA` | The following questions refer to your day yesterday: Did you have enough energy to get things done yesterday? | Student questionnaire |
| `WB178Q06HA` | The following questions refer to your day yesterday: Overall, are you satisfied with how you spent your time yesterday? | Student questionnaire |
| `WB178Q07HA` | The following questions refer to your day yesterday: Was yesterday a typical day? | Student questionnaire |

## Well-being & motivation

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `STUBMI` | Body mass index of student | Student questionnaire |

## Derived index (WLE)

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `HOMEPOS` | Home possessions (WLE) | Student questionnaire |
| `CULTPOSS` | Cultural possessions at home (WLE) | Student questionnaire |
| `HEDRES` | Home educational resources (WLE) | Student questionnaire |
| `WEALTH` | Family wealth (WLE) | Student questionnaire |
| `DISCLIMA` | Disciplinary climate in test language lessons (WLE) | Student questionnaire |
| `TEACHSUP` | Teacher support in test language lessons (WLE) | Student questionnaire |
| `DIRINS` | Teacher-directed instruction (WLE) | Student questionnaire |
| `PERFEED` | Perceived feedback (WLE) | Student questionnaire |
| `EMOSUPS` | Parents' emotional support perceived by student (WLE) | Student questionnaire |
| `STIMREAD` | Teacher's stimulation of reading engagement perceived by student (WLE) | Student questionnaire |
| `ADAPTIVITY` | Adaptation of instruction (WLE) | Student questionnaire |
| `TEACHINT` | Perceived teacher's interest (WLE) | Student questionnaire |
| `JOYREAD` | Joy/Like reading (WLE) | Student questionnaire |
| `SCREADCOMP` | Self-concept of reading: Perception of competence (WLE) | Student questionnaire |
| `SCREADDIFF` | Self-concept of reading: Perception of difficulty (WLE) | Student questionnaire |
| `PISADIFF` | Perception of difficulty of the PISA test (WLE) | Student questionnaire |
| `PERCOMP` | Perception of competitiveness at school (WLE) | Student questionnaire |
| `PERCOOP` | Perception of cooperation at school (WLE) | Student questionnaire |
| `ATTLNACT` | Attitude towards school: learning activities (WLE) | Student questionnaire |
| `COMPETE` | Competitiveness (WLE) | Student questionnaire |
| `WORKMAST` | Work mastery (WLE) | Student questionnaire |
| `GFOFAIL` | General fear of failure (WLE) | Student questionnaire |
| `EUDMO` | Eudaemonia: meaning in life (WLE) | Student questionnaire |
| `SWBP` | Subjective well-being: Positive affect (WLE) | Student questionnaire |
| `RESILIENCE` | Resilience (WLE) | Student questionnaire |
| `MASTGOAL` | Mastery goal orientation (WLE) | Student questionnaire |
| `GCSELFEFF` | Self-efficacy regarding global issues (WLE) | Student questionnaire |
| `GCAWARE` | Student's awareness of global issues (WLE) | Student questionnaire |
| `ATTIMM` | Student's attitudes towards immigrants (WLE) | Student questionnaire |
| `INTCULT` | Student's interest in learning about other cultures (WLE) | Student questionnaire |
| `PERSPECT` | Perspective-taking (WLE) | Student questionnaire |
| `COGFLEX` | Cognitive flexibility/adaptability (WLE) | Student questionnaire |
| `RESPECT` | Respect for people from other cultures (WLE) | Student questionnaire |
| `AWACOM` | Awareness of intercultural communication (WLE) | Student questionnaire |
| `GLOBMIND` | Global-mindedness (WLE) | Student questionnaire |
| `DISCRIM` | Discriminating school climate (WLE) | Student questionnaire |
| `BELONG` | Subjective well-being: Sense of belonging to school (WLE) | Student questionnaire |
| `BEINGBULLIED` | Student's experience of being bullied (WLE) | Student questionnaire |
| `ENTUSE` | ICT use outside of school (leisure) (WLE) | Student questionnaire |
| `HOMESCH` | Use of ICT outside of school (for school work activities) (WLE) | Student questionnaire |
| `USESCH` | Use of ICT at school in general (WLE) | Student questionnaire |
| `INTICT` | Interest in ICT (WLE) | Student questionnaire |
| `COMPICT` | Perceived ICT competence (WLE) | Student questionnaire |
| `AUTICT` | Perceived autonomy related to ICT use (WLE) | Student questionnaire |
| `SOIAICT` | ICT as a topic in social interaction (WLE) | Student questionnaire |
| `INFOCAR` | Information about careers (WLE) | Student questionnaire |
| `INFOJOB1` | Information about the labour market provided by the school (WLE) | Student questionnaire |
| `INFOJOB2` | Information about the labour market provided outside of school (WLE) | Student questionnaire |
| `CURSUPP` | Current parental support for learning at home (WLE) | Student questionnaire |
| `EMOSUPP` | Parents' emotional support (WLE) | Student questionnaire |
| `PQSCHOOL` | Parents' perceived school quality (WLE) | Student questionnaire |
| `PRESUPP` | Previous parental support for learning at home (WLE) | Student questionnaire |
| `JOYREADP` | Parents enjoyment of reading (WLE) | Student questionnaire |
| `ATTIMMP` | Parents' attitudes towards immigrants (WLE) | Student questionnaire |
| `INTCULTP` | Parents' interest in learning about other cultures (WLE) | Student questionnaire |
| `GCAWAREP` | Parents' awareness of global issues (WLE) | Student questionnaire |
| `BODYIMA` | Body image (WLE) | Student questionnaire |
| `SOCONPA` | Social Connections: Parents (WLE) | Student questionnaire |
| `EDUSHORT` | Shortage of educational material (WLE) | School questionnaire |
| `STAFFSHORT` | Shortage of educational staff (WLE) | School questionnaire |
| `STUBEHA` | Student behaviour hindering learning (WLE) | School questionnaire |
| `TEACHBEHA` | Teacher behaviour hindering learning (WLE) | School questionnaire |
| `SCMCEG` | School principal's view on teachers' multicultural and egalitarian beliefs (WLE) | School questionnaire |
| `TCSTAFFSHORT` | Teacher's view on staff shortage (WLE) | Teacher questionnaire |
| `TCEDUSHORT` | Teacher's view on educational material shortage (WLE) | Teacher questionnaire |
| `COLT` | Test language teacher collaboration (WLE) | Teacher questionnaire |
| `EXCHT` | Exchange and co-ordination for teaching (WLE) | Teacher questionnaire |
| `SATJOB` | Teacher's satisfaction with the current job environment (WLE) | Teacher questionnaire |
| `SATTEACH` | Teacher's satisfaction with teaching profession (WLE) | Teacher questionnaire |
| `SEFFCM` | Teacher's self-efficacy in classroom management (WLE) | Teacher questionnaire |
| `SEFFREL` | Teacher's self-efficacy in maintaining positive relations with students (WLE) | Teacher questionnaire |
| `SEFFINS` | Teacher's self-efficacy in instructional settings (WLE) | Teacher questionnaire |
| `TCOTLCOMP` | Opportunity to learn (OTL) aspects of reading comprehension (WLE) | Teacher questionnaire |
| `TCSTIMREAD` | Teacher's stimulation of reading engagement (WLE) | Teacher questionnaire |
| `TCSTRATREAD` | Teacher's initiation of reading strategies (WLE) | Teacher questionnaire |
| `TCICTUSE` | Teacher's use of specific ICT applications (WLE) | Teacher questionnaire |
| `TCDISCLIMA` | Disciplinary climate in test language lessons (WLE) | Teacher questionnaire |
| `TCDIRINS` | Direct teacher's instruction (WLE) | Teacher questionnaire |
| `FEEDBACK` | Feedback provided by the teachers (WLE) | Teacher questionnaire |
| `ADAPTINSTR` | Student assessment/use (adaption of instruction) (WLE) | Teacher questionnaire |
| `FEEDBINSTR` | Feedback provided by the teachers (WLE) | Teacher questionnaire |
| `TCATTIMM` | Teacher's attitudes towards immigrants (WLE) | Teacher questionnaire |
| `GCTRAIN` | Teacher's training on global competence (WLE) | Teacher questionnaire |
| `TCMCEG` | Teachers' multicultural and egalitarian beliefs (WLE) | Teacher questionnaire |
| `GCSELF` | Teacher's self-efficacy in multicultural environments (WLE) | Teacher questionnaire |

## Derived index (sum/other)

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `FCFMLRTY` | Familiarity with concepts of finance (Sum) | Student questionnaire |
| `UNDREM` | Meta-cognition: understanding and remembering | Student questionnaire |
| `METASUM` | Meta-cognition: summarising | Student questionnaire |
| `METASPAM` | Meta-cognition: assess credibility | Student questionnaire |
| `CREACTIV` | Creative extra-curricular activities (Sum) | School questionnaire |

## Test-taking motivation

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `EFFORT1` | How much effort did you put into this test? | Student questionnaire |
| `EFFORT2` | How much effort would you have invested? | Student questionnaire |

## Learning time

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `MMINS` | Learning time (minutes per week) - <Mathematics> | Student questionnaire |
| `LMINS` | Learning time (minutes per week) - <test language> | Student questionnaire |
| `SMINS` | Learning time (minutes per week) - <science> | Student questionnaire |
| `TMINS` | Learning time (minutes per week) - in total | Student questionnaire |
| `STTMG1` | Overlap between initial education and teaching the modal grade - Reading, writing and literature | Teacher questionnaire |
| `STTMG2` | Overlap between initial education and teaching the modal grade - Mathematics | Teacher questionnaire |
| `STTMG3` | Overlap between initial education and teaching the modal grade - Science | Teacher questionnaire |
| `STTMG4` | Overlap between initial education and teaching the modal grade - Technology | Teacher questionnaire |
| `STTMG5` | Overlap between initial education and teaching the modal grade - Social Studies | Teacher questionnaire |
| `STTMG6` | Overlap between initial education and teaching the modal grade - Modern foreign languages | Teacher questionnaire |
| `STTMG7` | Overlap between initial education and teaching the modal grade - Ancient languages | Teacher questionnaire |
| `STTMG8` | Overlap between initial education and teaching the modal grade - Arts | Teacher questionnaire |
| `STTMG9` | Overlap between initial education and teaching the modal grade - Physical education | Teacher questionnaire |
| `STTMG10` | Overlap between initial education and teaching the modal grade - Religion and-or ethics | Teacher questionnaire |
| `STTMG11` | Overlap between initial education and teaching the modal grade - Practical and vocational skills | Teacher questionnaire |

## Financial literacy items

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `FL150Q01TA` | Learned how to manage your money in a course: At school, in a subject or course specifically about managing your money | Student questionnaire |
| `FL150Q02TA` | Learned how to manage your money in a course: At school as part of another subject or course | Student questionnaire |
| `FL150Q03TA` | Learned how to manage your money in a course: In an activity outside school | Student questionnaire |
| `FL151Q01HA` | Text books used in the last 12 months: Have you had a specific text book on money matters? | Student questionnaire |
| `FL151Q02HA` | Text books used in the last 12 months: Have you had a text book on some other subject that discusses money matters? | Student questionnaire |
| `FL164Q01HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Interest payment | Student questionnaire |
| `FL164Q02HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Compound interest | Student questionnaire |
| `FL164Q03HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Exchange rate | Student questionnaire |
| `FL164Q04HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Depreciation | Student questionnaire |
| `FL164Q05HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Shares/stocks | Student questionnaire |
| `FL164Q06HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Return on investment | Student questionnaire |
| `FL164Q07HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Dividend | Student questionnaire |
| `FL164Q08HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Diversification | Student questionnaire |
| `FL164Q09HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Debit card | Student questionnaire |
| `FL164Q10HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Bank loan | Student questionnaire |
| `FL164Q11HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Pension plan | Student questionnaire |
| `FL164Q12HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Budget | Student questionnaire |
| `FL164Q13HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Wage | Student questionnaire |
| `FL164Q14HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Entrepreneur | Student questionnaire |
| `FL164Q15HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Central bank | Student questionnaire |
| `FL164Q16HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Income tax | Student questionnaire |
| `FL164Q17HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Credit default swap | Student questionnaire |
| `FL164Q18HA` | School lessons in the last 12 months, have you heard of, or learnt about, the following term: Call option | Student questionnaire |
| `FL165Q01HA` | Encountered types of problems about money matters: During your mathematics class | Student questionnaire |
| `FL165Q02HA` | Encountered types of problems about money matters: During another class | Student questionnaire |
| `FL165Q03HA` | Encountered types of problems about money matters: During [...] school time from an outside visitor [...] | Student questionnaire |
| `FL165Q04HA` | Encountered types of problems about money matters: During extra-curricular activity outside of school time | Student questionnaire |
| `FL166Q01HA` | Encountered in a school lesson in the last 12 months: Describing the purpose and uses of money | Student questionnaire |
| `FL166Q02HA` | Encountered in a school lesson in the last 12 months: Exploring the difference between spending money on needs and wants | Student questionnaire |
| `FL166Q03HA` | Encountered in a school lesson in the last 12 months: Exploring ways of planning to pay an expense | Student questionnaire |
| `FL166Q05HA` | Encountered in a school lesson in the last 12 months: Discussing the rights of consumers when dealing with [...] | Student questionnaire |
| `FL166Q06HA` | Encountered in a school lesson in the last 12 months: Discussing the ways in which money invested in the stock [...] | Student questionnaire |
| `FL166Q07HA` | Encountered in a school lesson in the last 12 months: Analysing advertisements to understand how they encourage [...] | Student questionnaire |
| `FL153Q01HA` | Get information about money matters (spending, saving, banking, investment): Parents/guardians or other adult relations | Student questionnaire |
| `FL153Q02HA` | Get information about money matters (spending, saving, banking, investment): Friends | Student questionnaire |
| `FL153Q03HA` | Get information about money matters (spending, saving, banking, investment): Television or radio | Student questionnaire |
| `FL153Q04HA` | Get information about money matters (spending, saving, banking, investment): The Internet | Student questionnaire |
| `FL153Q05HA` | Get information about money matters (spending, saving, banking, investment): Magazines | Student questionnaire |
| `FL153Q06HA` | Get information about money matters (spending, saving, banking, investment): Teachers | Student questionnaire |
| `FL167Q01HA` | Discuss the following with your parents (or guardians or relatives): Your spending decisions | Student questionnaire |
| `FL167Q02HA` | Discuss the following with your parents (or guardians or relatives): Your savings decisions | Student questionnaire |
| `FL167Q03HA` | Discuss the following with your parents (or guardians or relatives): The family budget | Student questionnaire |
| `FL167Q04HA` | Discuss the following with your parents (or guardians or relatives): Money for things you want to buy | Student questionnaire |
| `FL167Q05HA` | Discuss the following with your parents (or guardians or relatives): News related to economics or finance | Student questionnaire |
| `FL156Q01TA` | Do you get money from any of these sources? An allowance or pocket money for regularly doing chores at home | Student questionnaire |
| `FL156Q02TA` | Do you get money from any of these sources? An allowance or pocket money, without having to do any chores | Student questionnaire |
| `FL156Q03TA` | Do you get money from any of these sources? Working outside school hours (e.g. a holiday job, part-time work) | Student questionnaire |
| `FL156Q04TA` | Do you get money from any of these sources? Working in a family business | Student questionnaire |
| `FL156Q05TA` | Do you get money from any of these sources? Occasional informal jobs (e.g. baby-sitting or gardening) | Student questionnaire |
| `FL156Q06TA` | Do you get money from any of these sources? Gifts from friends or relatives | Student questionnaire |
| `FL156Q07HA` | Do you get money from any of these sources? Selling things (e.g. at local markets or on [eBay]) | Student questionnaire |
| `FL159Q01HA` | Agree: I can decide independently what to spend my money on. | Student questionnaire |
| `FL159Q02HA` | Agree: I can spend small amounts of my money independently, but for larger amounts I need to ask my parents or [...] | Student questionnaire |
| `FL159Q03HA` | Agree: I need to ask my parents or guardians for permission before I spend any money on my own. | Student questionnaire |
| `FL159Q04HA` | Agree: I am responsible for my own money matters (e.g. for preventing theft). | Student questionnaire |
| `FL160Q01HA` | Think about buying a new product from your allowance: Compare prices in different shops | Student questionnaire |
| `FL160Q02HA` | Think about buying a new product from your allowance: Compare prices between a shop and an online shop | Student questionnaire |
| `FL160Q03HA` | Think about buying a new product from your allowance: Buy the product without comparing prices | Student questionnaire |
| `FL160Q04HA` | Think about buying a new product from your allowance: Wait until the product gets cheaper before buying it | Student questionnaire |
| `FL161Q01HA` | Do you have any of the following things? An account with a [bank, building society, post office or credit union] | Student questionnaire |
| `FL161Q02HA` | Do you have any of the following things? A payment card/debit card | Student questionnaire |
| `FL161Q03HA` | Do you have any of the following things? A mobile app to access your account | Student questionnaire |
| `FL162Q01HA` | Confidence about doing the following: Making a money transfer (e.g. paying a bill) | Student questionnaire |
| `FL162Q02HA` | Confidence about doing the following: Filling in forms at the bank | Student questionnaire |
| `FL162Q03HA` | Confidence about doing the following: Understanding bank statements | Student questionnaire |
| `FL162Q04HA` | Confidence about doing the following: Understanding a sales contract | Student questionnaire |
| `FL162Q05HA` | Confidence about doing the following: Keeping track of my account balance | Student questionnaire |
| `FL162Q06HA` | Confidence about doing the following: Planning my spending with consideration of my current financial situation | Student questionnaire |
| `FL163Q01HA` | Confidence using digital or electronic devices outside of bank: Transferring money | Student questionnaire |
| `FL163Q02HA` | Confidence using digital or electronic devices outside of bank: Keeping track of my balance | Student questionnaire |
| `FL163Q03HA` | Confidence using digital or electronic devices outside of bank: Paying with a debit card instead of using cash | Student questionnaire |
| `FL163Q04HA` | Confidence using digital or electronic devices outside of bank: Paying with a mobile device [...] instead of using cash | Student questionnaire |
| `FL163Q05HA` | Confidence using digital or electronic devices outside of bank: Ensuring the safety of sensitive information when [...] | Student questionnaire |
| `FL168Q01HA` | In the last 12 months: Checked that you were given the right change when you bought something | Student questionnaire |
| `FL168Q02HA` | In the last 12 months: Talked to someone about the job you would like to do when you finish your education | Student questionnaire |
| `FL168Q03HA` | In the last 12 months: Complained that you did not have enough money for something you wanted to buy | Student questionnaire |
| `FL168Q04HA` | In the last 12 months: Bought something online (alone or with a family member) | Student questionnaire |
| `FL168Q05HA` | In the last 12 months: Undertook voluntary work | Student questionnaire |
| `FL168Q06HA` | In the last 12 months: Made a payment using a mobile phone | Student questionnaire |
| `FL168Q07HA` | In the last 12 months: Bought something that cost more money than you intended to spend | Student questionnaire |
| `FL168Q08HA` | In the last 12 months: Checked how much money you have | Student questionnaire |
| `FL169Q01HA` | Agree: I enjoy talking about money matters. | Student questionnaire |
| `FL169Q02HA` | Agree: Young people should make their own decisions about how to spend their money. | Student questionnaire |
| `FL169Q03HA` | Agree: Money matters are not relevant for me right now. | Student questionnaire |
| `FL169Q04HA` | Agree: I would like to run my own business in the future. | Student questionnaire |
| `FLCONFIN` | Confidence about financial matters (WLE) | Student questionnaire |
| `FLCONICT` | Confidence about financial matters using digital devices (WLE) | Student questionnaire |
| `FLSCHOOL` | Financial education in school lessons (WLE) | Student questionnaire |
| `FLFAMILY` | Parental involvement in matters of Financial Literacy (WLE) | Student questionnaire |

## School structure & resources

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `PROGN` | Unique national study programme code | Student questionnaire |
| `PRIVATESCH` | School type derived from sampling information; values = public, private, missing | School questionnaire |
| `SCHLTYPE` | School Ownership | School questionnaire |
| `STRATIO` | Student-Teacher ratio | School questionnaire |
| `SCHSIZE` | School Size (Sum) | School questionnaire |
| `RATCMP1` | Number of available computers per student at modal grade | School questionnaire |
| `RATCMP2` | Proportion of available computers that are connected to the Internet | School questionnaire |
| `TOTAT` | Total number of all teachers at school | School questionnaire |
| `PROATCE` | Index proportion of all teachers fully certified | School questionnaire |
| `PROAT5AB` | Index proportion of all teachers ISCED LEVEL 5A Bachelor | School questionnaire |
| `PROAT5AM` | Index proportion of all teachers ISCED LEVEL 5A Master | School questionnaire |
| `PROAT6` | Index proportion of all teachers ISCED LEVEL 6 | School questionnaire |
| `CLSIZE` | Class Size | School questionnaire |
| `OTT1` | Originally trained teacher (strict definition): standard teacher training | Teacher questionnaire |
| `OTT2` | Originally trained teacher (wide definition): standard, in-service, or work-based teacher training | Teacher questionnaire |
| `NTEACH1` | Subject included in initial training: Reading, writing and literature | Teacher questionnaire |
| `NTEACH2` | Subject included in initial training: Mathematics | Teacher questionnaire |
| `NTEACH3` | Subject included in initial training: Science | Teacher questionnaire |
| `NTEACH4` | Subject included in initial training: Technology | Teacher questionnaire |
| `NTEACH5` | Subject included in initial training: Social studies | Teacher questionnaire |
| `NTEACH6` | Subject included in initial training: Modern foreign languages | Teacher questionnaire |
| `NTEACH7` | Subject included in initial training: Ancient languages (e.g. Latin) | Teacher questionnaire |
| `NTEACH8` | Subject included in initial training: Arts | Teacher questionnaire |
| `NTEACH9` | Subject included in initial training: Physical education | Teacher questionnaire |
| `NTEACH10` | Subject included in initial training: Religion and\or ethics | Teacher questionnaire |
| `NTEACH11` | Subject included in initial training: Practical and vocational skills | Teacher questionnaire |

## Teacher questionnaire items

| Variable | Label | Questionnaire |
|----------|-------|---------------|
| `TC001Q01NA` | Are you female or male? | Teacher questionnaire |
| `TC002Q01NA` | How old are you? | Teacher questionnaire |
| `TC005Q01NA` | What is your current employment status as a teacher? My employment status at this school | Teacher questionnaire |
| `TC007Q01NA` | How many years of work experience do you have? Year(s) working as a teacher at this school | Teacher questionnaire |
| `TC007Q02NA` | How many years of work experience do you have? Year(s) working as a teacher in total | Teacher questionnaire |
| `TC014Q01HA` | Did you complete a teacher education or training programme? | Teacher questionnaire |
| `TC015Q01NA` | How did you receive your initial teaching qualifications? | Teacher questionnaire |
| `TC018Q01NA` | Included in teacher education, training or other qualification: Reading, writing and literature | Teacher questionnaire |
| `TC018Q01NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Reading, writing and literature | Teacher questionnaire |
| `TC018Q02NA` | Included in teacher education, training or other qualification: Mathematics | Teacher questionnaire |
| `TC018Q02NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Mathematics | Teacher questionnaire |
| `TC018Q03NA` | Included in teacher education, training or other qualification: Science | Teacher questionnaire |
| `TC018Q03NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Science | Teacher questionnaire |
| `TC018Q04NA` | Included in teacher education, training or other qualification: Technology | Teacher questionnaire |
| `TC018Q04NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Technology | Teacher questionnaire |
| `TC018Q05NA` | Included in teacher education, training or other qualification: Social studies | Teacher questionnaire |
| `TC018Q05NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Social studies | Teacher questionnaire |
| `TC018Q06NA` | Included in teacher education, training or other qualification: Modern foreign languages | Teacher questionnaire |
| `TC018Q06NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Modern foreign languages | Teacher questionnaire |
| `TC018Q07NA` | Included in teacher education, training or other qualification: Ancient languages (e.g. Latin) | Teacher questionnaire |
| `TC018Q07NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Ancient languages (e.g. Latin) | Teacher questionnaire |
| `TC018Q08NA` | Included in teacher education, training or other qualification: Arts | Teacher questionnaire |
| `TC018Q08NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Arts | Teacher questionnaire |
| `TC018Q09NA` | Included in teacher education, training or other qualification: Physical education | Teacher questionnaire |
| `TC018Q09NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Physical education | Teacher questionnaire |
| `TC018Q10NA` | Included in teacher education, training or other qualification: Religion and/or ethics | Teacher questionnaire |
| `TC018Q10NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Religion and/or ethics | Teacher questionnaire |
| `TC018Q11NA` | Included in teacher education, training or other qualification: Practical and vocational skills | Teacher questionnaire |
| `TC018Q11NB` | Teach it in the <national modal grade for 15-year-olds> in the current school year: Practical and vocational skills | Teacher questionnaire |
| `TC045Q01NA` | Included in teacher education, training or other qualification: Knowledge and understanding of my subject field(s) | Teacher questionnaire |
| `TC045Q01NB` | Included in professional development during last 12 months: Knowledge and understanding of my subject field(s) | Teacher questionnaire |
| `TC045Q02NA` | Included in teacher education, training or other qualification: Pedagogical competencies in teaching my subject field(s) | Teacher questionnaire |
| `TC045Q02NB` | Included in professional development during last 12 months: Pedagogical competencies in teaching my subject field(s) | Teacher questionnaire |
| `TC045Q03NA` | Included in teacher education, training or other qualification: Knowledge of the curriculum | Teacher questionnaire |
| `TC045Q03NB` | Included in professional development during last 12 months: Knowledge of the curriculum | Teacher questionnaire |
| `TC045Q04NA` | Included in teacher education, training or other qualification: Student assessment practices | Teacher questionnaire |
| `TC045Q04NB` | Included in professional development during last 12 months: Student assessment practices | Teacher questionnaire |
| `TC045Q05NA` | Included in teacher education, training or other qualification: ICT [...] skills for teaching | Teacher questionnaire |
| `TC045Q05NB` | Included in professional development during last 12 months: ICT [...] skills for teaching | Teacher questionnaire |
| `TC045Q06NA` | Included in teacher education, training or other qualification: Student behaviour and classroom management | Teacher questionnaire |
| `TC045Q06NB` | Included in professional development during last 12 months: Student behaviour and classroom management | Teacher questionnaire |
| `TC045Q07NA` | Included in teacher education, training or other qualification: School management and administration | Teacher questionnaire |
| `TC045Q07NB` | Included in professional development during last 12 months: School management and administration | Teacher questionnaire |
| `TC045Q08NA` | Included in teacher education, training or other qualification: Approaches to individualised learning | Teacher questionnaire |
| `TC045Q08NB` | Included in professional development during last 12 months: Approaches to individualised learning | Teacher questionnaire |
| `TC045Q09NA` | Included in teacher education, training or other qualification: Teaching students with special needs | Teacher questionnaire |
| `TC045Q09NB` | Included in professional development during last 12 months: Teaching students with special needs | Teacher questionnaire |
| `TC045Q10NA` | Included in teacher education, training or other qualification: Teaching in a multicultural or multilingual setting | Teacher questionnaire |
| `TC045Q10NB` | Included in professional development during last 12 months: Teaching in a multicultural or multilingual setting | Teacher questionnaire |
| `TC045Q11NA` | Included in teacher education, training or other qualification: Teaching cross-curricular skills [...] | Teacher questionnaire |
| `TC045Q11NB` | Included in professional development during last 12 months: Teaching cross-curricular skills [...] | Teacher questionnaire |
| `TC045Q12NA` | Included in teacher education, training or other qualification: Student career guidance and counselling | Teacher questionnaire |
| `TC045Q12NB` | Included in professional development during last 12 months: Student career guidance and counselling | Teacher questionnaire |
| `TC045Q13NA` | Included in teacher education, training or other qualification: Internal evaluation or self-evaluation of schools | Teacher questionnaire |
| `TC045Q13NB` | Included in professional development during last 12 months: Internal evaluation or self-evaluation of schools | Teacher questionnaire |
| `TC045Q14NA` | Included in teacher education, training or other qualification: Use of evaluation results | Teacher questionnaire |
| `TC045Q14NB` | Included in professional development during last 12 months: Use of evaluation results | Teacher questionnaire |
| `TC045Q15NA` | Included in teacher education, training or other qualification: Teacher-parent cooperation | Teacher questionnaire |
| `TC045Q15NB` | Included in professional development during last 12 months: Teacher-parent cooperation | Teacher questionnaire |
| `TC045Q16HA` | Included in teacher education, training or other qualification: Second language teaching | Teacher questionnaire |
| `TC045Q16HB` | Included in professional development during last 12 months: Second language teaching | Teacher questionnaire |
| `TC045Q17HA` | Included in teacher education, training or other qualification: Communicating with people from different cultures [...] | Teacher questionnaire |
| `TC045Q17HB` | Included in professional development during last 12 months: Communicating with people from different cultures [...] | Teacher questionnaire |
| `TC045Q18HA` | Included in teacher education, training or other qualification: Teaching about equity and diversity | Teacher questionnaire |
| `TC045Q18HB` | Included in professional development during last 12 months: Teaching about equity and diversity | Teacher questionnaire |
| `TC021Q01NA` | Are you required to take part in professional development activities? | Teacher questionnaire |
| `TC175Q01HA` | About how much time per week do you spend reading for your work [...] out of your classes? | Teacher questionnaire |
| `TC198Q01HA` | Agree: The advantages of being a teacher clearly outweigh the disadvantages. | Teacher questionnaire |
| `TC198Q02HA` | Agree: If I could decide again, I would still choose to work as a teacher. | Teacher questionnaire |
| `TC198Q03HA` | Agree: I would like to change to another school if that were possible. | Teacher questionnaire |
| `TC198Q04HA` | Agree: I regret that I decided to become a teacher. | Teacher questionnaire |
| `TC198Q05HA` | Agree: I enjoy working at this school. | Teacher questionnaire |
| `TC198Q06HA` | Agree: I wonder whether it would have been better to choose another profession. | Teacher questionnaire |
| `TC198Q07HA` | Agree: I would recommend my school as a good place to work. | Teacher questionnaire |
| `TC198Q08HA` | Agree: I think that the teaching profession is valued in society. | Teacher questionnaire |
| `TC198Q09HA` | Agree: I am satisfied with my performance in this school. | Teacher questionnaire |
| `TC198Q10HA` | Agree: All in all, I am satisfied with my job. | Teacher questionnaire |
| `TC152Q01HA` | Agree: Every teacher should be trained to teach reading comprehension. | Teacher questionnaire |
| `TC152Q02HA` | Agree: Every teacher has a responsibility to improve students' reading comprehension skills. | Teacher questionnaire |
| `TC152Q03HA` | Agree: I know how to diagnose the students' reading comprehension problems. | Teacher questionnaire |
| `TC152Q04HA` | Agree: I am very confident in my capability to teach reading comprehension strategies. | Teacher questionnaire |
| `TC155Q02HA` | In your lessons, how often do you teach: Summarizing strategies | Teacher questionnaire |
| `TC155Q03HA` | In your lessons, how often do you teach: Connecting texts with prior content knowledge | Teacher questionnaire |
| `TC155Q04HA` | In your lessons, how often do you teach: Monitoring comprehension | Teacher questionnaire |
| `TC155Q05HA` | In your lessons, how often do you teach: Adapting the mode of reading depending on reading purposes | Teacher questionnaire |
| `TC155Q06HA` | In your lessons, how often do you teach: Assessing credibility of information available on the Internet | Teacher questionnaire |
| `TC155Q07HA` | In your lessons, how often do you teach: Searching and selecting relevant information on the Internet | Teacher questionnaire |
| `TC166Q01HA` | In your lessons, have you ever taught: How to use keywords when using a search engine such as <Google>, <Yahoo>, etc. | Teacher questionnaire |
| `TC166Q02HA` | In your lessons, have you ever taught: How to decide whether to trust information from the Internet | Teacher questionnaire |
| `TC166Q03HA` | In your lessons, have you ever taught: How to compare different web pages and decide what information is more [...] | Teacher questionnaire |
| `TC166Q04HA` | In your lessons, have you ever taught: To understand the consequences of making information publicly available [...] | Teacher questionnaire |
| `TC166Q05HA` | In your lessons, have you ever taught: How to use the short description below the links in the list of results of [...] | Teacher questionnaire |
| `TC166Q06HA` | In your lessons, have you ever taught: How to detect whether the information is subjective or biased | Teacher questionnaire |
| `TC166Q07HA` | In your lessons, have you ever taught: How to detect phishing or spam emails | Teacher questionnaire |
| `TC164Q01HA` | <this academic year>, how many pages was the longest piece of text your [...] students had to read for your lessons | Teacher questionnaire |
| `TC207Q01HA` | In your lessons, opportunities to promote the following skills: Communicating with people from different cultures [...] | Teacher questionnaire |
| `TC207Q02HA` | In your lessons, opportunities to promote the following skills: Knowledge of different cultures | Teacher questionnaire |
| `TC207Q03HA` | In your lessons, opportunities to promote the following skills: Openness to people from other cultural backgrounds | Teacher questionnaire |
| `TC207Q04HA` | In your lessons, opportunities to promote the following skills: Respect for cultural diversity | Teacher questionnaire |
| `TC207Q05HA` | In your lessons, opportunities to promote the following skills: Foreign languages | Teacher questionnaire |
| `TC207Q06HA` | In your lessons, opportunities to promote the following skills: Critical thinking skills | Teacher questionnaire |
| `TC178Q01HA` | In your lessons, do you include: Climate change and global warming | Teacher questionnaire |
| `TC178Q02HA` | In your lessons, do you include: Global health (e.g. epidemics) | Teacher questionnaire |
| `TC178Q04HA` | In your lessons, do you include: Migration (movement of people) | Teacher questionnaire |
| `TC178Q07HA` | In your lessons, do you include: International conflicts | Teacher questionnaire |
| `TC178Q08HA` | In your lessons, do you include: Hunger or malnutrition in different parts of the world | Teacher questionnaire |
| `TC178Q09HA` | In your lessons, do you include: Causes of poverty | Teacher questionnaire |
| `TC178Q12HA` | In your lessons, do you include: Equality between men and women in different parts of the world | Teacher questionnaire |
| `TC184Q01HA` | Does your school have a policy concerning the use of digital devices for teaching? | Teacher questionnaire |
| `TC176Q01HA` | How often involved in: Reading emails | Teacher questionnaire |
| `TC176Q02HA` | How often involved in: <Chat on line> (e.g. <Whatsapp>, <Messenger>) | Teacher questionnaire |
| `TC176Q03HA` | How often involved in: Reading online news | Teacher questionnaire |
| `TC176Q05HA` | How often involved in: Searching information online to learn about a particular topic | Teacher questionnaire |
| `TC176Q06HA` | How often involved in: Taking part in online group discussions or forums | Teacher questionnaire |
| `TC176Q07HA` | How often involved in: Searching for practical information online (e.g. schedules, events, tips, recipes) | Teacher questionnaire |
| `TC172Q01HA` | Best describes how you read books | Teacher questionnaire |
| `TC173Q01HA` | Best describes how you read the news (e.g. politics, culture, sport, local news) | Teacher questionnaire |
| `TC186Q01HA` | Country of birth | Teacher questionnaire |
| `TC188Q01HA` | Studied in a country other than [country of test] | Teacher questionnaire |
| `TC206Q01HA` | Your education and training as a teacher: Have you received training on intercultural communication? | Teacher questionnaire |
| `TC206Q02HA` | Your education and training as a teacher: Have you received training on conflict resolution strategies? | Teacher questionnaire |
| `TC206Q03HA` | Your education and training as a teacher: Have you received training on the role education can play in confronting [...] | Teacher questionnaire |
| `TC206Q04HA` | Your education and training as a teacher: Have you studied culturally-responsive teaching approaches and techniques? | Teacher questionnaire |
| `TC206Q05HA` | Your education and training as a teacher: Have you received training on [...] teaching in multi-cultural classrooms? | Teacher questionnaire |
| `TC185Q01HA` | Current need for professional development: Knowledge and understanding of my subject field(s) | Teacher questionnaire |
| `TC185Q02HA` | Current need for professional development: Pedagogical competencies in teaching my subject field(s) | Teacher questionnaire |
| `TC185Q03HA` | Current need for professional development: Knowledge of the curriculum | Teacher questionnaire |
| `TC185Q04HA` | Current need for professional development: Student assessment practices | Teacher questionnaire |
| `TC185Q05HA` | Current need for professional development: ICT (information and communication technology) skills for teaching | Teacher questionnaire |
| `TC185Q06HA` | Current need for professional development: Student behaviour and classroom management | Teacher questionnaire |
| `TC185Q07HA` | Current need for professional development: School management and administration | Teacher questionnaire |
| `TC185Q08HA` | Current need for professional development: Approaches to individualised learning | Teacher questionnaire |
| `TC185Q09HA` | Current need for professional development: Teaching students with special needs | Teacher questionnaire |
| `TC185Q10HA` | Current need for professional development: Teaching in a multicultural or multilingual setting | Teacher questionnaire |
| `TC185Q11HA` | Current need for professional development: Teaching cross-curricular skills (e.g. problem solving, learning-to-learn) | Teacher questionnaire |
| `TC185Q12HA` | Current need for professional development: Student career guidance and counselling | Teacher questionnaire |
| `TC185Q13HA` | Current need for professional development: Internal evaluation or self-evaluation of schools | Teacher questionnaire |
| `TC185Q14HA` | Current need for professional development: Use of evaluation results | Teacher questionnaire |
| `TC185Q15HA` | Current need for professional development: Teacher-parent cooperation | Teacher questionnaire |
| `TC185Q16HA` | Current need for professional development: Second language teaching | Teacher questionnaire |
| `TC185Q17HA` | Current need for professional development: Communicating with people from different cultures or countries | Teacher questionnaire |
| `TC185Q18HA` | Current need for professional development: Teaching about equity and diversity | Teacher questionnaire |
| `TC193Q01HA` | During the last 12 months, participated in: Courses/workshops [...] | Teacher questionnaire |
| `TC193Q02HA` | During the last 12 months, participated in: Education conferences or seminars [...] | Teacher questionnaire |
| `TC193Q03HA` | During the last 12 months, participated in: Observation visits to other schools | Teacher questionnaire |
| `TC193Q04HA` | During the last 12 months, participated in: Observation visits to business premises, public organisations, [...] | Teacher questionnaire |
| `TC193Q05HA` | During the last 12 months, participated in: In-service training courses in business premises, public organisations [...] | Teacher questionnaire |
| `TC020Q01NA` | During the last 12 months, participated in: Qualification programme (e.g. a <degree programme>) | Teacher questionnaire |
| `TC020Q02NA` | During the last 12 months, participated in: Participation in a network of teachers formed specifically for the [...] | Teacher questionnaire |
| `TC020Q03NA` | During the last 12 months, participated in: Individual or collaborative research on a topic of interest to you [...] | Teacher questionnaire |
| `TC020Q04NA` | During the last 12 months, participated in: Mentoring and/or peer observation and coaching, as part of a formal [...] | Teacher questionnaire |
| `TC020Q05NA` | During the last 12 months, participated in: Reading professional literature (e.g. journals, evidence-based papers [...]) | Teacher questionnaire |
| `TC020Q06NA` | During the last 12 months, participated in: [...] informal dialogue with your colleagues on how to improve your teaching | Teacher questionnaire |
| `TC199Q01HA` | In your teaching, to what extent can you do: Get students to believe they can do well in school work | Teacher questionnaire |
| `TC199Q02HA` | In your teaching, to what extent can you do: Help my students value learning | Teacher questionnaire |
| `TC199Q03HA` | In your teaching, to what extent can you do: Craft good questions for my students | Teacher questionnaire |
| `TC199Q04HA` | In your teaching, to what extent can you do: Control disruptive behaviour in the classroom | Teacher questionnaire |
| `TC199Q05HA` | In your teaching, to what extent can you do: Motivate students who show low interest in school work | Teacher questionnaire |
| `TC199Q06HA` | In your teaching, to what extent can you do: Make my expectations about student behaviour clear | Teacher questionnaire |
| `TC199Q07HA` | In your teaching, to what extent can you do: Help students think critically | Teacher questionnaire |
| `TC199Q08HA` | In your teaching, to what extent can you do: Get students to follow classroom rules | Teacher questionnaire |
| `TC199Q09HA` | In your teaching, to what extent can you do: Calm a student who is disruptive or noisy | Teacher questionnaire |
| `TC199Q10HA` | In your teaching, to what extent can you do: Use a variety of assessment strategies | Teacher questionnaire |
| `TC199Q11HA` | In your teaching, to what extent can you do: Provide an alternative explanation for example when students are confused | Teacher questionnaire |
| `TC199Q12HA` | In your teaching, to what extent can you do: Implement alternative instructional strategies in my classroom | Teacher questionnaire |
| `TC046Q04NA` | How often: Exchange teaching materials with colleagues | Teacher questionnaire |
| `TC046Q05NA` | How often: Engage in discussions about the learning development of specific students | Teacher questionnaire |
| `TC046Q06NA` | How often: Work with other teachers [...] to ensure common standards in evaluations for assessing student progress | Teacher questionnaire |
| `TC046Q07NA` | How often: Attend team conferences | Teacher questionnaire |
| `TC028Q01NA` | School's instruction hindered by: A lack of teaching staff. | Teacher questionnaire |
| `TC028Q02NA` | School's instruction hindered by: Inadequate or poorly qualified teaching staff. | Teacher questionnaire |
| `TC028Q03NA` | School's instruction hindered by: A lack of assisting staff. | Teacher questionnaire |
| `TC028Q04NA` | School's instruction hindered by: Inadequate or poorly qualified assisting staff. | Teacher questionnaire |
| `TC028Q05NA` | School's instruction hindered by: A lack of educational material [...] | Teacher questionnaire |
| `TC028Q06NA` | School's instruction hindered by: Inadequate or poor quality educational material [...] | Teacher questionnaire |
| `TC028Q07NA` | School's instruction hindered by: A lack of physical infrastructure [...] | Teacher questionnaire |
| `TC028Q08NA` | School's instruction hindered by: Inadequate or poor quality physical infrastructure [...] | Teacher questionnaire |
| `TC169Q01HA` | This school year, how often used for teaching: Tutorial software or practice programmes | Teacher questionnaire |
| `TC169Q02HA` | This school year, how often used for teaching: Digital learning games | Teacher questionnaire |
| `TC169Q03HA` | This school year, how often used for teaching: Word-processors or presentation software [...] | Teacher questionnaire |
| `TC169Q04HA` | This school year, how often used for teaching: Spreadsheets (e.g. <Microsoft Excel>) | Teacher questionnaire |
| `TC169Q05HA` | This school year, how often used for teaching: Multimedia production tools [...] | Teacher questionnaire |
| `TC169Q06HA` | This school year, how often used for teaching: Concept mapping software (e.g. <Inspiration>, <Webspiration>) | Teacher questionnaire |
| `TC169Q07HA` | This school year, how often used for teaching: Data logging and monitoring tools | Teacher questionnaire |
| `TC169Q08HA` | This school year, how often used for teaching: Simulations and modelling software | Teacher questionnaire |
| `TC169Q09HA` | This school year, how often used for teaching: Social media (e.g. <Facebook>, <Twitter>) | Teacher questionnaire |
| `TC169Q10HA` | This school year, how often used for teaching: Communication software (e.g. email, blogs) | Teacher questionnaire |
| `TC169Q11HA` | This school year, how often used for teaching: Computer-based information resources [...] | Teacher questionnaire |
| `TC169Q12HA` | This school year, how often used for teaching: Interactive digital learning resources (e.g. learning objects) | Teacher questionnaire |
| `TC169Q13HA` | This school year, how often used for teaching: Graphing or drawing software | Teacher questionnaire |
| `TC169Q14HA` | This school year, how often used for teaching: E-portfolios | Teacher questionnaire |
| `TC054Q01NA` | Assessing student learning, how often: I develop and administer my own assessment. | Teacher questionnaire |
| `TC054Q02NA` | Assessing student learning, how often: I administer a <standardised test>. | Teacher questionnaire |
| `TC054Q03NA` | Assessing student learning, how often: I have individual students answer questions in front of the class. | Teacher questionnaire |
| `TC054Q04NA` | Assessing student learning, how often: Provide written feedback on student work in addition to a <mark [...]>. | Teacher questionnaire |
| `TC054Q05NA` | Assessing student learning, how often: I let students judge their own progress. | Teacher questionnaire |
| `TC054Q06NA` | Assessing student learning, how often: I observe students when working [...] and provide immediate feedback. | Teacher questionnaire |
| `TC054Q07NA` | Assessing student learning, how often: I collect data from classroom assignments or home work. | Teacher questionnaire |
| `TC192Q01HA` | How often in your lessons: I tell students how they are performing in my course. | Teacher questionnaire |
| `TC192Q02HA` | How often in your lessons: I give students feedback on their strengths in my course. | Teacher questionnaire |
| `TC192Q03HA` | How often in your lessons: I tell students in which areas they can still improve. | Teacher questionnaire |
| `TC192Q04HA` | How often in your lessons: I tell students how they can improve their performance. | Teacher questionnaire |
| `TC192Q05HA` | How often in your lessons: I advise students on how to reach their learning goals. | Teacher questionnaire |
| `TC209Q01HA` | Teach in multicultural environments: I can cope with the challenges of a multicultural classroom. | Teacher questionnaire |
| `TC209Q02HA` | Teach in multicultural environments: I can adapt my teaching to the cultural diversity of students. | Teacher questionnaire |
| `TC209Q05HA` | Teach in multicultural environments: I can take care that students with and without migrant background work together. | Teacher questionnaire |
| `TC209Q06HA` | Teach in multicultural environments: I can raise awareness for cultural differences amongst the students. | Teacher questionnaire |
| `TC209Q09HA` | Teach in multicultural environments: I can contribute to reducing ethnic stereotypes between the students. | Teacher questionnaire |
| `TC208Q02HA` | Opinion shared by teachers: It is important for students to learn that people from other cultures can have [...] | Teacher questionnaire |
| `TC208Q03HA` | Opinion shared by teachers: Respecting other cultures is something that students should learn as early as possible. | Teacher questionnaire |
| `TC208Q07HA` | Opinion shared by teachers: In the classroom, it is important that students of different origins recognize the [...] | Teacher questionnaire |
| `TC208Q08HA` | Opinion shared by teachers: When there are conflicts between students of different origins, they should be [...] | Teacher questionnaire |
| `TC196Q02HA` | Agree: Immigrant children should have the same opportunities for education that other children in the country have. | Teacher questionnaire |
| `TC196Q03HA` | Agree: Immigrants who live in a country for several years should have the opportunity to vote in elections. | Teacher questionnaire |
| `TC196Q04HA` | Agree: Immigrants should have the opportunity to continue their own customs and lifestyle. | Teacher questionnaire |
| `TC196Q05HA` | Agree: Immigrants should have all the same rights that everyone else in the country has. | Teacher questionnaire |
| `TC203Q01HA` | Proportion of your teacher education dedicated to: <Reading literacy> [...] | Teacher questionnaire |
| `TC203Q02HA` | Proportion of your teacher education dedicated to: Pedagogy of <reading literacy> [...] | Teacher questionnaire |
| `TC203Q03HA` | Proportion of your teacher education dedicated to: General pedagogical knowledge [...] | Teacher questionnaire |
| `TC150Q01HA` | In your formal education and/or training, did you study: <Test language> | Teacher questionnaire |
| `TC150Q02HA` | In your formal education and/or training, did you study: Pedagogy/teaching <test language> | Teacher questionnaire |
| `TC150Q03HA` | In your formal education and/or training, did you study: Educational psychology | Teacher questionnaire |
| `TC150Q04HA` | In your formal education and/or training, did you study: Remedial <test language> | Teacher questionnaire |
| `TC150Q05HA` | In your formal education and/or training, did you study: Theoretical models and processes of reading | Teacher questionnaire |
| `TC150Q06HA` | In your formal education and/or training, did you study: Special education | Teacher questionnaire |
| `TC150Q07HA` | In your formal education and/or training, did you study: Pedagogy/teaching <test language> as a second [...] language | Teacher questionnaire |
| `TC150Q08HA` | In your formal education and/or training, did you study: Assessment methods in reading comprehension | Teacher questionnaire |
| `TC204Q01HA` | During the last 12 months, proportion of professional development dedicated to: <Reading Literacy> [...] | Teacher questionnaire |
| `TC204Q02HA` | During the last 12 months, proportion of professional development dedicated to: Pedagogy of <reading literacy> [...] | Teacher questionnaire |
| `TC204Q03HA` | During the last 12 months, proportion of professional development dedicated to: General pedagogical knowledge [...] | Teacher questionnaire |
| `TC163Q01HA` | How important do you consider teaching the following skills in your lessons? Skills related to reading comprehension | Teacher questionnaire |
| `TC163Q02HA` | How important do you consider teaching the following skills in your lessons? Skills related to writing | Teacher questionnaire |
| `TC163Q03HA` | How important do you consider teaching the following skills in your lessons? Skills related to listening comprehension | Teacher questionnaire |
| `TC163Q04HA` | How important do you consider teaching the following skills in your lessons? Skills related to oral communication | Teacher questionnaire |
| `TC202Q01HA` | How often in your <test language lessons>: I tailor my teaching to meet the needs of my students. | Teacher questionnaire |
| `TC202Q02HA` | How often in your <test language lessons>: I provide individual help when a student has difficulties understanding [...] | Teacher questionnaire |
| `TC202Q03HA` | How often in your <test language lessons>: I change the structure of my lesson on a topic that most students [...] | Teacher questionnaire |
| `TC202Q04HA` | How often in your <test language lessons>: I provide individual support for advanced students. | Teacher questionnaire |
| `TC202Q05HA` | How often in your <test language lessons>: I tell students how they are performing in my course. | Teacher questionnaire |
| `TC202Q06HA` | How often in your <test language lessons>: I give students feedback on their strengths in my course. | Teacher questionnaire |
| `TC202Q07HA` | How often in your <test language lessons>: I tell students in which areas they can still improve. | Teacher questionnaire |
| `TC202Q08HA` | How often in your <test language lessons>: I tell students how they can improve their performance. | Teacher questionnaire |
| `TC202Q09HA` | How often in your <test language lessons>: I advise students on how to reach their learning goals. | Teacher questionnaire |
| `TC170Q01HA` | How often in your <test language lessons>: Many students don't listen to what I say. | Teacher questionnaire |
| `TC170Q02HA` | How often in your <test language lessons>: There is noise and disorder. | Teacher questionnaire |
| `TC170Q03HA` | How often in your <test language lessons>: I have to wait a long time for students to quiet down. | Teacher questionnaire |
| `TC170Q04HA` | How often in your <test language lessons>: Students cannot work well. | Teacher questionnaire |
| `TC170Q05HA` | How often in your <test language lessons>: Students don't start working for a long time after the lesson begins. | Teacher questionnaire |
| `TC171Q01HA` | How often in your <test language lessons>: I set clear goals for the students' learning. | Teacher questionnaire |
| `TC171Q02HA` | How often in your <test language lessons>: I ask questions to check whether students have understood what was taught. | Teacher questionnaire |
| `TC171Q03HA` | How often in your <test language lessons>: At the beginning [...], I present a short summary of the previous lesson. | Teacher questionnaire |
| `TC171Q04HA` | How often in your <test language lessons>: I tell students what they have to learn. | Teacher questionnaire |
| `TC156Q05IA` | In your <test language lessons>, how often: I encourage students to express their opinion about a text. | Teacher questionnaire |
| `TC156Q06IA` | In your <test language lessons>, how often: I help students relate the stories they read to their lives. | Teacher questionnaire |
| `TC156Q07IA` | In your <test language lessons>, how often: I show students how the information in texts builds on what they [...] | Teacher questionnaire |
| `TC156Q08IA` | In your <test language lessons>, how often: I pose questions that motivate students to participate actively. | Teacher questionnaire |
| `TC157Q02HA` | How often do you ask students to: Identify the main ideas of what they have read | Teacher questionnaire |
| `TC157Q03HA` | How often do you ask students to: Explain or support their understanding of what they have read | Teacher questionnaire |
| `TC157Q07HA` | How often do you ask students to: Draw inferences based on what they have read | Teacher questionnaire |
| `TC157Q08HA` | How often do you ask students to: Describe the style or structure of the text they have read | Teacher questionnaire |
| `TC157Q09HA` | How often do you ask students to: Determine the author's perspective or purpose | Teacher questionnaire |
| `TC167Q01HA` | Within the last month, have digital devices [...] been used in your teaching of <test language lessons>? | Teacher questionnaire |
| `TC168Q01HA` | During the last month, asked students to use digital devices for: Searching for subject-related information online | Teacher questionnaire |
| `TC168Q02HA` | During the last month, asked students to use digital devices for: Working on extended projects (e.g. over several weeks) | Teacher questionnaire |
| `TC168Q03HA` | During the last month, asked students to use digital devices for: Working on short assignments (e.g. within a week) | Teacher questionnaire |
| `TC168Q04HA` | During the last month, asked students to use digital devices for: Working at their individual pace | Teacher questionnaire |
| `TC168Q05HA` | During the last month, asked students to use digital devices for: Working on individualised material | Teacher questionnaire |
| `TC168Q06HA` | During the last month, asked students to use digital devices for: Planning [...] learning activities for themselves | Teacher questionnaire |
| `TC168Q07HA` | During the last month, asked students to use digital devices for: Submitting homework or classwork | Teacher questionnaire |
| `TC168Q08HA` | During the last month, asked students to use digital devices for: Practicing or drilling | Teacher questionnaire |
| `TC168Q09HA` | During the last month, asked students to use digital devices for: Coordinating schoolwork with other students | Teacher questionnaire |
| `TC168Q10HA` | During the last month, asked students to use digital devices for: Following up on missed lessons or material | Teacher questionnaire |
| `TC168Q11HA` | During the last month, asked students to use digital devices for: Reading texts electronically instead of paper versions | Teacher questionnaire |
| `TC168Q12HA` | During the last month, asked students to use digital devices for: Writing a text such as a blog or a wiki | Teacher questionnaire |
| `TC031Q04NA` | Teacher cooperation: We discuss the achievement requirements for <test language lessons> when setting tests. | Teacher questionnaire |
| `TC031Q11NA` | Teacher cooperation: We discuss the criteria we use to grade written tests. | Teacher questionnaire |
| `TC031Q13NA` | Teacher cooperation: We exchange tasks for lessons and homework that cover a range of different levels of difficulty. | Teacher questionnaire |
| `TC031Q14NA` | Teacher cooperation: I prepare [...] units with my fellow teachers of <test language lessons>. | Teacher questionnaire |
| `TC031Q15NA` | Teacher cooperation: We discuss ways to teach learning strategies and techniques to our students. | Teacher questionnaire |
| `TC031Q18NA` | Teacher cooperation: My fellow teachers of <test language lessons> benefit from my specific skills and interests. | Teacher questionnaire |
| `TC031Q20NA` | Teacher cooperation: We discuss ways to better identify students' individual strengths and weaknesses. | Teacher questionnaire |
| `TC039Q01NA` | Is there any formal curriculum for <test language lessons> in <national modal grade for 15-year-olds>? | Teacher questionnaire |
| `TC043Q01NA` | Are parents informed about the availability and content of the <test language lessons> curriculum [...]? | Teacher questionnaire |
| `TC182Q01HA` | Does your school have special programmes for: Students with special needs | Teacher questionnaire |
| `TC182Q02HA` | Does your school have special programmes for: Students whose <heritage language> is different from <test language> | Teacher questionnaire |
| `TC182Q03HA` | Does your school have special programmes for: Students who struggle with reading | Teacher questionnaire |
