# Dementia Risk Prediction with SVM

This project predicts dementia risk using a Support Vector Machine (SVM) model trained on clinical and MRI data.

## Project Structure

- `app.py`: Flask web application for prediction.
- `model.ipynb`: Jupyter notebook for data analysis, model training, and export.
- `dementia_dataset.csv`: Dataset used for training and inference.
- `svm_dementia_model.pkl`: Trained SVM model.
- `scaler.pkl`: Scaler used for feature normalization.
- `templates/index.html`: Web form for user input.
- `static/style.css`: Stylesheet for the web interface.

## Usage

1. **Install dependencies**  
   ```
   pip install flask numpy joblib scikit-learn pandas
   ```

2. **Run the web app**  
   ```
   python app.py
   ```
   Visit `http://127.0.0.1:5000` in your browser.

3. **Make a prediction**  
   - Fill in the form with patient data.
   - Click "Predict" to see the result.

## Model Details

- Features: Age, EDUC, SES, MMSE, CDR, eTIV, nWBV, ASF, Gender
- Gender: 0 = Female, 1 = Male
- Target: Dementia risk (0 = Nondemented, 1 = Demented/Converted)

## Training

See [`model.ipynb`](model.ipynb) for data preprocessing, model training, and evaluation.

## License

For academic purposes only