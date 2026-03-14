import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest

# ---- LOAD SAVED OBJECTS (we reuse from notebook) ----
# Run this cell ONCE in notebook before UI:
# joblib.dump(scaler, "scaler.pkl")
# joblib.dump(selector, "selector.pkl")
# joblib.dump(gbm_optimized, "gbm_model.pkl")

# Attempt to load required artifacts; show a friendly message in Streamlit if missing
required_files = {"scaler": "scaler.pkl", "selector": "selector.pkl", "model": "gbm_model.pkl"}
missing = [p for p in required_files.values() if not os.path.exists(p)]
scaler = selector = model = None
if missing:
    st.title("Heart Failure Prediction")
    st.error(
        "Missing saved artifacts: {}.\nRun the notebook cell that trains the model and use `joblib.dump(...)` to save `scaler.pkl`, `selector.pkl`, and `gbm_model.pkl` into the project root.`".format(
            ", ".join(missing)
        )
    )
    st.stop()
else:
    scaler = joblib.load(required_files["scaler"])
    selector = joblib.load(required_files["selector"])
    model = joblib.load(required_files["model"])

st.title("Heart Failure Prediction")

# ---- INPUTS ----
age = st.number_input("Age", 1, 120, 60)
ejection_fraction = st.number_input("Ejection Fraction", 10, 80, 35)
serum_creatinine = st.number_input("Serum Creatinine", 0.1, 10.0, 1.4)
serum_sodium = st.number_input("Serum Sodium", 100, 150, 137)
time = st.number_input("Follow-up Time (days)", 1, 300, 120)

anaemia = st.selectbox("Anaemia", [0, 1])
diabetes = st.selectbox("Diabetes", [0, 1])
high_bp = st.selectbox("High Blood Pressure", [0, 1])
sex = st.selectbox("Sex (1=Male)", [0, 1])
smoking = st.selectbox("Smoking", [0, 1])

cpk = st.number_input("CPK", 0, 8000, 250)
platelets = st.number_input("Platelets", 10000, 1000000, 265000)

if st.button("Predict"):
    patient = pd.DataFrame([[
        age, anaemia, cpk, diabetes, ejection_fraction,
        high_bp, platelets, serum_creatinine,
        serum_sodium, sex, smoking, time
    ]])

    patient_scaled = scaler.transform(patient)
    patient_fs = selector.transform(np.abs(patient_scaled))
    pred = model.predict(patient_fs)[0]

    if pred == 1:
        st.error("High risk of death")
    else:
        st.success("Low risk (survived)")
