# 0. Project Overview

## Heart Failure Prediction using PSO-Optimized Gradient Boosting

### Objective
Build a clinical decision-support system that predicts the risk of death in heart failure patients using machine learning — with a focus on maximizing recall to reduce missed fatalities.

### Approach
| Step | Technique |
|------|-----------|
| Imbalance handling | SMOTE (Synthetic Minority Oversampling) |
| Feature selection | SelectKBest with Chi-squared scoring |
| Model | Gradient Boosting Classifier (GBM) |
| Optimization | Particle Swarm Optimization (PSO) via Mealpy |
| Deployment | Streamlit web application |

### Tech Stack
| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.13 | Core language |
| Scikit-learn | 1.8.0 | ML pipeline |
| Imbalanced-learn | latest | SMOTE |
| Mealpy | 3.0.3 | PSO optimization |
| Streamlit | latest | Web app |
| Joblib | latest | Model serialization |
