# Detecting Phishing Effectively: A Stable and Adaptable Mechanism

A machine learning-based web application designed to efficiently detect and classify potentially phishing or malicious messages. The system provides a web-based interface for message analysis and prediction, along with data management and result visualisation.

## 📌 Project Overview

Phishing is one of the most common forms of cybercrime, where attackers attempt to deceive users into revealing sensitive information through fraudulent messages and links.

This project focuses on developing a stable and adaptable mechanism for detecting phishing-related messages using machine learning techniques. The system provides a Django-based web interface through which users can submit messages for analysis and obtain prediction results.

## 🎯 Objectives

- Detect potentially phishing or malicious messages efficiently.
- Provide a simple web-based interface for users.
- Store and manage prediction-related data.
- Provide prediction results through a user-friendly interface.
- Support analysis and visualisation of collected results.
- Develop a mechanism that can be adapted for future improvements in phishing detection.

## 🛠️ Technologies Used

- Python
- Django
- MySQL
- HTML5
- CSS3
- JavaScript
- CSV Dataset
- Machine Learning

## 📂 Project Structure

- Database/
  - Detecting_Phishing_Effectively.sql
- Datastructure.txt
- Detecting_Phishing_Effectively/
  - Datasets.csv
  - Results.csv
  - manage.py
  - Detecting_Phishing_Effectively/
    - settings.py
    - urls.py
    - asgi.py
    - wsgi.py
  - Remote_User/
    - models.py
    - views.py
    - forms.py
    - migrations/
  - Service_Provider/
    - models.py
    - views.py
    - admin.py
    - migrations/
  - Template/
    - htmls/
    - images/
- .gitignore

## ⚙️ Main Features

### 👤 Remote User

- User registration and login.
- Submit messages for prediction.
- Analyse submitted messages.
- View prediction results.
- View relevant information related to message classification.

### 👨‍💼 Service Provider

- Service provider login.
- Manage user-related information.
- View remote user details.
- View prediction-related information.
- Analyse prediction results.
- View graphical representations of collected data.
- Manage system-related information.

## 🗄️ Database

The project uses MySQL for database management.

The database export is included in:

Database/Detecting_Phishing_Effectively.sql

The SQL file can be imported into MySQL to recreate the required database structure.

## 📊 Dataset

The project contains the dataset used by the phishing detection system.

Dataset:

Detecting_Phishing_Effectively/Datasets.csv

Prediction results:

Detecting_Phishing_Effectively/Results.csv

## 🚀 Installation and Setup

### 1. Clone the repository

git clone https://github.com/RaavanHrishi07/Detecting-Phishing-Effectively.git

cd Detecting-Phishing-Effectively

### 2. Create a virtual environment

python -m venv venv

Activate the environment on Windows:

venv\Scripts\activate

### 3. Install Django

pip install django

Additional dependencies may be required depending on the project environment.

### 4. Configure MySQL

Create the required MySQL database and import:

Database/Detecting_Phishing_Effectively.sql

Then configure the database settings in:

Detecting_Phishing_Effectively/Detecting_Phishing_Effectively/settings.py

### 5. Run migrations

python manage.py migrate

### 6. Start the Django development server

python manage.py runserver

Then open:

http://127.0.0.1:8000/

## 🔐 Security Note

This repository is intended for academic and educational purposes.

Sensitive credentials, passwords, API keys, and production secrets should not be committed to a public repository. Environment variables should be used when deploying the application in a production environment.

## 🔮 Future Scope

- Improve detection accuracy using larger and more diverse datasets.
- Support additional languages and message formats.
- Integrate advanced machine learning and deep learning techniques.
- Develop real-time phishing detection.
- Extend the system for email and URL-based phishing detection.
- Deploy the application as a cloud-based service.
- Improve the user interface and reporting capabilities.

## 👨‍💻 Author

Hrishikesh Sharma

Final Year Project

## 📄 License

This project was developed for academic and educational purposes.