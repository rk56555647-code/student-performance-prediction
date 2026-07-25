# Student Performance Prediction System

## Project Overview
This project is an end-to-end Machine Learning web application designed to predict a student's final exam score based on their continuous academic metrics. It serves as a practical demonstration of supervised learning regression techniques.

## Problem Statement & Objective
Educators often lack early quantitative indicators to identify students who are falling behind. The objective of this project is to use midterm academic habits (such as attendance and study hours) to predict final exam scores. This allows for early identification of students who may require additional academic support.

## Dataset & Features
The model uses a synthetic, mathematically grounded dataset containing continuous numerical values.
**Input Features (X):**
* Attendance Percentage
* Assignment Average
* Midterm Score
* Class Participation
* Project Score
* Study Habit Metric

**Target Variable (y):**
* Final Exam Score

## Machine Learning Workflow
1. **Data Preprocessing:** Features were standardized using `StandardScaler` to ensure uniform scaling.
2. **Model Selection:** Evaluated multiple regression algorithms including Linear Regression, Decision Tree Regressor, and Random Forest Regressor.
3. **Best Model:** **Linear Regression** was selected as the best performing model due to the linear nature of the feature-target relationships.
4. **Evaluation Metrics:** 
   * R² Score: ~0.78
   * Mean Absolute Error (MAE): ~0.04 (4%)

## Project Structure
```text
student-performance-prediction/
│
├── app.py                      # Main Streamlit web application code
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
└── models/                     # Saved Machine Learning files
    ├── student_performance_model.pkl
    ├── scaler.pkl
    └── feature_names.pkl  
```

## How to Run the Application Locally
Follow these step-by-step instructions to set up and run the Machine Learning web application on your local machine.

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system. You can check your Python version by running:
```bash
python --version
```

### 2. Navigate to the Project Directory
Open your terminal (PowerShell, Command Prompt, or Bash) and navigate to the project folder:
```bash
cd path/to/student-performance-prediction
```

### 3. Create and Activate a Virtual Environment
It is recommended to use a virtual environment to isolate project dependencies.

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
*(If using Command Prompt, run: `venv\Scripts\activate.bat`)*

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install all required Python packages (`streamlit`, `pandas`, `scikit-learn`, `joblib`, `numpy`) using `pip`:
```bash
pip install -r requirements.txt
```

### 5. Launch the Web Application
Start the Streamlit development server by running:
```bash
streamlit run app.py
```

### 6. View in Browser
Once the command executes, Streamlit will automatically open the application in your default web browser at:
* 🌐 **Local URL:** `http://localhost:8501`

---
💡 **Tip (Customizing Theme):** You can freely toggle between **Light Mode** and **Dark Mode** directly in the application by clicking the **`⋮` menu icon** in the top-right corner of the web page ➔ **Settings** ➔ **Theme**.
