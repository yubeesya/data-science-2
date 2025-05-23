import streamlit as st
import joblib
import json
import numpy as np


# Load model & scaler
model = joblib.load('./model/model.pkl')
scaler = joblib.load('model/scaler.pkl')
with open("model/features.json") as f:
    feature_order = json.load(f)
  
st.set_page_config(page_title="Dropout Prediction Student", layout="centered")

st.title("\U0001F393 Dropout Prediction Student Jaya Jaya Institut")
st.write("Fill out the form below to predict the status of students who have the potential to drop out.")

# --- FORM INPUT MANUSIAWI ---
with st.form("form_prediksi"):
    st.subheader("Student Academic and Social Data")

    # Beberapa input dipilih sebagai representatif, sisanya default 0
    marital_status = st.selectbox("Marital Status", [1, 2, 3, 4, 5, 6],
        format_func=lambda x: {
            1: "1 – Single", 2: "2 – Married", 3: "3 – Widower",
            4: "4 – Divorced", 5: "5 – Facto Union", 6: "6 – Legally Separated"
        }[x])

    application_mode = st.selectbox("Application Mode", [1, 2, 5, 7, 10, 15, 39, 42, 51, 57],
        format_func=lambda x: {
            1: "1 – 1st Phase (General)", 2: "2 – Ordinance 612/93",
            5: "5 – Special (Azores)", 7: "7 – Another PT", 10: "10 – Ordinance 854-B/99",
            15: "15 – International Student", 39: "39 – Usia >23 tahun",
            42: "42 – Transfer", 51: "51 – Change of Institution", 57: "57 – Int'l Transfer"
        }.get(x, f"Mode {x}"))

    admission_grade = st.slider("Admission Grade (0-200)", 0, 200, 130)
    previous_qualification_grade = st.slider("Admission Grade (0-200)", 0, 200, 120)
    age = st.slider("Age at Enrollment", 17, 60, 20)

    tuition_status = st.radio("Tuition Status", ["In-credit", "Late"])
    tuition_val = 1 if tuition_status == "In-credit" else 0

    curr_1st_grade = st.slider("Curricular units 1st semester grade (0-20)", 0.0, 20.0, 12.0)
    curr_2nd_grade = st.slider("Curricular units 2nd semester grade (0-20)", 0.0, 20.0, 12.0)

    approved_1st = st.number_input("Curricular units 1st semester approved", min_value=0, step=1)
    approved_2nd = st.number_input("Curricular units 2nd semester approved", min_value=0, step=1)

    submitted = st.form_submit_button("🔍 Predict")

# --- PREDIKSI ---
if submitted:
    # Buat template input default
    input_dict = {feat: 0 for feat in feature_order}

    # Masukkan nilai dari input pengguna
    input_dict.update({
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Admission_grade': admission_grade,
        'Previous_qualification_grade': previous_qualification_grade,
        'Age_at_enrollment': age,
        'Tuition_fees_up_to_date': tuition_val,
        'Curricular_units_1st_sem_grade': curr_1st_grade,
        'Curricular_units_2nd_sem_grade': curr_2nd_grade,
        'Curricular_units_1st_sem_approved': approved_1st,
        'Curricular_units_2nd_sem_approved': approved_2nd,
    })

    # Susun array input sesuai urutan
    input_array = np.array([[input_dict[feat] for feat in feature_order]])
    input_scaled = scaler.transform(input_array)

    pred = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][pred]
    label = "Dropout" if pred == 0 else "Graduate" 

    st.success(f"📢 Prediction: **{label}**  \n🎯 Probability: **{prob:.2%}**")
