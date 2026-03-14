# 2. Data Preprocessing

## Steps Performed

### 1. Data Loading
```python
df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
# Shape: (299, 13)
```

### 2. Missing Value Check
- Zero missing values across all columns ✅

### 3. Feature / Target Split
```python
X = df.drop("DEATH_EVENT", axis=1)   # (299, 12)
y = df["DEATH_EVENT"]                 # (299,)
```

### 4. Train / Test Split
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```
| Split | Samples |
|-------|---------|
| Training | 239 (80%) |
| Testing | 60 (20%) |

### 5. Feature Scaling
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)
```
> Scaler fitted on training data only — prevents data leakage into the test set.

### Output
| Set | Shape |
|-----|-------|
| X_train_scaled | (239, 12) |
| X_test_scaled | (60, 12) |
