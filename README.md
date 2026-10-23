# Multiple Disease Prediction System

## 1. Project Overview

The Multiple Disease Prediction System is a machine learning-based web application designed to assist healthcare staff, researchers, and students in predicting the likelihood of several diseases based on patient health parameters. The system is built using Python and Streamlit, and it includes trained predictive models for:

- Diabetes
- Heart disease
- Parkinson’s disease
- Breast cancer

The goal of the project is to provide a simple, interactive medical prediction tool that can analyze patient data and generate a risk assessment based on historical medical datasets.

This project is intended for educational, research, and demonstration purposes. It is not a clinical diagnostic tool and should not replace a doctor’s judgment.

---

## 2. Problem Statement

Medical professionals often rely on multiple assessments and clinical tests to detect diseases. In many cases, early detection is crucial. However, traditional processes can be time-consuming and may require extensive manual effort.

This project addresses that problem by:
- automating disease-risk prediction using machine learning,
- allowing quick input of patient parameters,
- providing an easy-to-use interface for data entry and prediction,
- helping users understand the health risk associated with specific patients.

---

## 3. Project Description

The system provides a Streamlit web interface where the user can:

- log in to the application,
- select a disease prediction page,
- enter patient values,
- receive a prediction result based on a trained model,
- view or manage patient-related records in a sample database.

The project uses machine learning models stored in the `save_models/` directory and data files in the `dataset/` directory. The app is designed to run locally and is suitable for demonstration and training scenarios.

---

## 4. Objectives

The main objectives of this project are:

- To build an interactive disease prediction system.
- To support prediction for multiple diseases.
- To make predictions based on real healthcare datasets.
- To simplify the user experience through a user-friendly interface.
- To provide a foundation for future extension into real clinical dashboards.
- To support education and research in artificial intelligence and healthcare analytics.

---

## 5. HR and Human-Centered Aspects

Although this project is technical in nature, it also includes important human-resource and healthcare-support dimensions.

### 5.1 Human-Friendly Usage
The interface is designed to be simple enough for:
- healthcare workers,
- clinic staff,
- students,
- researchers,
- project evaluators.

### 5.2 Accessibility
The system is designed for practical use by people who may not be familiar with programming. A simple web interface reduces the need for technical expertise.

### 5.3 Role-Based Access
The application contains a login page that restricts unauthorized access and supports the idea of role-based use in healthcare environments.

### 5.4 Data Responsibility
Since the system deals with health-related information, it is important to observe the following:
- do not store real patient data without consent,
- avoid sharing sensitive medical information publicly,
- use anonymized or demonstration data when testing,
- follow local healthcare data protection rules.

### 5.5 Medical Ethics
The system should be used responsibly:
- It is not a medical diagnosis tool.
- It must not replace consultation with a licensed physician.
- It should be used only as a decision-support tool in educational and research contexts.

---

## 6. System Features

The application includes the following features:

- Login page
- Sidebar navigation
- Multi-disease prediction module
- Patient data management page
- Real dataset files for testing
- Pre-trained models for prediction
- Simple dashboard for demonstration

---

## 7. Supported Disease Models

### Diabetes Prediction
Uses patient parameters such as:
- number of pregnancies,
- glucose level,
- blood pressure,
- skin thickness,
- insulin,
- BMI,
- diabetes pedigree function,
- age.

### Heart Disease Prediction
Uses patient parameters such as:
- age,
- sex,
- chest pain type,
- resting blood pressure,
- cholesterol,
- fasting blood sugar,
- resting ECG,
- maximum heart rate,
- exercise angina,
- oldpeak,
- slope,
- number of major vessels,
- thal.

### Parkinson’s Disease Prediction
Uses voice-related and health signal parameters such as:
- MDVP values,
- shimmer,
- jitter,
- D2,
- PPE,
- HNR,
- spread values,
- and other signal measurements.

### Breast Cancer Prediction
Uses medical image-derived feature values such as:
- radius_mean,
- texture_mean,
- perimeter_mean,
- area_mean,
- smoothness_mean,
- compactness_mean,
- concavity_mean,
- concave points,
- symmetry,
- fractal dimension.

---

## 8. Project Structure

```text
multiple-disease-prediction/
├── login.py
├── navigation.py
├── README.md
├── requirements.txt
├── run.txt
├── .gitignore
├── .streamlit/
├── dataset/
│   ├── diabetes.csv
│   ├── heart.csv
│   ├── parkinsons.csv
│   └── Cancer.csv
├── save_models/
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   ├── parkinsons_model.sav
│   └── breaset_model.sav
├── pages/
│   ├── home.py
│   ├── Dashbord.py
│   └── Patientdata.py
├── doc/
├── file train model in jubter/
└── cfghyg.png
```

---

## 9. Installation Requirements

The project requires Python and a few Python libraries.

### Python Version
- Python 3.10 or higher is recommended.

### Install Dependencies

```bash
pip install -r requirements.txt
```

The file `requirements.txt` includes basic dependencies needed to run the Streamlit application.

---

## 10. How to Run the Project

Open a terminal in the project folder and run:

```bash
streamlit run login.py
```

Then open the URL shown in the terminal, typically:

```text
http://localhost:8501
```

---

## 11. Login Details

The application includes a simple login page. The default credentials are:

- Username: `Admin`
- Password: `123456789`

This is useful for demonstration and testing. For production use, the login mechanism should be improved with secure authentication and environment-based configuration.

---

## 12. How to Use the System

### Step 1: Open the App
Launch the app using Streamlit.

### Step 2: Log In
Use the provided login form.

### Step 3: Select Prediction Type
From the sidebar or prediction menu, choose the disease prediction section you want to use.

### Step 4: Enter Patient Values
Insert the required values for the selected disease.

### Step 5: Click Prediction Button
After entering values, press the prediction button.

### Step 6: Read the Result
The app will display a prediction result such as:
- patient is diabetic / not diabetic,
- disease detected / not detected,
- risk present / no risk.

### Step 7: Manage Patient Records
The patient data page allows adding or updating patient information in a local SQLite database.

---

## 13. How to Use the Datasets

The project includes real dataset files in the `dataset/` folder. These can be used to understand the model feature structure and validate that the app is receiving values in the correct format.

### Example: Diabetes Data

File: `dataset/diabetes.csv`

```csv
Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
6,148,72,35,0,33.6,0.627,50,1
1,85,66,29,0,26.6,0.351,31,0
8,183,64,0,0,23.3,0.672,32,1
```

This sample demonstrates the input format expected by the diabetes model.

### Example: Heart Data

```csv
age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target
63,1,3,145,233,1,0,150,0,2.3,0,0,1,1
37,1,2,130,250,0,1,187,0,3.5,0,0,2,1
41,0,1,130,204,0,0,172,0,1.4,2,0,2,1
```

### Example: Parkinson’s Data

```csv
name,MDVP:Fo(Hz),MDVP:Fhi(Hz),MDVP:Flo(Hz),MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP,MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA,NHR,HNR,status,RPDE,DFA,spread1,spread2,D2,PPE
phon_R01_S01_1,119.99200,157.30200,74.99700,0.00784,0.00007,0.00370,0.00554,0.01109,0.04374,0.42600,0.02182,0.03130,0.02971,0.06545,0.02211,21.03300,1,0.414783,0.815285,-4.813031,0.266482,2.301442,0.284654
```

These datasets can be used to:
- validate model input format,
- test predictions,
- understand real-world patient values,
- support educational demonstrations.

---

## 14. Important Notes

- The app is intended for educational and research purposes.
- It is not a clinical diagnostic system.
- Predictions are based on machine learning models and historical datasets.
- Real patient data should not be uploaded unless authorized.
- The system should be handled with proper privacy awareness.
- The project should be considered a prototype or demo platform, not a medical device.

---

## 15. Project Limitations

Although useful, the project has some limitations:

- It uses static datasets.
- Model performance depends on data quality.
- It does not include secure production-level authentication.
- It is not linked to real hospital systems.
- It does not include patient consent management or healthcare compliance handling.
- The prediction logic is based on sample learning models and may not be clinically validated.

---

## 16. Future Improvements

This project can be extended in several useful ways:

- Add secure authentication and role-based access control
- Add real-time patient database integration
- Add model performance charts and evaluation metrics
- Support CSV upload for batch prediction
- Add data validation and preprocessing
- Improve the dashboard design
- Add support for more diseases
- Integrate with hospital record systems
- Add export feature for reports
- Add audit logs for healthcare staff usage

---

## 17. Suggested Use Cases

This project is suitable for:

- academic demonstrations,
- healthcare awareness tools,
- university student projects,
- machine learning practice,
- medical decision-support prototypes,
- healthcare analytics demos.

---

## 18. Disclaimer

This application should not be used as a substitute for medical diagnosis or treatment. It is a machine learning demonstration project designed for educational and research purposes only. The final medical decision must always be made by a trained medical professional.

---

## 19. Conclusion

The Multiple Disease Prediction System is a practical application that demonstrates how machine learning can be used to support disease detection using real datasets and a user-friendly interface. It combines technical functionality with healthcare-oriented usability, offering a simplified platform for disease risk prediction.

The project is useful for learning, demonstration, and prototype development. With additional enhancements, it could be expanded into a more robust and secure healthcare application.

---

## 20. Contact / Project Notes

If you want to extend this project, the typical next steps are:
1. improve authentication,
2. validate model accuracy,
3. add CSV upload support,
4. add patient record security,
5. integrate with a real database or hospital workflow.

This project is a strong foundation for learning the connection between AI, healthcare, and user-friendly application design.
