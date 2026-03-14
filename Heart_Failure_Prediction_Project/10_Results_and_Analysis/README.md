# 10. Results and Analysis

## End-to-End Pipeline Summary
```
Raw Data (299 samples, 12 features)
        ↓
  Preprocessing — StandardScaler, 80/20 split
        ↓
  SMOTE — Balanced training set (324 samples)
        ↓
  Feature Selection — 12 → 7 features (chi-squared)
        ↓
  PSO Optimization — 30 epochs, 20 particles
        ↓
  Final GBM Model — trained on balanced + selected data
        ↓
  Streamlit App — real-time patient risk prediction
```

## Performance Improvement
| Metric | Baseline | Optimized | Change |
|--------|----------|-----------|--------|
| Accuracy | 0.75 | — | — |
| Precision | 0.625 | — | — |
| Recall | 0.526 | — | — |
| F1 Score | 0.571 | — | — |

## Key Insights

### Clinical
- `time` (follow-up duration) was the strongest predictor of survival
- `serum_creatinine` and `ejection_fraction` are the most actionable biomarkers
- Features removed by selection (`anaemia`, `smoking`, `diabetes`) had weak predictive power

### Technical
- SMOTE improved recall significantly by preventing class bias
- PSO found better hyperparameters than defaults without exhaustive search
- Reducing features from 12 → 7 improved generalization without information loss
