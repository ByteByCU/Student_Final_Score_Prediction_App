import streamlit as st
import pandas as pd
import joblib

# Load trained model
model=joblib.load("student_final_score_model.pkl")

# Page Title
st.title("Student Final Exam Score Predictor")
st.write("Enter the student details to predict the Final Exam Score.")

# Input 1
study_hours=st.number_input(
    "Study Hours per Week",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)

# Input 2
attendance=st.number_input(
    "Attendance Rate",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

# Input 3
previous_grades=st.number_input(
    "Previous Grades",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

# Input 4
extracurricular=st.selectbox(
    "Participation in Extracurricular Activities",
    ["No","Yes"]
)

# Convert Yes/No to 0/1
if extracurricular=="Yes":
    extracurricular_value=1
else:
    extracurricular_value=0

# Input 5
parent_education=st.selectbox(
    "Parent Education Level",
    [
        "High School",
        "Associate",
        "Bachelor",
        "Master",
        "Doctorate"
    ]
)

# Convert education level to numbers
parent_education_value={
    "High School":0,
    "Associate":1,
    "Bachelor":2,
    "Master":3,
    "Doctorate":4
}[parent_education]

# Prediction Button
if st.button("Predict Final Exam Score"):

    input_data=pd.DataFrame([[
        study_hours,
        attendance,
        previous_grades,
        extracurricular_value,
        parent_education_value
    ]],columns=[
        "Study Hours per Week",
        "Attendance Rate",
        "Previous Grades",
        "Participation in Extracurricular Activities",
        "Parent Education Level"
    ])

    prediction=model.predict(input_data)

    score=prediction[0]
    if score > 40.00:
        st.success(f"Predicted Final Exam Score: {score:.2f}")
    else:
        st.warning(f'Predicted Final Exam Score: {score:.2f}')
