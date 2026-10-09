# Type 2 Diabetes Risk Prediction

A machine learning web application that estimates the risk of Type 2 Diabetes using health and demographic information. Built with Python, Scikit-learn, and Streamlit, and deployed on Render.

## Live Demo

**Live Application:** https://diabetes-prediction-fdtu.onrender.com

**GitHub Repository:** https://github.com/Shruti-Mandlik-07/diabetes_prediction

## Project Overview

Type 2 Diabetes is a chronic condition that affects how the body regulates blood glucose. This project explores how machine learning classification algorithms can use health-related features to predict diabetes status.

The application provides an interactive interface where users can enter relevant information and receive a model-generated prediction.

## Objectives

- Build a machine learning model for diabetes prediction.
- Train and compare multiple classification algorithms.
- Apply preprocessing to numerical and categorical features.
- Evaluate models using classification metrics.
- Deploy the trained model through an interactive web application.

## Machine Learning Algorithms

The training workflow compares nine classification algorithms:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Linear Support Vector Classifier (Linear SVC)
4. Decision Tree
5. Random Forest
6. Extra Trees
7. Gradient Boosting
8. AdaBoost
9. Gaussian Naive Bayes

The best-performing model is selected according to the evaluation criterion implemented in the training workflow.

## Technology Stack

- **Language:** Python
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Model Serialization:** Pickle / Joblib
- **Web Framework:** Streamlit
- **Version Control:** Git and GitHub
- **Deployment:** Render

## Key Features

- Interactive health-data input form.
- Machine learning-based diabetes prediction.
- Prediction probability when supported by the selected model.
- Integrated data preprocessing pipeline.
- Browser-accessible web interface.
- Cloud deployment for public access.

## Project Structure

```text
diabetes_prediction/
├── app.py
├── requirements.txt
├── diabetes_best_model.pkl
├── diabetes_model_metadata.pkl
├── .gitignore
└── README.md
```

| File | Description |
|---|---|
| `app.py` | Streamlit application and prediction logic |
| `requirements.txt` | Python dependencies |
| `diabetes_best_model.pkl` | Saved trained machine learning pipeline |
| `diabetes_model_metadata.pkl` | Feature information and model metadata |
| `.gitignore` | Files excluded from version control |

## Model Development Workflow

1. Load and explore the diabetes dataset.
2. Identify the target variable and input features.
3. Split the data into training and testing sets.
4. Handle missing values and preprocess numerical and categorical data.
5. Train multiple classification algorithms.
6. Compare model performance using evaluation metrics.
7. Select and save the best-performing pipeline.
8. Integrate the saved model into the Streamlit application.
9. Deploy the application using Render.

## Evaluation Metrics

The model comparison workflow considers:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Reliability of positive predictions.
- **Recall:** Ability to identify actual positive cases.
- **F1-score:** Balance between precision and recall.
- **ROC-AUC:** Ability to distinguish between the two classes, when applicable.

Actual performance depends on the dataset and test results. Refer to the training output for measured scores.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Shruti-Mandlik-07/diabetes_prediction.git
cd diabetes_prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, typically `http://localhost:8501`.

## Deployment

The application is hosted on Render and connected to the GitHub repository.

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
- **Branch:** `main`

## Future Enhancements

- Add model explainability using SHAP.
- Improve validation with cross-validation and independent datasets.
- Evaluate probability calibration and model fairness.
- Add visualizations for model performance and feature importance.
- Improve input validation and application monitoring.

## Limitations and Disclaimer

This application is an educational machine learning project. Its predictions depend on the quality and representativeness of the training data and may not generalize to every population.

**It is not a medical diagnostic tool.** Predictions should not replace professional medical advice, screening, or diagnosis.

## Author

**Shruti Mandlik**

GitHub: https://github.com/Shruti-Mandlik-07

---

If you find this project useful, consider starring the repository.
