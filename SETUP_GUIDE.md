# 🚀 Complete Setup Guide - Beyond the Veil of Wellness

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.7+** (Check: `python --version` or `python3 --version`)
- **pip** (Python package installer)
- **Git** (for version control)
- **Text Editor/IDE** (VS Code, PyCharm, etc.)

## 🏗️ Step-by-Step Setup

### Step 1: Create Project Directory

```bash
# Create main project directory
mkdir animal_health_app
cd animal_health_app
```

### Step 2: Set Up Virtual Environment (MANDATORY)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows:
venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate

# Verify activation (you should see (venv) in your terminal)
```

### Step 3: Create Directory Structure

```bash
# Create all necessary directories
mkdir models
mkdir templates
mkdir static
mkdir static/css
mkdir static/js
mkdir static/images
```

Your directory structure should look like:
```
animal_health_app/
├── venv/                 # Virtual environment
├── models/              # For ML models
├── templates/           # HTML templates
├── static/
│   ├── css/            # CSS files
│   ├── js/             # JavaScript files
│   └── images/         # Image files
```

### Step 4: Install Required Packages

Create `requirements.txt`:
```bash
# Create requirements file with this content:
Flask==2.3.3
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
joblib==1.3.2
pickle-mixin==1.0.2
Werkzeug==2.3.7
Jinja2==3.1.2
MarkupSafe==2.1.3
itsdangerous==2.1.2
click==8.1.7
blinker==1.6.2
```

Then install:
```bash
pip install -r requirements.txt
```

### Step 5: Download Your Trained Model

1. Go to your Google Colab notebook
2. Download the `rfc.pkl` file (your trained Random Forest model)
3. Place it in the `models/` directory
4. Rename it to `rfc.pkl` if necessary

### Step 6: Create Application Files

Create the following files with the provided code:

#### 6.1 Main Application (`app.py`)
[Copy the Flask application code from the artifacts]

#### 6.2 HTML Templates
Create these files in the `templates/` directory:
- `base.html` - Base template
- `index.html` - Home page
- `inner-page.html` - Prediction form
- `output.html` - Results page
- `about.html` - About page
- `contact.html` - Contact page

#### 6.3 Static Files
Create these files in the `static/` directory:
- `static/css/style.css` - Custom styles
- `static/js/script.js` - JavaScript functionality

### Step 7: Test the Application

```bash
# Make sure virtual environment is activated
# Run the application
python app.py
```

You should see output like:
```
Model loaded successfully!
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://[your-ip]:5000
```

### Step 8: Access Your Application

Open your web browser and navigate to:
- **Local**: `http://127.0.0.1:5000`
- **Network**: `http://localhost:5000`

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue 1: "Model not found" Error
**Solution:**
```bash
# Check if model file exists
ls -la models/
# Should show rfc.pkl file

# If missing, download from Google Colab:
# 1. In Colab: files.download('rfc.pkl')
# 2. Move downloaded file to models/ directory
```

#### Issue 2: "Module not found" Error
**Solution:**
```bash
# Ensure virtual environment is activated
# Reinstall requirements
pip install -r requirements.txt

# Check installed packages
pip list
```

#### Issue 3: "Permission denied" Error (macOS/Linux)
**Solution:**
```bash
# Make run script executable
chmod +x run.py

# Or run with python directly
python app.py
```

#### Issue 4: Port 5000 already in use
**Solution:**
```bash
# Find process using port 5000
# Windows:
netstat -ano | findstr :5000

# macOS/Linux:
lsof -i :5000

# Kill the process or change port in app.py
```

### Model Integration Issues

If your model isn't working correctly:

1. **Check Model Format:**
```python
# Test your model file
import pickle
model = pickle.load(open('models/rfc.pkl', 'rb'))
print(type(model))  # Should be RandomForestClassifier
```

2. **Verify Feature Encoding:**
Make sure the encoding in `app.py` matches your training data encoding.

3. **Test Model Prediction:**
```python
# Create test data
import pandas as pd
test_data = pd.DataFrame([[0, 0, 0, 0, 0, 0]], 
                        columns=['AnimalName', 'BloodBrainDisease', 'AppearanceDisease', 
                                'GeneralDisease', 'LungDisease', 'AbdominalDisease'])
prediction = model.predict(test_data)
print(prediction)
```

## 🌐 Deployment Options

### Option 1: Local Development
```bash
python app.py
# Access at http://127.0.0.1:5000
```

### Option 2: Network Access
```bash
# Modify app.py to include your IP
app.run(debug=True, host='0.0.0.0', port=5000)
# Access from other devices: http://your-ip-address:5000
```

### Option 3: Production Deployment

#### Using Heroku:
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Add Procfile
echo "web: python app.py" > Procfile

# Deploy
git init
git add .
git commit -m "Initial commit"
heroku git:remote -a your-app-name
git push heroku main
```

#### Using Docker:
```bash
# Build image
docker build -t animal-health-app .

# Run container
docker run -p 5000:5000 animal-health-app
```

## 🎨 Customization

### Changing Colors
Edit `static/css/style.css` and modify the CSS variables:
```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
    /* etc. */
}
```

### Adding Your Images
1. Add your images to `static/images/`
2. Update image URLs in HTML templates
3. Recommended images:
   - `hero-bg.jpg` - Hero section background
   - `doctor-pet.jpg` - Doctor with pets
   - `logo.png` - Your logo
   - `favicon.ico` - Website icon

### Updating Content
- Modify HTML templates for content changes
- Update contact information in templates
- Add your social media links

## 📊 Model Requirements

Your `rfc.pkl` model should:
- Be a trained scikit-learn RandomForestClassifier
- Accept 6 features in this order:
  1. AnimalName (encoded)
  2. BloodBrainDisease (encoded)
  3. AppearanceDisease (encoded)
  4. GeneralDisease (encoded)
  5. LungDisease (encoded)
  6. AbdominalDisease (encoded)
- Output binary classification (0: Critical, 1: Normal)

## 🔐 Security Checklist

- [ ] Change the Flask secret key in `app.py`
- [ ] Set `debug=False` for production
- [ ] Use environment variables for sensitive data
- [ ] Implement HTTPS in production
- [ ] Add input sanitization
- [ ] Set up proper logging

## 📞 Support

If you encounter any issues:

1. **Check the console output** for error messages
2. **Verify all files are in place** according to the directory structure
3. **Ensure virtual environment is activated**
4. **Check Python and package versions**

**Contact Information:**
- 📧 Email: contact@example.com
- 📱 Phone: +91 78453 23860
- 🔗 LinkedIn: [linkedin.com/in/viral-ghataliya](https://linkedin.com/in/viral-ghataliya)

## 🎉 Success Indicators

Your setup is successful when:
- ✅ No error messages in terminal
- ✅ Application loads at http://127.0.0.1:5000
- ✅ All navigation links work
- ✅ Prediction form accepts input
- ✅ Model makes predictions successfully
- ✅ Results page displays correctly

**Happy coding! 🚀**