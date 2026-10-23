from pathlib import Path
import pickle
import streamlit as st
from navigation import make_sidebar

make_sidebar()

if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.switch_page("login.py")
    st.stop()

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = BASE_DIR / "save_models"

# simple built-in navigation instead of streamlit_option_menu
selected = st.radio(
    "Choose a disease prediction model:",
    ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction", "Breast Cancer"],
    index=0,
)

try:
    with open(MODEL_DIR / "diabetes_model.sav", "rb") as f:
        diabetes_model = pickle.load(f)
    with open(MODEL_DIR / "heart_disease_model.sav", "rb") as f:
        heart_disease_model = pickle.load(f)
    with open(MODEL_DIR / "parkinsons_model.sav", "rb") as f:
        parkinsons_model = pickle.load(f)
    with open(MODEL_DIR / "breaset_model.sav", "rb") as f:
        breaset_model = pickle.load(f)
except Exception as e:
    st.error(f"Failed to load model files: {e}")
    st.stop()

if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")
    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.number_input("Number of Pregnancies", min_value=0.0, step=1.0)
    with col2:
        glucose = st.number_input("Glucose Level", min_value=0.0, step=1.0)
    with col3:
        blood_pressure = st.number_input("Blood Pressure", min_value=0.0, step=1.0)

    with col1:
        skin_thickness = st.number_input("Skin Thickness", min_value=0.0, step=1.0)
    with col2:
        insulin = st.number_input("Insulin Level", min_value=0.0, step=1.0)
    with col3:
        bmi = st.number_input("BMI", min_value=0.0, step=0.1)

    with col1:
        pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.01)
    with col2:
        age = st.number_input("Age", min_value=0, step=1)

    diagnosis = ""
    if st.button("Diabetes Test Result"):
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]
        pred = diabetes_model.predict([user_input])[0]
        diagnosis = "The person is diabetic" if pred == 1 else "The person is not diabetic"

    st.success(diagnosis)

elif selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=0, step=1)
    with col2:
        sex = st.number_input("Sex", min_value=0, step=1)
    with col3:
        cp = st.number_input("Chest Pain Type", min_value=0, step=1)

    with col1:
        trestbps = st.number_input("Resting Blood Pressure", min_value=0.0, step=1.0)
    with col2:
        chol = st.number_input("Serum Cholestoral", min_value=0.0, step=1.0)
    with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120", min_value=0.0, step=1.0)

    with col1:
        restecg = st.number_input("Resting ECG", min_value=0, step=1)
    with col2:
        thalach = st.number_input("Max Heart Rate", min_value=0.0, step=1.0)
    with col3:
        exang = st.number_input("Exercise Induced Angina", min_value=0, step=1)

    with col1:
        oldpeak = st.number_input("ST Depression", min_value=0.0, step=0.1)
    with col2:
        slope = st.number_input("Slope", min_value=0, step=1)
    with col3:
        ca = st.number_input("Major Vessels", min_value=0, step=1)

    with col1:
        thal = st.number_input("Thal", min_value=0, step=1)

    diagnosis = ""
    if st.button("Heart Disease Test Result"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        pred = heart_disease_model.predict([user_input])[0]
        diagnosis = "The person is having heart disease" if pred == 1 else "The person does not have heart disease"

    st.success(diagnosis)

elif selected == "Parkinson's Prediction":
    st.title("Parkinson's Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input("MDVP:Fo(Hz)", min_value=0.0, step=1.0)
    with col2:
        fhi = st.number_input("MDVP:Fhi(Hz)", min_value=0.0, step=1.0)
    with col3:
        flo = st.number_input("MDVP:Flo(Hz)", min_value=0.0, step=1.0)
    with col4:
        jitter_percent = st.number_input("MDVP:Jitter(%)", min_value=0.0, step=0.01)
    with col5:
        jitter_abs = st.number_input("MDVP:Jitter(Abs)", min_value=0.0, step=0.01)

    with col1:
        rap = st.number_input("MDVP:RAP", min_value=0.0, step=0.01)
    with col2:
        ppq = st.number_input("MDVP:PPQ", min_value=0.0, step=0.01)
    with col3:
        ddp = st.number_input("Jitter:DDP", min_value=0.0, step=0.01)
    with col4:
        shimmer = st.number_input("MDVP:Shimmer", min_value=0.0, step=0.01)
    with col5:
        shimmer_db = st.number_input("MDVP:Shimmer(dB)", min_value=0.0, step=0.01)

    with col1:
        apq3 = st.number_input("Shimmer:APQ3", min_value=0.0, step=0.01)
    with col2:
        apq5 = st.number_input("Shimmer:APQ5", min_value=0.0, step=0.01)
    with col3:
        apq = st.number_input("MDVP:APQ", min_value=0.0, step=0.01)
    with col4:
        dda = st.number_input("Shimmer:DDA", min_value=0.0, step=0.01)
    with col5:
        nhr = st.number_input("NHR", min_value=0.0, step=0.01)

    with col1:
        hnr = st.number_input("HNR", min_value=0.0, step=0.01)
    with col2:
        rpde = st.number_input("RPDE", min_value=0.0, step=0.01)
    with col3:
        dfa = st.number_input("DFA", min_value=0.0, step=0.01)
    with col4:
        spread1 = st.number_input("spread1", min_value=-10.0, step=0.01)
    with col5:
        spread2 = st.number_input("spread2", min_value=-10.0, step=0.01)

    with col1:
        d2 = st.number_input("D2", min_value=0.0, step=0.01)
    with col2:
        ppe = st.number_input("PPE", min_value=0.0, step=0.01)

    diagnosis = ""
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]
        pred = parkinsons_model.predict([user_input])[0]
        diagnosis = "The person has Parkinson's disease" if pred == 1 else "The person does not have Parkinson's disease"

    st.success(diagnosis)

elif selected == "Breast Cancer":
    st.title("Breast Cancer")
    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.number_input("radius_mean", min_value=0.0, step=0.01)
    with col2:
        texture_mean = st.number_input("texture_mean", min_value=0.0, step=0.01)
    with col3:
        perimeter_mean = st.number_input("perimeter_mean", min_value=0.0, step=0.01)

    with col1:
        area_mean = st.number_input("area_mean", min_value=0.0, step=0.01)
    with col2:
        smoothness_mean = st.number_input("smoothness_mean", min_value=0.0, step=0.01)
    with col3:
        compactness_mean = st.number_input("compactness_mean", min_value=0.0, step=0.01)

    with col1:
        concavity_mean = st.number_input("concavity_mean", min_value=0.0, step=0.01)
    with col2:
        concave_points_mean = st.number_input("concave points_mean", min_value=0.0, step=0.01)
    with col3:
        symmetry_mean = st.number_input("symmetry_mean", min_value=0.0, step=0.01)

    with col1:
        fractal_dimension_mean = st.number_input("fractal_dimension_mean", min_value=0.0, step=0.01)

    diagnosis = ""
    if st.button("Breast Test Result"):
        user_input = [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
                      concavity_mean, concave_points_mean, fractal_dimension_mean, symmetry_mean]
        pred = breaset_model.predict([user_input])[0]
        diagnosis = "The person is diagnosed with breast cancer" if pred == 1 else "The person is not diagnosed with breast cancer"

    st.success(diagnosis)
