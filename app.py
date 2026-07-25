import streamlit as st
import pandas as pd
import joblib
import warnings

warnings.filterwarnings('ignore')

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(page_title="Student ML Predictor", page_icon="🎓", layout="centered")

# Custom Styling for vibrant blue buttons
st.markdown("""
    <style>
    /* Style Streamlit primary button to vibrant blue */
    div[data-testid="stButton"] > button[kind="primary"],
    div.stButton > button[kind="primary"] {
        background-color: #0083D6 !important;
        border-color: #0083D6 !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        transition: all 0.2s ease-in-out !important;
    }
    div[data-testid="stButton"] > button[kind="primary"]:hover,
    div.stButton > button[kind="primary"]:hover {
        background-color: #006AA8 !important;
        border-color: #006AA8 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 131, 214, 0.3) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Load the trained model and scaler
model = joblib.load('models/student_performance_model.pkl')
scaler = joblib.load('models/scaler.pkl')
feature_names = joblib.load('models/feature_names.pkl')

# 3. Header Section
st.title(":material/school: Student Performance Predictor")
st.markdown("""
This Machine Learning tool uses **Linear Regression** to predict a student's final exam score based on their midterm academic habits. 
*Enter the student's metrics below (0-100 scale).*
""")
st.divider() # Draws a neat horizontal line

# 4. Input Section (Using Columns for a professional layout)
col1, col2 = st.columns(2)

with col1:
    attendance = st.number_input("Attendance %", min_value=0, max_value=100, value=80, step=5)
    assignment = st.number_input("Assignment Average %", min_value=0, max_value=100, value=75, step=5)
    midterm = st.number_input("Midterm Score %", min_value=0, max_value=100, value=70, step=5)

with col2:
    participation = st.number_input("Class Participation %", min_value=0, max_value=100, value=85, step=5)
    project = st.number_input("Project Score %", min_value=0, max_value=100, value=80, step=5)
    study_hours = st.number_input("Study Hours Per Week %", min_value=0, max_value=100, value=60, step=5)

st.divider()

# 5. Predict Button & Logic
if st.button("Predict Final Score", type="primary"): # type="primary" uses the blue theme color
    
    # Backend Validation Check
    if any(val < 0 or val > 100 for val in [attendance, assignment, midterm, participation, project, study_hours]):
        st.error("❌ Error: All input values must be strictly between 0 and 100.")
    else:
        # Prediction logic (Safely tucked inside the 'else' block)
        input_data = pd.DataFrame({
            'Attendance': [attendance / 100.0],
            'Assignment_Score': [assignment / 100.0],
            'Midterm_Score': [midterm / 100.0],
            'Class_Participation': [participation / 100.0],
            'Project_Score': [project / 100.0],
            'Study_Hours_Per_Week': [study_hours / 100.0]
        })
        
        input_data = input_data[feature_names]
        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data)[0]
        final_score_percentage = prediction * 100
        
        # 6. Display Results & Academic Support Messages
        st.subheader("Prediction Result")
        st.metric(label="Predicted Final Exam Score", value=f"{final_score_percentage:.1f}%")
        
        # Dynamic Support Messages
        if final_score_percentage >= 80:
            st.success(":material/star_shine: **Strong predicted performance.** This student is on track to excel.")
        elif final_score_percentage >= 50:
            st.info(":material/thumb_up: **Satisfactory predicted performance.** Student is passing, but could improve with focused study.")
        else:
            st.warning(":material/warning: **Alert:** This student may require additional academic support and early intervention.")
            
        st.caption("Note: This is an AI prediction and should supplement, not replace, a teacher's professional judgment.")