# 5. Correlation Analysis

## Purpose
Understand feature relationships with the target variable and detect multicollinearity among predictors.

## Correlation with DEATH_EVENT
| Feature | Correlation | Direction |
|---------|-------------|-----------|
| time | -0.53 | Longer follow-up → lower death risk |
| serum_creatinine | +0.29 | Higher creatinine → higher risk |
| ejection_fraction | -0.27 | Lower ejection → higher risk |
| age | +0.25 | Older → higher risk |
| serum_sodium | -0.20 | Lower sodium → higher risk |
| creatinine_phosphokinase | +0.06 | Weak positive |
| sex | -0.05 | Weak correlation |

## Key Findings
- `time` is the strongest predictor — closely tied to patient monitoring intensity
- `serum_creatinine` and `ejection_fraction` are the most clinically actionable biomarkers
- No significant multicollinearity detected between selected features

## Visualizations Produced
- Pearson correlation heatmap
- Feature distribution plots (survived vs died)
- Boxplots of top features against DEATH_EVENT
