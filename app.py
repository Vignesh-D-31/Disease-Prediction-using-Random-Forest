from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load the model, encoder, and dataset
final_rf_model = joblib.load('model.joblib')
encoder = joblib.load(open('encoder.pkl', 'rb'))
df = pd.read_csv('Training.csv')
X = pd.read_csv("X.csv")
symptoms = X.columns.values

# Create a symptom index mapping
symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

data_dict = {
    "symptom_index": symptom_index,
    "predictions_classes": encoder.classes_
}

# Prediction function
def predictDisease(symptoms):
    symptoms = symptoms.split(",")
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        if symptom in data_dict["symptom_index"]:
            index = data_dict["symptom_index"][symptom]
            input_data[index] = 1
    input_data = np.array(input_data).reshape(1, -1)
    rf_prediction = final_rf_model.predict(input_data)[0]
    return rf_prediction

# Routes
@app.route('/')
def home():
    # Render the form with all symptoms as options
    symptom_options = list(symptom_index.keys())
    
    # Pass an empty list as default for selected_symptoms
    return render_template('index.html', symptoms=symptom_options, selected_symptoms=['', '', ''])

@app.route('/predict', methods=['POST'])
def predict():
    selected_symptoms = [
        request.form.get('symptom1', '-select-'),
        request.form.get('symptom2', '-select-'),
        request.form.get('symptom3', '-select-')
    ]
    
    prediction = predictDisease(",".join(selected_symptoms))
    
    symptom_options = [symptom.replace("_", " ").title() for symptom in symptoms]
    
    return render_template('index.html', symptoms=symptom_options, selected_symptoms=selected_symptoms, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
