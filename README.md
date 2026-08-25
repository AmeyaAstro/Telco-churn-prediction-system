# Telco Customer Churn Prediction System

## Live Demo

Streamlit App: <YOUR STREAMLIT APP LINK>

FastAPI API: https://telco-churn-prediction-system.onrender.com

API Docs: https://telco-churn-prediction-system.onrender.com/docs

## Project Overview

This project is an end-to-end machine learning application for predicting customer churn using telecommunications customer data.

The project covers the full workflow from exploratory data analysis and preprocessing through model training, API development, frontend development, and cloud deployment.

## Machine Learning Workflow

Raw Telco Data
→ Data Cleaning
→ Feature / Target Preparation
→ Train/Test Split
→ Preprocessing Pipeline
→ Logistic Regression
→ Model Evaluation
→ Model Persistence

## Model Performance

Accuracy: 80.6%

Precision: 65.7%

Recall: 55.9%

F1 Score: 60.4%

ROC-AUC: 72.7%

The baseline model shows useful churn discrimination, but recall remains an area for improvement because the model misses a meaningful portion of actual churners.

## System Architecture

User
→ Streamlit Frontend
→ FastAPI Backend
→ Saved scikit-learn Pipeline
→ Churn Prediction
→ API Response
→ Streamlit Result

## Technologies

- Python
- pandas
- NumPy
- scikit-learn
- FastAPI
- Pydantic
- Streamlit
- joblib
- Git/GitHub
- Render
- Streamlit Community Cloud

## Project Structure

api/
- FastAPI backend

app/
- Streamlit frontend

data/
- Raw dataset

models/
- Saved ML pipeline

notebooks/
- EDA and model development

src/
- Reusable inference logic

tests/
- Future automated tests

## Future Improvements

- Optimize classification threshold
- Improve churn recall
- Compare additional classifiers
- Add PostgreSQL prediction logging
- Add automated tests
- Dockerize application
- Add monitoring