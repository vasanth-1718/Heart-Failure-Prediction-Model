# 9. Model Evaluation

## Test Set Evaluation
All evaluation was performed on the held-out test set (60 samples) — never seen during training or optimization.

## Metrics Explained
| Metric | Formula | Importance |
|--------|---------|------------|
| Accuracy | (TP+TN) / Total | Overall correctness |
| Precision | TP / (TP+FP) | Avoids false alarms |
| Recall | TP / (TP+FN) | Most critical — catch all deaths |
| F1 Score | 2×P×R / (P+R) | Balance of precision & recall |

> Recall is the priority metric. A false negative (predicting survival when the patient dies) is far more dangerous than a false positive in a clinical context.

## Performance Comparison
| Model | Accuracy | Precision | Recall | F1 |
|-------|----------|-----------|--------|----|
| GBM Baseline | 0.75 | 0.625 | 0.526 | 0.571 |
| GBM + PSO | — | — | — | — |

## Confusion Matrix
```
                  Predicted: Survived    Predicted: Died
Actual: Survived        TN                    FP
Actual: Died            FN  ← Danger          TP
```

## Evaluation Visualizations
- Confusion matrix heatmap
- ROC curve with AUC score
- Precision-Recall curve
- Feature importance bar chart
