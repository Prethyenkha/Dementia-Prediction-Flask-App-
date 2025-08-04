from flask import Flask, render_template, request
import numpy as np
import joblib  # joblib can still load .pkl files as long as they were saved with joblib

app = Flask(__name__)

# Load the model and scaler
model = joblib.load('svm_dementia_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        try:
            # Collect input values from form
            inputs = [
                float(request.form['Age']),
                float(request.form['EDUC']),
                float(request.form['SES']),
                float(request.form['MMSE']),
                float(request.form['CDR']),
                float(request.form['eTIV']),
                float(request.form['nWBV']),
                float(request.form['ASF']),
                int(request.form['Gender'])  # 0 for Female, 1 for Male
            ]

            # Scale and predict
            inputs_scaled = scaler.transform([inputs])
            result = model.predict(inputs_scaled)[0]
            prediction = 'Demented' if result == 1 else 'Non-Demented'

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
