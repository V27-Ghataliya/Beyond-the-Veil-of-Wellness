#!/usr/bin/env python3
"""
Beyond the Veil of Wellness - Application Runner
Author: VIRAL GHATALIYA
Description: Enhanced runner script for the Animal Health Classification web app
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} detected")

def check_virtual_environment():
    """Check if virtual environment is activated"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment is active")
        return True
    else:
        print("⚠️  Warning: Virtual environment not detected")
        return False

def install_requirements():
    """Install required packages"""
    if Path('requirements.txt').exists():
        print("📦 Installing requirements...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
            print("✅ Requirements installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install requirements")
            sys.exit(1)
    else:
        print("⚠️  requirements.txt not found")

def check_model_file():
    """Check if the trained model exists"""
    model_path = Path('models/rfc.pkl')
    if model_path.exists():
        print("✅ Model file found")
        return True
    else:
        print("❌ Model file (models/rfc.pkl) not found")
        print("📝 Please download your trained model from Google Colab and place it in the models/ directory")
        return False

def create_directories():
    """Create necessary directories"""
    directories = [
        'models',
        'static/css',
        'static/js', 
        'static/images',
        'templates'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("✅ Directory structure created")

def check_files():
    """Check if all necessary files exist"""
    required_files = [
        'app.py',
        'templates/base.html',
        'templates/index.html',
        'templates/inner-page.html',
        'templates/output.html',
        'templates/about.html',
        'templates/contact.html',
        'static/css/style.css',
        'static/js/script.js'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print("✅ All required files present")
        return True

def run_application():
    """Run the Flask application"""
    print("\n🚀 Starting Beyond the Veil of Wellness...")
    print("📍 Application will be available at: http://127.0.0.1:5000")
    print("🛑 Press Ctrl+C to stop the server\n")
    
    try:
        # Import and run the Flask app
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except ImportError as e:
        print(f"❌ Error importing app: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")
        sys.exit(1)

def main():
    """Main function to set up and run the application"""
    print("🌟 Beyond the Veil of Wellness - Animal Health Classification")
    print("=" * 60)
    
    # Pre-flight checks
    check_python_version()
    
    # Check virtual environment (warning only)
    check_virtual_environment()
    
    # Create necessary directories
    create_directories()
    
    # Install requirements
    install_requirements()
    
    # Check required files
    if not check_files():
        print("\n❌ Setup incomplete. Please ensure all files are present.")
        sys.exit(1)
    
    # Check model file
    if not check_model_file():
        print("\n❌ Model file missing. Please add your trained model before running.")
        response = input("Do you want to continue anyway? (y/N): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    print("\n✅ All checks passed!")
    print("🎉 Ready to launch the application!")
    
    # Run the application
    run_application()

if __name__ == "__main__":
    main()