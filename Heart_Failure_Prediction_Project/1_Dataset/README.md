# 1. Dataset

## Heart Failure Clinical Records Dataset

### Source
- **Repository:** UCI Machine Learning Repository
- **Study:** Ahmad et al., 2017 — Survival analysis of heart failure patients

### Overview
| Property | Value |
|----------|-------|
| Total Records | 299 patients |
| Features | 12 clinical + 1 target |
| Target | DEATH_EVENT (0 = Survived, 1 = Died) |
| Missing Values | None |

### Feature Description
| Feature | Type | Description |
|---------|------|-------------|
| age | Continuous | Patient age in years |
| anaemia | Binary | Low red blood cell count (0=No, 1=Yes) |
| creatinine_phosphokinase | Continuous | CPK enzyme level in blood (mcg/L) |
| diabetes | Binary | Diabetic patient (0=No, 1=Yes) |
| ejection_fraction | Continuous | % of blood pumped per heartbeat |
| high_blood_pressure | Binary | Hypertension (0=No, 1=Yes) |
| platelets | Continuous | Platelet count (kiloplatelets/mL) |
| serum_creatinine | Continuous | Creatinine level in blood (mg/dL) |
| serum_sodium | Continuous | Sodium level in blood (mEq/L) |
| sex | Binary | Gender (0=Female, 1=Male) |
| smoking | Binary | Smoker (0=No, 1=Yes) |
| time | Continuous | Follow-up period (days) |
| DEATH_EVENT | Binary | Target — died during follow-up |

### Class Distribution
| Class | Count | Percentage |
|-------|-------|------------|
| Survived (0) | 203 | 67.9% |
| Died (1) | 96 | 32.1% |

> Dataset is imbalanced — addressed using SMOTE in Step 3.
