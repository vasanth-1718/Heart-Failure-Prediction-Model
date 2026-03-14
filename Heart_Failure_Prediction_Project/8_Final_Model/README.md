# 8. Final Model

## PSO-Optimized Gradient Boosting Classifier
The best hyperparameters found by PSO were used to train the final production model on the full SMOTE-balanced training set.

## Training
```python
gbm_optimized = GradientBoostingClassifier(
    n_estimators      = best_params["n_estimators"],
    max_depth         = best_params["max_depth"],
    learning_rate     = best_params["learning_rate"],
    subsample         = best_params["subsample"],
    min_samples_split = best_params["min_samples_split"],
    random_state      = 42
)
gbm_optimized.fit(X_train_fs, y_train_res)
```

## Saved Artifacts
```python
import joblib
joblib.dump(scaler,        "scaler.pkl")
joblib.dump(selector,      "selector.pkl")
joblib.dump(gbm_optimized, "gbm_model.pkl")
```

| File | Contents |
|------|----------|
| scaler.pkl | Fitted StandardScaler (12 features) |
| selector.pkl | Fitted SelectKBest (k=7) |
| gbm_model.pkl | Trained PSO-optimized GBM |

> These three artifacts are loaded by app.py (Streamlit) for real-time patient risk prediction.
