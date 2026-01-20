# Beyond the Veil of Wellness
## Machine Learning's Unique Journey in Animal Health Classification

### 🐾 Project Overview

**Beyond the Veil of Wellness** is an AI-powered web application that uses machine learning to classify animal health status. The system analyzes multiple health parameters to determine whether an animal requires immediate veterinary attention or is in normal health condition.

### 🎯 Features

- **Multi-Species Support**: Dogs, Cats, Birds, Horses, Cows, Sheep, Goats, and Pigs
- **Comprehensive Health Analysis**: Blood/Brain, Appearance, General, Lung, and Abdominal conditions
- **Real-Time Predictions**: Instant health status classification with confidence scores
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **User-Friendly Interface**: Intuitive design with modern UI/UX principles
- **95%+ Accuracy**: High-performance Random Forest Classifier
- **Professional Recommendations**: Evidence-based health advice and next steps

### 🚀 Technology Stack

- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Model**: Random Forest Classifier
- **Deployment**: Ready for cloud deployment

### 📁 Project Structure

```
animal_health_app/
│
├── venv/                          # Virtual environment
├── app.py                         # Main Flask application
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── models/                        # ML models directory
│   └── rfc.pkl                   # Trained Random Forest model
├── templates/                     # HTML templates
│   ├── base.html                 # Base template
│   ├── index.html                # Home page
│   ├── inner-page.html           # Prediction form
│   ├── output.html               # Results page
│   ├── about.html                # About page
│   └── contact.html              # Contact page
└── static/                        # Static files
    ├── css/
    │   └── style.css             # Custom styles
    ├── js/
    │   └── script.js             # JavaScript functionality
    └── images/                    # Website images
        ├── favicon.ico
        └── [other images]
```

### 🛠️ Installation & Setup

#### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd animal_health_app
```

#### Step 2: Create Virtual Environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Add Your Trained Model
- Download your trained model (`rfc.pkl`) from Google Colab
- Place it in the `models/` directory

#### Step 5: Create Directory Structure
```bash
mkdir -p models static/css static/js static/images templates
```

#### Step 6: Run the Application
```bash
python app.py
```

The application will be available at: `http://127.0.0.1:5000`

### 🔧 Configuration

#### Model Integration
Ensure your trained Random Forest model is saved as `rfc.pkl` in the `models/` directory. The model should expect the following features:
- AnimalName (encoded)
- BloodBrainDisease (encoded)
- AppearanceDisease (encoded)
- GeneralDisease (encoded)
- LungDisease (encoded)
- AbdominalDisease (encoded)

#### Environment Variables (Optional)
Create a `.env` file for configuration:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
```

### 📊 Model Information

- **Algorithm**: Random Forest Classifier
- **Training Data**: Animal health records with multiple disease indicators
- **Features**: 6 categorical features representing different health aspects
- **Output**: Binary classification (0: Critical, 1: Normal)
- **Accuracy**: 95%+ on test data

### 🎨 Design Features

#### Color Palette
- **Primary**: Sky Blue (#2563eb)
- **Secondary**: Light Blue (#3b82f6)
- **Accent**: Bright Blue (#0ea5e9)
- **Success**: Green (#059669)
- **Warning**: Orange (#d97706)
- **Danger**: Red (#dc2626)

#### Key Design Elements
- **Glass Morphism**: Modern glass-like navigation bar
- **Gradient Backgrounds**: Smooth color transitions
- **Micro-animations**: Hover effects and smooth transitions
- **Responsive Grid**: Mobile-first design approach
- **Accessibility**: WCAG 2.1 compliant design

### 🔍 Usage Guide

#### For Veterinarians
1. Navigate to "Check Health Status"
2. Select the animal type
3. Choose appropriate conditions for each health category
4. Submit for instant analysis
5. Review results and recommendations

#### For Pet Owners
1. Observe your pet's condition
2. Use the simple dropdown menus to describe symptoms
3. Get immediate health status assessment
4. Follow recommendations for veterinary care

#### For Farmers
1. Regular health monitoring of livestock
2. Early detection of potential health issues
3. Cost-effective screening before veterinary visits
4. Bulk assessment capabilities

### 🔒 Security & Privacy

- **Data Privacy**: No personal data is stored permanently
- **Secure Processing**: All computations happen server-side
- **Input Validation**: Comprehensive form validation and sanitization
- **Error Handling**: Graceful error management and user feedback

### 🚀 Deployment Options

#### Local Development
```bash
python app.py
```

#### Production Deployment

**Option 1: Heroku**
```bash
# Install Heroku CLI and login
heroku create your-app-name
git push heroku main
```

**Option 2: Docker**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

**Option 3: Cloud Platforms**
- AWS EC2 with Elastic Beanstalk
- Google Cloud Platform App Engine
- Microsoft Azure App Service

### 📈 Performance Optimization

- **Caching**: Model loaded once at startup
- **Compression**: Gzip compression for static files
- **CDN**: External libraries loaded from CDN
- **Lazy Loading**: Images and components loaded on demand
- **Minification**: CSS and JS optimization

### 🧪 Testing

#### Unit Tests
```bash
python -m pytest tests/
```

#### Model Validation
```python
# Test model accuracy
from sklearn.metrics import accuracy_score, classification_report

# Load test data and evaluate
accuracy = accuracy_score(y_true, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")
```

### 📝 API Documentation

#### Prediction Endpoint
```
POST /submit
Content-Type: application/x-www-form-urlencoded

Parameters:
- animal_name: string (required)
- blood_brain_disease: string (required)
- appearance_disease: string (required)
- general_disease: string (required)
- lung_disease: string (required)
- abdominal_disease: string (required)
```

### 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 👨‍💻 Developer

**VIRAL GHATALIYA**
- 🔗 LinkedIn: [linkedin.com/in/viral-ghataliya](https://linkedin.com/in/viral-ghataliya)

### 🙏 Acknowledgments

- Veterinary professionals for domain expertise
- Open-source community for tools and libraries
- Animal health research for training data insights

*Owned by VIRAL GHATALIYA*
