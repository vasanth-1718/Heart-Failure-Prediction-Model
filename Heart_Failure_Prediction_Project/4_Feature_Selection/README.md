# 4. Feature Selection

## Method: SelectKBest (Chi-squared)
Selects the top K features based on chi-squared statistical scores between each feature and the target variable.
```python
from sklearn.feature_selection import SelectKBest, chi2

selector = SelectKBest(chi2, k=7)
X_train_fs = selector.fit_transform(np.abs(X_train_res), y_train_res)
X_test_fs  = selector.transform(np.abs(X_test_scaled))
```

## Selected Features (Top 7)
| Feature | Clinical Relevance |
|---------|-------------------|
| age | Older age increases mortality risk |
| creatinine_phosphokinase | CPK elevation signals cardiac muscle damage |
| ejection_fraction | Low EF indicates weak heart pumping |
| serum_creatinine | Elevated levels indicate kidney-heart dysfunction |
| serum_sodium | Low sodium linked to poor cardiac prognosis |
| sex | Gender-based cardiovascular risk differences |
| time | Longer follow-up generally indicates survival |

## Removed Features
`anaemia`, `diabetes`, `high_blood_pressure`, `platelets`, `smoking` — statistically lower chi-squared scores.

## Shape After Selection
| Set | Before | After |
|-----|--------|-------|
| X_train | (324, 12) | (324, 7) |
| X_test | (60, 12) | (60, 7) |
