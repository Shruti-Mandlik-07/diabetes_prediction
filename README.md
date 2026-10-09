# Type 2 Diabetes Risk Prediction

A machine learning web application that estimates the risk of Type 2 Diabetes based on user-provided health and demographic information. The application uses trained classification models and an interactive Streamlit interface to generate predictions.

## Live Demo

**Live Application:** [Open Diabetes Risk Prediction](YOUR_RENDER_URL)

**GitHub Repository:** [diabetes_prediction](https://github.com/Shruti-Mandlik-07/diabetes_prediction)

> Replace `YOUR_RENDER_URL` with your public Render URL.

## Project Overview

Type 2 Diabetes is a chronic condition that affects how the body regulates blood glucose. Early identification of potential risk factors can encourage timely medical consultation and preventive care.

This project applies machine learning classification techniques to a diabetes dataset and provides a user-friendly interface for generating predictions from health-related input features.

## Objectives

- Develop a machine learning model to predict diabetes risk.
- Compare multiple classification algorithms using evaluation metrics.
- Build an interactive web application using Streamlit.
- Deploy the application on Render for public access.
- Demonstrate an end-to-end machine learning workflow, from preprocessing and model evaluation to deployment.

## Machine Learning Models

The training workflow compares the following classification algorithms:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Linear Support Vector Classifier (Linear SVC)
- Decision Tree
- Random Forest
- Extra Trees
- Gradient Boosting
- AdaBoost
- Gaussian Naive Bayes

The best-performing model is selected based on the evaluation workflow implemented during training.

## Technology Stack

| Component | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Model Serialization | Joblib / Pickle |
| Web Application | Streamlit |
| Version Control | Git, GitHub |
| Deployment | Render |

## Application Features

- Interactive input form for health and demographic attributes.
- Machine learning-based diabetes prediction.
- Prediction probability when supported by the selected model.
- Data preprocessing integrated into the saved model pipeline.
- Responsive, browser-accessible Streamlit interface.
- Cloud deployment through Render.

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

### File Description

- `app.py` — Streamlit application and prediction interface.
- `requirements.txt` — Python package dependencies.
- `diabetes_best_model.pkl` — Saved trained machine learning pipeline.
- `diabetes_model_metadata.pkl` — Model metadata, feature information, and evaluation details.
- `.gitignore` — Excludes unnecessary files from version control.
- `README.md` — Project documentation.

## Installation and Local Setup

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

### 4. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Model Development Workflow

1. Load the diabetes dataset.
2. Inspect the data and prepare the target variable.
3. Separate input features and the target.
4. Split the data into training and testing sets.
5. Handle missing values and preprocess numerical and categorical features.
6. Train and compare multiple classification algorithms.
7. Evaluate models using appropriate classification metrics.
8. Select the best-performing model according to the implemented selection criterion.
9. Save the trained pipeline and metadata.
10. Integrate the saved model into the Streamlit application.
11. Deploy the application on Render.

## Evaluation Metrics

The model comparison workflow uses relevant classification metrics, including:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Proportion of predicted positive cases that are actually positive.
- **Recall:** Proportion of actual positive cases correctly identified.
- **F1-score:** Harmonic mean of precision and recall.
- **ROC-AUC:** Measures the model's ability to distinguish between the classes when applicable.

Actual metric values depend on the dataset, test split, and selected model. Refer to the training results for measured performance.

## Deployment

The application is deployed on **Render** using the connected GitHub repository.

Typical deployment configuration:

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
- **Branch:** `main`

## Limitations

- Predictions depend on the quality, representativeness, and limitations of the training dataset.
- Performance on unseen populations may differ from test-set performance.
- Model outputs represent estimates, not confirmed diagnoses.
- A prediction probability should not be interpreted as a person's medically calibrated probability of developing diabetes unless calibration has been independently evaluated.
- The application is intended for educational and research purposes, not for clinical decision-making.

## Future Enhancements

- Add explainability techniques such as SHAP to help interpret predictions.
- Improve model validation using cross-validation and external datasets.
- Evaluate probability calibration and fairness across demographic groups.
- Add data visualizations and model performance dashboards.
- Strengthen input validation and application monitoring.

## Disclaimer

This project is intended for educational and research purposes only. It is not a medical diagnostic tool and must not replace advice, screening, or diagnosis from a qualified healthcare professional.

## Author

**Shruti Mandlik**

GitHub: [Shruti-Mandlik-07](https://github.com/Shruti-Mandlik-07)

---

If you find this project useful, consider starring the repository.
