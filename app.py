from flask import Flask, request, render_template, redirect, url_for, flash
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import os
import secrets
import joblib


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Change this to a random secret key
try:
    model = joblib.load('models/animal_health_model.pkl')
    label_encoders = joblib.load('models/label_encoders.pkl')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    label_encoders = None


# Load the trained model
#try:
#    model = pickle.load(open('models/rfc.pkl', 'rb'))
#    print("Model loaded successfully!")
#except Exception as e:
#    print(f"Error loading model: {e}")
#    model = None

# Define animal categories and disease options
ANIMAL_OPTIONS = ['Birds', 'Cats', 'Dogs', 'Horses', 'Cows', 'Sheep', 'Goats', 'Pigs']
DISEASE_OPTIONS = {
    'blood_brain': ['normal', 'anemia', 'leukemia', 'brain_tumor', 'encephalitis'],
    'appearance': ['normal', 'skin_lesions', 'hair_loss', 'emaciation', 'swelling'],
    'general': ['normal', 'fever', 'lethargy', 'coughing', 'vomiting'],
    'lung': ['normal', 'pneumonia', 'asthma', 'difficulty_breathing', 'lung_infection'],
    'abdominal': ['normal', 'bloating', 'diarrhea', 'abdominal_pain', 'constipation']
}

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    """Render the prediction form page"""
    return render_template('inner-page.html', 
                         animal_options=ANIMAL_OPTIONS,
                         disease_options=DISEASE_OPTIONS)

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    """Handle form submission and make predictions"""
    if request.method == 'POST':
        try:
            # Get form data
            animal_name = request.form.get('animal_name')
            blood_brain_disease = request.form.get('blood_brain_disease')
            appearance_disease = request.form.get('appearance_disease')
            general_disease = request.form.get('general_disease')
            lung_disease = request.form.get('lung_disease')
            abdominal_disease = request.form.get('abdominal_disease')
            
            # Validate input
            if not all([animal_name, blood_brain_disease, appearance_disease, 
                       general_disease, lung_disease, abdominal_disease]):
                flash('Please fill in all fields', 'error')
                return redirect(url_for('predict_page'))
            
            # Create feature array for prediction
            # Note: Adjust this based on your actual model's expected input format
            features = [
                animal_name,
                blood_brain_disease,
                appearance_disease,
                general_disease,
                lung_disease,
                abdominal_disease
            ]
            
            # Create label encoders (you may need to adjust this based on your training data)
            encoders = {}
            feature_names = ['AnimalName', 'BloodBrainDisease', 'AppearanceDisease', 
                           'GeneralDisease', 'LungDisease', 'AbdominalDisease']
            
            # Convert categorical features to numerical
            encoded_features = []
            
            # Simple encoding for demonstration (you should use the same encoding as in training)
            animal_encoding = {'Birds': 0, 'Cats': 1, 'Dogs': 2, 'Horses': 3, 
                             'Cows': 4, 'Sheep': 5, 'Goats': 6, 'Pigs': 7}
            
            disease_encoding = {'normal': 0, 'anemia': 1, 'leukemia': 2, 'brain_tumor': 3,
                              'encephalitis': 4, 'skin_lesions': 5, 'hair_loss': 6,
                              'emaciation': 7, 'swelling': 8, 'fever': 9, 'lethargy': 10,
                              'coughing': 11, 'vomiting': 12, 'pneumonia': 13, 'asthma': 14,
                              'difficulty_breathing': 15, 'lung_infection': 16, 'bloating': 17,
                              'diarrhea': 18, 'abdominal_pain': 19, 'constipation': 20}
            
            # Encode features
            encoded_features.append(animal_encoding.get(animal_name, 0))
            encoded_features.append(disease_encoding.get(blood_brain_disease, 0))
            encoded_features.append(disease_encoding.get(appearance_disease, 0))
            encoded_features.append(disease_encoding.get(general_disease, 0))
            encoded_features.append(disease_encoding.get(lung_disease, 0))
            encoded_features.append(disease_encoding.get(abdominal_disease, 0))
            
            # Create DataFrame for prediction
            input_data = pd.DataFrame([encoded_features], columns=feature_names)
            
            # Make prediction if model is loaded
            if model:
                prediction = model.predict(input_data)
                prediction_proba = model.predict_proba(input_data)
                
                # Get the prediction result
                result = int(prediction[0])
                confidence = max(prediction_proba[0]) * 100
                
                # Determine health status
                if result == 0:
                    health_status = "Critical - Immediate veterinary attention required!"
                    status_class = "critical"
                    recommendation = "Please consult a veterinarian immediately. The animal shows signs that require urgent medical attention."
                else:
                    health_status = "Normal - Animal appears healthy"
                    status_class = "normal"
                    recommendation = "The animal appears to be in good health. Continue regular care and monitoring."
                
                return render_template('output.html',
                                     animal_name=animal_name,
                                     health_status=health_status,
                                     status_class=status_class,
                                     confidence=round(confidence, 2),
                                     recommendation=recommendation,
                                     features={
                                         'Animal': animal_name,
                                         'Blood/Brain Disease': blood_brain_disease,
                                         'Appearance Disease': appearance_disease,
                                         'General Disease': general_disease,
                                         'Lung Disease': lung_disease,
                                         'Abdominal Disease': abdominal_disease
                                     })
            else:
                flash('Model not loaded. Please check the model file.', 'error')
                return redirect(url_for('predict_page'))
                
        except Exception as e:
            print(f"Error during prediction: {e}")
            flash('An error occurred during prediction. Please try again.', 'error')
            return redirect(url_for('predict_page'))
    
    return redirect(url_for('predict_page'))

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('models', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/images', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)