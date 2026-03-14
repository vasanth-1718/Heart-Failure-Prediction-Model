# 11. Conclusion and Future Work

## Conclusion
This project built a complete, production-ready heart failure mortality prediction system. The pipeline demonstrates that combining SMOTE + feature selection + PSO-optimized GBM outperforms a naive baseline on imbalanced clinical data.

### What Was Achieved
- Handled class imbalance with SMOTE
- Reduced feature space from 12 → 7 using chi-squared selection
- Optimized GBM hyperparameters using Particle Swarm Optimization
- Deployed as an interactive Streamlit web application
- Serialized model artifacts for reproducible inference

## Limitations
| Limitation | Impact |
|-----------|--------|
| Small dataset (299 patients) | Limited generalizability |
| Single-institution data | May not transfer across hospitals |
| No temporal modeling | Patient trajectory not captured |
| No external validation | Clinical readiness unconfirmed |

## Future Work

### Short Term
- [ ] Add SHAP explainability — show which features drove each prediction
- [ ] Display confusion matrix and ROC curve inside the Streamlit app
- [ ] Compare PSO against Genetic Algorithm and Bayesian Optimization

### Medium Term
- [ ] Collect multi-institution data for better generalization
- [ ] Add cross-validation inside the PSO objective function
- [ ] Try XGBoost and LightGBM as alternative base models

### Long Term
- [ ] Deploy to Streamlit Cloud or AWS for public access
- [ ] Build a REST API with FastAPI for EHR system integration
- [ ] Incorporate longitudinal patient monitoring data (time-series)
- [ ] Conduct clinical validation with medical professionals

## References
1. Ahmad, T., et al. (2017). Survival analysis of heart failure patients — A case study.
2. Chicco, D., Jurman, G. (2020). Machine learning for the prediction of survival of patients with heart failure.
3. UCI ML Repository — Heart Failure Clinical Records Dataset.
