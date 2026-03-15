# Heart Failure Prediction using PSO-Optimized Gradient Boosting

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.8.0-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-deployed-red)
![License](https://img.shields.io/badge/License-MIT-green)

A clinical decision-support system that predicts the risk of mortality in heart failure patients using a PSO-optimized Gradient Boosting Classifier — deployed as an interactive Streamlit web application.

---

## Problem Statement
Heart failure is a life-threatening condition where early identification of high-risk patients can enable timely intervention. This project tackles two core challenges in medical ML:
- **Class imbalance** — death events are underrepresented in clinical data
- **Hyperparameter tuning** — default models produce insufficient recall for clinical use

---

## Pipeline Overview
```
Raw Data (299 patients, 12 features)
        ↓
  Preprocessing — StandardScaler + 80/20 stratified split
        ↓
  SMOTE — Balanced training set (324 samples)
        ↓
  Feature Selection — 12 → 7 features (chi-squared)
        ↓
  PSO Optimization — AIW_PSO, 30 epochs, 20 particles
        ↓
  Final GBM Model
        ↓
  Streamlit Web App — real-time patient risk prediction
```

---

## Results
| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| GBM Baseline | 0.75 | 0.625 | 0.526 | 0.571 |
| GBM + PSO | — | — | — | — |

> Recall is the priority metric — minimizing false negatives (missed deaths) is critical in a clinical setting.

---

## Dataset
- **Source:** UCI Machine Learning Repository
- **Records:** 299 patients with heart failure
- **Features:** 12 clinical features + 1 target (`DEATH_EVENT`)
- **Class split:** 203 survived (67.9%) / 96 died (32.1%)

---

## Tech Stack
| Tool | Purpose |
|------|---------|
| Python 3.13 | Core language |
| Scikit-learn | ML models & preprocessing |
| Imbalanced-learn | SMOTE oversampling |
| Mealpy 3.0.3 | PSO hyperparameter optimization |
| Streamlit | Web app deployment |
| Joblib | Model serialization |
| Pandas / NumPy | Data manipulation |
| Matplotlib / Seaborn | Visualization |

---

## Project Structure
```
Heart_Failure_Prediction_Project/
├── 0_Project_Overview/
├── 1_Dataset/
├── 2_Data_Preprocessing/
├── 3_Class_Imbalance_Handling/
├── 4_Feature_Selection/
├── 5_Correlation_Analysis/
├── 6_Model_Development/
├── 7_Hyperparameter_Optimization/
├── 8_Final_Model/
├── 9_Model_Evaluation/
├── 10_Results_and_Analysis/
├── 11_Conclusion_and_Future_Work/
└── notebooks/
    └── heart_failure_pipeline.ipynb
app.py           ← Streamlit web application
scaler.pkl       ← Fitted StandardScaler
selector.pkl     ← Fitted SelectKBest (k=7)
gbm_model.pkl    ← Trained PSO-optimized GBM
run_app.sh       ← One-click app launcher
```

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/vasanth-1718/Heart-Failure-Prediction-Model.git
cd Heart-Failure-Prediction-Model
```

### 2. Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install matplotlib seaborn scikit-learn pandas imbalanced-learn scipy streamlit joblib
pip install --no-deps mealpy
```

### 4. Run the Streamlit app
```bash
cd mainpro
streamlit run app.py
```

---

## Features Used in Model
| Feature | Clinical Relevance |
|---------|-------------------|
| age | Older age increases mortality risk |
| creatinine_phosphokinase | CPK elevation signals cardiac muscle damage |
| ejection_fraction | Low EF indicates weak heart pumping |
| serum_creatinine | Elevated levels indicate kidney-heart dysfunction |
| serum_sodium | Low sodium linked to poor cardiac prognosis |
| sex | Gender-based cardiovascular risk differences |
| time | Longer follow-up generally indicates survival |

---

## Future Work
- [ ] Add SHAP explainability to the Streamlit app
- [ ] Deploy to Streamlit Cloud for public access
- [ ] Build REST API with FastAPI for EHR integration
- [ ] Validate on multi-institution datasets

---

## References
1. Ahmad, T., et al. (2017). Survival analysis of heart failure patients.
2. Chicco, D., Jurman, G. (2020). Machine learning for the prediction of survival of patients with heart failure.
3. UCI ML Repository — Heart Failure Clinical Records Dataset.

---

## Author
**Vasanth** — [GitHub](https://github.com/vasanth-1718)
