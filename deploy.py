#!/usr/bin/env python3
"""
Beyond the Veil of Wellness - Deployment Helper
Author: VIRAL GHATALIYA
Description: Automated deployment script for various platforms
"""

import os
import sys
import subprocess
import json
from pathlib import Path

class DeploymentHelper:
    def __init__(self):
        self.project_name = "beyond-the-veil-wellness"
        self.app_name = "animal-health-app"
        
    def create_procfile(self):
        """Create Procfile for Heroku deployment"""
        procfile_content = "web: python app.py"
        with open('Procfile', 'w') as f:
            f.write(procfile_content)
        print("✅ Procfile created")
    
    def create_runtime_txt(self):
        """Create runtime.txt for Heroku"""
        python_version = f"python-{sys.version.split()[0]}"
        with open('runtime.txt', 'w') as f:
            f.write(python_version)
        print(f"✅ runtime.txt created with {python_version}")
    
    def create_app_json(self):
        """Create app.json for Heroku"""
        app_json = {
            "name": "Beyond the Veil of Wellness",
            "description": "AI-powered Animal Health Classification System",
            "keywords": ["flask", "machine-learning", "animal-health", "ai"],
            "website": "https://your-domain.com",
            "repository": "https://github.com/viralghataliya/animal-health-app",
            "env": {
                "FLASK_ENV": {
                    "description": "Flask environment",
                    "value": "production"
                },
                "SECRET_KEY": {
                    "description": "Secret key for Flask sessions",
                    "generator": "secret"
                }
            },
            "formation": {
                "web": {
                    "quantity": 1,
                    "size": "free"
                }
            },
            "addons": [],
            "buildpacks": [
                {
                    "url": "heroku/python"
                }
            ]
        }
        
        with open('app.json', 'w') as f:
            json.dump(app_json, f, indent=2)
        print("✅ app.json created")
    
    def prepare_for_heroku(self):
        """Prepare application for Heroku deployment"""
        print("🚀 Preparing for Heroku deployment...")
        
        self.create_procfile()
        self.create_runtime_txt()
        self.create_app_json()
        
        # Update app.py for production
        self.update_app_for_production()
        
        print("\n📝 Heroku deployment files created!")
        print("Next steps:")
        print("1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli")
        print("2. Login: heroku login")
        print("3. Create app: heroku create your-app-name")
        print("4. Deploy: git push heroku main")
    
    def update_app_for_production(self):
        """Update app.py for production deployment"""
        production_code = '''
# Add this to the end of app.py for production
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
'''
        
        print("📝 Production configuration ready")
        print("Note: Update the final lines in app.py with the production code above")
    
    def create_docker_compose(self):
        """Create docker-compose.yml for container deployment"""
        docker_compose = """version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=your-secret-key-here
    volumes:
      - ./models:/app/models
    restart: unless-stopped
    
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web
    restart: unless-stopped
"""
        
        with open('docker-compose.yml', 'w') as f:
            f.write(docker_compose)
        print("✅ docker-compose.yml created")
    
    def create_nginx_config(self):
        """Create Nginx configuration for production"""
        nginx_config = """events {
    worker_connections 1024;
}

http {
    upstream app {
        server web:5000;
    }
    
    server {
        listen 80;
        
        location / {
            proxy_pass http://app;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        
        location /static {
            alias /app/static;
            expires 1y;
            add_header Cache-Control "public, immutable";
        }
    }
}
"""
        
        with open('nginx.conf', 'w') as f:
            f.write(nginx_config)
        print("✅ nginx.conf created")
    
    def prepare_for_docker(self):
        """Prepare application for Docker deployment"""
        print("🐳 Preparing for Docker deployment...")
        
        self.create_docker_compose()
        self.create_nginx_config()
        
        print("\n📝 Docker deployment files created!")
        print("Next steps:")
        print("1. Build: docker-compose build")
        print("2. Run: docker-compose up -d")
        print("3. Access: http://localhost")
    
    def create_gitignore(self):
        """Create .gitignore file"""
        gitignore_content = """# Virtual Environment
venv/
env/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Flask
instance/
.webassets-cache

# Environment variables
.env
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Model files (if too large for git)
# models/*.pkl

# Temporary files
*.tmp
*.bak
"""
        
        with open('.gitignore', 'w') as f:
            f.write(gitignore_content)
        print("✅ .gitignore created")
    
    def create_env_template(self):
        """Create environment variables template"""
        env_template = """# Environment Variables Template
# Copy this file to .env and update the values

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database (if needed)
# DATABASE_URL=sqlite:///animal_health.db

# Email Configuration (if needed)
# MAIL_SERVER=smtp.gmail.com
# MAIL_PORT=587
# MAIL_USERNAME=your-email@gmail.com
# MAIL_PASSWORD=your-password

# External APIs (if needed)
# API_KEY=your-api-key
"""
        
        with open('.env.template', 'w') as f:
            f.write(env_template)
        print("✅ .env.template created")
    
    def run_deployment_menu(self):
        """Interactive deployment menu"""
        print("\n🌟 Beyond the Veil of Wellness - Deployment Helper")
        print("=" * 60)
        
        while True:
            print("\nChoose deployment option:")
            print("1. 🚀 Prepare for Heroku")
            print("2. 🐳 Prepare for Docker")
            print("3. 📁 Create Git files")
            print("4. 🔧 Create environment template")
            print("5. 📋 Full setup (all files)")
            print("6. ❌ Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                self.prepare_for_heroku()
            elif choice == '2':
                self.prepare_for_docker()
            elif choice == '3':
                self.create_gitignore()
            elif choice == '4':
                self.create_env_template()
            elif choice == '5':
                self.prepare_for_heroku()
                self.prepare_for_docker()
                self.create_gitignore()
                self.create_env_template()
                print("\n🎉 All deployment files created!")
            elif choice == '6':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.")

def main():
    """Main function"""
    deployer = DeploymentHelper()
    deployer.run_deployment_menu()

if __name__ == "__main__":
    main()