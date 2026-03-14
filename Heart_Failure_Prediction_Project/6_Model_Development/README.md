# 6. Model Development

## Baseline: Gradient Boosting Classifier (GBM)
A GBM was trained with default hyperparameters to establish a performance benchmark.
```python
from sklearn.ensemble import GradientBoostingClassifier

gbm_baseline = GradientBoostingClassifier(random_state=42)
gbm_baseline.fit(X_train_fs, y_train_res)
```

## Baseline Performance
| Metric | Score |
|--------|-------|
| Accuracy | 0.75 |
| Precision | 0.625 |
| Recall | 0.526 |
| F1 Score | 0.571 |

## Why Gradient Boosting?
- Sequentially corrects errors from previous trees → high accuracy on tabular data
- Handles non-linear relationships and feature interactions naturally
- Highly tunable — ideal for PSO-based optimization
- Strong performance on small-to-medium medical datasets

## Why Not Other Models?
| Model | Reason Not Chosen |
|-------|------------------|
| Logistic Regression | Assumes linearity — too simple |
| SVM | Poor recall on imbalanced classes |
| Random Forest | GBM outperforms via boosting |
| Neural Network | Overkill for 299 samples |

> Baseline recall of 52.6% is insufficient for a medical classifier — optimized via PSO in Step 7.
