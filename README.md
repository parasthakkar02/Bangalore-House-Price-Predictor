# Bangalore House Price Predictor

Bangalore House Price Predictor is a project that leverages machine learning techniques to predict house prices of Bangalore city based on various parameters. The predictions are accessible through a user-friendly Django web application.

## Table of Contents
- [ML Model](#ml-model)
- [Django Web Application](#django-web-application)
- [Dependencies](#dependencies)
- [Getting Started](#getting-started)

## ML Model

The machine learning model involves extensive data preprocessing, model training, and validation. It is trained using regression techniques and the dataset was sourced from Kaggle, specific to Bangalore city. The trained model is then utilized in the Django web application for real-time price predictions.

## Django Web Application

The Django web application provides an intuitive interface for users to input property details and receive house price estimates as result. The application seamlessly integrates with the machine learning model, ensuring a smooth user experience.

## Dependencies

- Django==5.0.1
- numpy==1.26.3
- scikit-learn==1.4.0
- scipy==1.12.0
- pandas==2.1.4
- matplotlib==3.8.2

## Getting Started

This assumes that `python3` is linked to valid installation and `pip3` is valid for installing python 3 packages. Installing inside `virtualenv` is recommended, however you can start your project without virtualenv too.

To get started with the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Bangalore-House-Price-Predictor.git
   cd Bangalore-House-Price-Predictor
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Apply mirations:
   ```
   python manage.py migrate
   ```
5. Run the Django development server:
   ```
   python manage.py runserver
   ```
6. Access the application at http://localhost:8000 in your web browser.
