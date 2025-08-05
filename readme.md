# 🧠 Dementia Risk Prediction with SVM

This project is a **Flask-based web application** that predicts **dementia risk** using a **Support Vector Machine (SVM)** model trained on clinical and MRI data. It helps in early detection and risk assessment for timely interventions.

## 🚀 Features
- 🧠 SVM-based dementia risk classifier
- 🧹 Data preprocessing and feature normalization
- 🌐 Flask web interface for patient data entry
- 📊 Real-time risk prediction output
- ☁️ Deployment-ready for platforms like Render, Heroku, or AWS

## 📂 Project Structure
```
dementia-risk-predictor/
│── app.py                  # Flask web application for prediction
│── model.ipynb              # Notebook for data analysis and model training
│── dementia_dataset.csv     # Dataset used for training and inference
│── svm_dementia_model.pkl   # Trained SVM model
│── scaler.pkl               # Scaler for feature normalization
│── templates/
│     └── index.html         # Web form for user input
│── static/
│     └── style.css          # Stylesheet for the web interface
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
```

## ⚡ Installation & Usage
1. **Install dependencies**
   ```bash
   pip install flask numpy joblib scikit-learn pandas
   ```
2. **Run the web app**
   ```bash
   python app.py
   ```
   Open your browser → `http://127.0.0.1:5000`
3. **Make a prediction**
   - Fill in the patient data form
   - Click **Predict** to see the dementia risk result

## 🧬 Model Details
- **Features:** Age, EDUC, SES, MMSE, CDR, eTIV, nWBV, ASF, Gender
- **Gender:** `0 = Female`, `1 = Male`
- **Target:** Dementia Risk → `0 = Nondemented`, `1 = Demented/Converted`

## 🏋️ Training
Refer to [`model.ipynb`](model.ipynb) for detailed **data preprocessing**, **model training**, and **evaluation steps**.

## 🖼️ App Preview

<img width="1348" height="631" alt="Screenshot 2025-08-05 144633" src="https://github.com/user-attachments/assets/afd3101f-882e-4168-9ccd-0343a79c685f" />

