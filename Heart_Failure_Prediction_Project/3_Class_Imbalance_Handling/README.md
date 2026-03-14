# 3. Class Imbalance Handling

## Problem
Training on imbalanced data causes the model to favour the majority class (survived), resulting in poor recall for deaths — the most critical outcome in a clinical setting.

| Class | Before SMOTE |
|-------|-------------|
| Survived (0) | 162 |
| Died (1) | 77 |

## Solution: SMOTE
SMOTE (Synthetic Minority Oversampling Technique) creates synthetic samples for the minority class by interpolating between existing minority instances — without simply duplicating them.
```python
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train_scaled, y_train)
```

## Result
| Class | Before SMOTE | After SMOTE |
|-------|-------------|-------------|
| Survived (0) | 162 | 162 |
| Died (1) | 77 | 162 |
| Total | 239 | 324 |

> SMOTE applied only on the training set — test set remains untouched to ensure unbiased evaluation.
