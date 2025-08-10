import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def create_sample_data():
    """Create sample animal health data for training"""
    np.random.seed(42)
    
    # Sample data - you should replace this with your actual dataset
    data = {
        'temperature': np.random.normal(101, 2, 1000),  # Normal temp around 101°F for animals
        'heart_rate': np.random.normal(80, 15, 1000),   # Heart rate
        'respiratory_rate': np.random.normal(20, 5, 1000),  # Breathing rate
        'appetite': np.random.choice(['poor', 'fair', 'good'], 1000, p=[0.2, 0.3, 0.5]),
        'activity_level': np.random.choice(['low', 'medium', 'high'], 1000, p=[0.3, 0.4, 0.3]),
        'age_years': np.random.randint(1, 15, 1000),
        'weight_kg': np.random.normal(25, 10, 1000),
    }
    
    # Create target variable (health status)
    health_status = []
    for i in range(1000):
        score = 0
        # Temperature check
        if 99 <= data['temperature'][i] <= 102.5:
            score += 1
        # Heart rate check
        if 60 <= data['heart_rate'][i] <= 100:
            score += 1
        # Respiratory rate check
        if 15 <= data['respiratory_rate'][i] <= 25:
            score += 1
        # Appetite check
        if data['appetite'][i] == 'good':
            score += 1
        elif data['appetite'][i] == 'fair':
            score += 0.5
        # Activity level check
        if data['activity_level'][i] == 'high':
            score += 1
        elif data['activity_level'][i] == 'medium':
            score += 0.5
        
        # Determine health status
        if score >= 4:
            health_status.append('healthy')
        elif score >= 2.5:
            health_status.append('monitor')
        else:
            health_status.append('concern')
    
    data['health_status'] = health_status
    
    return pd.DataFrame(data)

def preprocess_data(df):
    """Preprocess the data for training"""
    # Create a copy to avoid modifying original data
    df_processed = df.copy()
    
    # Encode categorical variables
    label_encoders = {}
    categorical_columns = ['appetite', 'activity_level']
    
    for col in categorical_columns:
        le = LabelEncoder()
        df_processed[col] = le.fit_transform(df_processed[col])
        label_encoders[col] = le
    
    # Separate features and target
    X = df_processed.drop('health_status', axis=1)
    y = df_processed['health_status']
    
    return X, y, label_encoders

def train_model(X, y):
    """Train the machine learning model"""
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print("Training model...")
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    
    # Try both models and choose the best one
    models = {
        'DecisionTree': DecisionTreeClassifier(random_state=42, max_depth=10),
        'RandomForest': RandomForestClassifier(random_state=42, n_estimators=100, max_depth=10)
    }
    
    best_model = None
    best_accuracy = 0
    best_name = ""
    
    for name, model in models.items():
        # Train the model
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print(f"\n{name} Accuracy: {accuracy:.4f}")
        print(f"{name} Classification Report:")
        print(classification_report(y_test, y_pred))
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model
            best_name = name
    
    print(f"\nBest model: {best_name} with accuracy: {best_accuracy:.4f}")
    return best_model, best_accuracy

def save_model_and_encoders(model, label_encoders, model_path='models/'):
    """Save the trained model and encoders"""
    # Create models directory if it doesn't exist
    os.makedirs(model_path, exist_ok=True)
    
    # Save the model
    model_file = os.path.join(model_path, 'animal_health_model.pkl')
    joblib.dump(model, model_file)
    print(f"Model saved to: {model_file}")
    
    # Save the label encoders
    encoders_file = os.path.join(model_path, 'label_encoders.pkl')
    joblib.dump(label_encoders, encoders_file)
    print(f"Label encoders saved to: {encoders_file}")
    
    # Save feature names for reference
    feature_info = {
        'feature_names': ['temperature', 'heart_rate', 'respiratory_rate', 'appetite', 'activity_level', 'age_years', 'weight_kg'],
        'categorical_features': ['appetite', 'activity_level'],
        'target_classes': ['healthy', 'monitor', 'concern']
    }
    
    info_file = os.path.join(model_path, 'model_info.pkl')
    joblib.dump(feature_info, info_file)
    print(f"Model info saved to: {info_file}")

def main():
    """Main training function"""
    print("=== Animal Health Model Training ===")
    
    # Create or load your dataset
    print("Creating sample dataset...")
    df = create_sample_data()
    
    # If you have your own dataset, load it instead:
    # df = pd.read_csv('your_animal_health_data.csv')
    
    print(f"Dataset shape: {df.shape}")
    print(f"Health status distribution:")
    print(df['health_status'].value_counts())
    
    # Preprocess the data
    print("\nPreprocessing data...")
    X, y, label_encoders = preprocess_data(df)
    
    # Train the model
    print("\nTraining model...")
    model, accuracy = train_model(X, y)
    
    # Save everything
    print("\nSaving model and encoders...")
    save_model_and_encoders(model, label_encoders)
    
    print(f"\n=== Training Complete ===")
    print(f"Final model accuracy: {accuracy:.4f}")
    print("Files created:")
    print("- models/animal_health_model.pkl")
    print("- models/label_encoders.pkl")
    print("- models/model_info.pkl")
    
    # Test the saved model
    print("\n=== Testing Saved Model ===")
    test_saved_model()

def test_saved_model():
    """Test the saved model with sample predictions"""
    try:
        # Load the saved model
        model = joblib.load('models/animal_health_model.pkl')
        label_encoders = joblib.load('models/label_encoders.pkl')
        
        # Create a test sample
        test_data = {
            'temperature': [101.5],
            'heart_rate': [75],
            'respiratory_rate': [18],
            'appetite': ['good'],
            'activity_level': ['high'],
            'age_years': [5],
            'weight_kg': [30.0]
        }
        
        test_df = pd.DataFrame(test_data)
        
        # Encode categorical variables
        for col in ['appetite', 'activity_level']:
            test_df[col] = label_encoders[col].transform(test_df[col])
        
        # Make prediction
        prediction = model.predict(test_df)
        prediction_proba = model.predict_proba(test_df)
        
        print("Test prediction successful!")
        print(f"Sample input: {test_data}")
        print(f"Prediction: {prediction[0]}")
        print(f"Prediction probabilities: {prediction_proba[0]}")
        
    except Exception as e:
        print(f"Error testing saved model: {e}")

if __name__ == "__main__":
    main()