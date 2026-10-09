import os
import joblib
import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Diabetes Risk Assessment",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "diabetes_best_model.pkl")
METADATA_PATH = os.path.join(BASE_DIR, "diabetes_model_metadata.pkl")


# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    metadata = joblib.load(METADATA_PATH)
    return model, metadata


try:
    model, metadata = load_artifacts()
except FileNotFoundError:
    st.error(
        "Model files are missing. Keep `diabetes_best_model.pkl` and "
        "`diabetes_model_metadata.pkl` in the same folder as `app.py`."
    )
    st.stop()
except Exception as exc:
    st.error(f"Could not load the model files: {exc}")
    st.stop()


# ---------------------------------------------------------
# DESIGN / CSS
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #14213d;
        --muted: #64748b;
        --teal: #0f9b8e;
        --teal-dark: #087f75;
        --pale: #f2fbf9;
        --line: #e2e8f0;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background:
          radial-gradient(circle at 90% 0%, rgba(15,155,142,0.09), transparent 28%),
          linear-gradient(180deg, #f7fafc 0%, #f5f8fb 100%);
        color: var(--ink);
    }

    [data-testid="stHeader"] {
        background: rgba(247,250,252,0.85);
    }

    [data-testid="stSidebar"] {
        background: #102a43;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stSidebar"] * {
        color: #eaf4f7 !important;
    }

    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.16);
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 0 0 24px 0;
    }

    .brand-icon {
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 14px;
        background: linear-gradient(135deg, #2dd4bf, #0f9b8e);
        color: white;
        font-size: 23px;
        box-shadow: 0 8px 22px rgba(15,155,142,0.24);
    }

    .brand-name {
        color: #ffffff;
        font-family: 'Manrope', sans-serif;
        font-size: 17px;
        line-height: 1.2;
        font-weight: 800;
    }

    .brand-sub {
        color: #9fb3c8;
        font-size: 11px;
        margin-top: 4px;
        letter-spacing: 1.2px;
        text-transform: uppercase;
    }

    .hero {
        position: relative;
        overflow: hidden;
        background: linear-gradient(120deg, #102a43 0%, #174b59 62%, #0f9b8e 130%);
        padding: 34px 38px;
        border-radius: 24px;
        margin: 4px 0 24px 0;
        box-shadow: 0 18px 40px rgba(16,42,67,0.13);
    }

    .hero:after {
        content: "";
        position: absolute;
        width: 250px;
        height: 250px;
        border-radius: 50%;
        right: -60px;
        top: -115px;
        border: 38px solid rgba(255,255,255,0.07);
    }

    .eyebrow {
        color: #8ce9dc;
        font-size: 11px;
        letter-spacing: 2px;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 12px;
    }

    .hero h1 {
        color: #ffffff;
        font-family: 'Manrope', sans-serif;
        font-size: clamp(28px, 3vw, 42px);
        line-height: 1.13;
        letter-spacing: -1.2px;
        margin: 0 0 12px 0;
        font-weight: 800;
    }

    .hero p {
        color: #d7e9ef;
        max-width: 680px;
        font-size: 15px;
        line-height: 1.7;
        margin: 0;
    }

    .hero-chip {
        display: inline-block;
        margin-top: 20px;
        padding: 7px 12px;
        border-radius: 999px;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.18);
        color: #f0fffd;
        font-size: 12px;
    }

    .section-heading {
        font-family: 'Manrope', sans-serif;
        color: #14213d;
        font-size: 21px;
        font-weight: 800;
        margin: 8px 0 5px 0;
    }

    .section-sub {
        color: #64748b;
        font-size: 13px;
        margin-bottom: 18px;
    }

    [data-testid="stForm"] {
        background: #ffffff;
        border: 1px solid #e3eaf0;
        border-radius: 20px;
        padding: 24px 26px 20px 26px;
        box-shadow: 0 8px 28px rgba(15, 35, 60, 0.045);
    }

    [data-testid="stWidgetLabel"] p {
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
    }

    input, [data-baseweb="select"] > div {
        border-radius: 10px !important;
    }

    div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
        border: 0;
        border-radius: 12px;
        padding: 0.78rem 1rem;
        min-height: 48px;
        color: white;
        background: linear-gradient(100deg, #0f9b8e, #087f75);
        font-weight: 700;
        box-shadow: 0 7px 18px rgba(15,155,142,0.18);
        transition: all 0.2s ease;
    }

    div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        border: 0;
        color: white;
        background: linear-gradient(100deg, #0b8a7e, #066d65);
        transform: translateY(-1px);
    }

    .result-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 24px 26px;
        box-shadow: 0 10px 30px rgba(15,35,60,0.055);
        margin-top: 20px;
    }

    .result-label {
        color: #64748b;
        font-size: 11px;
        letter-spacing: 1.6px;
        text-transform: uppercase;
        font-weight: 700;
    }

    .result-title {
        color: #14213d;
        font-family: 'Manrope', sans-serif;
        font-size: 27px;
        font-weight: 800;
        margin: 8px 0;
    }

    .result-copy {
        color: #64748b;
        font-size: 14px;
        line-height: 1.65;
    }

    .metric-tile {
        background: #f0faf8;
        border: 1px solid #d1f0e9;
        border-radius: 16px;
        padding: 17px 18px;
        margin: 12px 0;
    }

    .metric-title {
        color: #52716f;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .metric-value {
        color: #087f75;
        font-family: 'Manrope', sans-serif;
        font-size: 28px;
        font-weight: 800;
        margin-top: 4px;
    }

    .info-strip {
        background: #edf5fb;
        border: 1px solid #d6e8f5;
        border-radius: 14px;
        padding: 14px 16px;
        color: #34536b;
        font-size: 12px;
        line-height: 1.65;
        margin: 20px 0;
    }

    .footer {
        color: #8291a5;
        font-size: 11px;
        text-align: center;
        padding: 24px 0 8px 0;
    }

    #MainMenu, footer { visibility: hidden; }

    @media (max-width: 700px) {
        .hero { padding: 26px 22px; border-radius: 18px; }
        [data-testid="stForm"] { padding: 18px 16px; }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="brand">
          <div class="brand-icon">✚</div>
          <div>
            <div class="brand-name">GlucoGuide</div>
            <div class="brand-sub">ML health insights</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Project overview")
    st.write(
        "An academic machine learning application that compares "
        "traditional classification algorithms on a diabetes dataset."
    )

    st.markdown("---")
    st.markdown("**CURRENT MODEL**")
    st.write(metadata.get("model_name", "Trained classifier"))

    st.markdown("---")
    st.markdown("**HOW IT WORKS**")
    st.write("01  Enter the available health details")
    st.write("02  Run the trained model")
    st.write("03  Review the predicted class")

    st.markdown("---")
    st.caption(
        "For learning and demonstration only. "
        "Not intended for diagnosis or treatment decisions."
    )


# ---------------------------------------------------------
# MAIN HEADER
# ---------------------------------------------------------
st.markdown(
    """
    <div class="hero">
      <div class="eyebrow">Preventive health • Machine learning</div>
      <h1>Type 2 Diabetes<br>Risk Prediction</h1>
      <p>
        Explore a machine-learning prediction based on the information entered.
        Add the available health details below to generate a result from the
        model trained on your dataset.
      </p>
      <span class="hero-chip">● &nbsp; Model-powered assessment</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Small summary tiles
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(
        '<div class="metric-tile"><div class="metric-title">Input features</div>'
        f'<div class="metric-value">{len(metadata["feature_columns"])}</div></div>',
        unsafe_allow_html=True
    )
with m2:
    st.markdown(
        '<div class="metric-tile"><div class="metric-title">Model type</div>'
        '<div class="metric-value" style="font-size:19px;">Classification</div></div>',
        unsafe_allow_html=True
    )
with m3:
    st.markdown(
        '<div class="metric-tile"><div class="metric-title">Output</div>'
        '<div class="metric-value" style="font-size:19px;">Predicted class</div></div>',
        unsafe_allow_html=True
    )

st.markdown('<div class="section-heading">Patient information</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-sub">Enter values carefully. Fields are generated from the features used during training.</div>',
    unsafe_allow_html=True
)

features = metadata["feature_columns"]
numeric_features = metadata["numeric_features"]
categorical_features = metadata["categorical_features"]

# Read categories from the fitted OneHotEncoder so inputs match training.
encoder_categories = {}
try:
    preprocessor = model.named_steps["preprocessor"]
    categorical_transformer = preprocessor.named_transformers_["categorical"]
    encoder = categorical_transformer.named_steps["encoder"]
    for feature, categories in zip(categorical_features, encoder.categories_):
        encoder_categories[feature] = list(categories)
except Exception:
    encoder_categories = {}

# Common feature-specific starting values and sensible UI bounds.
defaults = {
    "age": 40.0,
    "bmi": 25.0,
    "HbA1c_level": 5.5,
    "blood_glucose_level": 100.0,
    "hypertension": 0.0,
    "heart_disease": 0.0
}

help_text = {
    "age": "Age in years.",
    "bmi": "Body mass index (BMI).",
    "HbA1c_level": "HbA1c value as represented in your dataset.",
    "blood_glucose_level": "Blood glucose value in the dataset's units.",
    "hypertension": "Use the categories shown in the dataset.",
    "heart_disease": "Use the categories shown in the dataset."
}

input_values = {}

with st.form("patient_form", border=False):
    left, right = st.columns(2, gap="large")

    for index, feature in enumerate(features):
        current_column = left if index % 2 == 0 else right
        label = feature.replace("_", " ").title()

        with current_column:
            if feature in categorical_features:
                options = encoder_categories.get(feature, [])
                if options:
                    # Prefer common options first when they exist.
                    input_values[feature] = st.selectbox(
                        label,
                        options=options,
                        help=help_text.get(feature, f"Select a value recorded in the training dataset."),
                        key=f"field_{feature}"
                    )
                else:
                    input_values[feature] = st.text_input(
                        label,
                        help=help_text.get(feature, ""),
                        key=f"field_{feature}"
                    )
            else:
                default_value = float(defaults.get(feature, 0.0))

                if feature in ("hypertension", "heart_disease"):
                    input_values[feature] = st.selectbox(
                        label,
                        options=[0, 1],
                        format_func=lambda x: "No (0)" if x == 0 else "Yes (1)",
                        help=help_text.get(feature, ""),
                        key=f"field_{feature}"
                    )
                else:
                    # Use number input so this remains compatible with numeric model features.
                    if feature == "age":
                        min_value, max_value, step = 0.0, 120.0, 1.0
                    elif feature == "bmi":
                        min_value, max_value, step = 0.0, 100.0, 0.1
                    elif feature == "HbA1c_level":
                        min_value, max_value, step = 0.0, 30.0, 0.1
                    elif feature == "blood_glucose_level":
                        min_value, max_value, step = 0.0, 1000.0, 1.0
                    else:
                        min_value, max_value, step = -1_000_000.0, 1_000_000.0, 0.1

                    input_values[feature] = st.number_input(
                        label,
                        min_value=min_value,
                        max_value=max_value,
                        value=max(min_value, min(max_value, default_value)),
                        step=step,
                        help=help_text.get(feature, ""),
                        key=f"field_{feature}"
                    )

    submitted = st.form_submit_button(
        "Generate prediction   →",
        type="primary",
        use_container_width=True
    )


# ---------------------------------------------------------
# RESULT
# ---------------------------------------------------------
if submitted:
    input_df = pd.DataFrame([input_values], columns=features)

    try:
        prediction = int(model.predict(input_df)[0])
        classes = list(getattr(model, "classes_", [0, 1]))

        st.markdown('<div class="section-heading">Assessment result</div>', unsafe_allow_html=True)

        result_col, detail_col = st.columns([1.35, 1], gap="large")

        with result_col:
            if prediction == 1:
                result_title = "Diabetes class predicted"
                result_copy = (
                    "The model classified this input as class 1. "
                    "This result is not a diagnosis and should be interpreted "
                    "only as an output of the trained model."
                )
                result_color = "#a33d45"
                result_bg = "#fff5f5"
                result_border = "#f2d2d4"
                result_symbol = "!"
            else:
                result_title = "Non-diabetes class predicted"
                result_copy = (
                    "The model classified this input as class 0. "
                    "This does not rule out diabetes or replace medical testing."
                )
                result_color = "#087f75"
                result_bg = "#f0faf8"
                result_border = "#ccece5"
                result_symbol = "✓"

            st.markdown(
                f"""
                <div class="result-card" style="background:{result_bg}; border-color:{result_border};">
                  <div class="result-label">Model output</div>
                  <div style="display:flex;align-items:center;gap:14px;margin:14px 0;">
                    <div style="width:46px;height:46px;border-radius:14px;background:{result_color};
                                color:white;display:flex;align-items:center;justify-content:center;
                                font-size:24px;font-weight:800;">{result_symbol}</div>
                    <div class="result-title" style="font-size:23px;margin:0;color:{result_color};">
                      {result_title}
                    </div>
                  </div>
                  <div class="result-copy">{result_copy}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with detail_col:
            if hasattr(model, "predict_proba") and 1 in classes:
                probabilities = model.predict_proba(input_df)[0]
                diabetes_probability = float(probabilities[classes.index(1)])

                st.markdown(
                    f"""
                    <div class="result-card">
                      <div class="result-label">Model score for class 1</div>
                      <div class="result-title" style="color:#087f75;">
                        {diabetes_probability * 100:.1f}%
                      </div>
                      <div class="result-copy">
                        Model-estimated probability for the diabetes label.
                        This is not a clinically validated personal risk percentage.
                      </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """
                    <div class="result-card">
                      <div class="result-label">Selected algorithm</div>
                      <div class="result-title" style="font-size:22px;">
                        Model prediction
                      </div>
                      <div class="result-copy">
                        This classifier returns a class label but does not
                        provide a probability estimate.
                      </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown(
            """
            <div class="info-strip">
              <strong>Important health note</strong><br>
              This application is an academic demonstration. It is not validated
              for clinical use and must not be used to diagnose, treat, or rule out
              diabetes. If you have concerns, consult a qualified healthcare
              professional about appropriate testing.
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.expander("Review entered information"):
            st.dataframe(input_df, use_container_width=True, hide_index=True)

    except Exception as exc:
        st.error(f"Prediction could not be generated: {exc}")
        st.caption(
            "Check that both PKL files were created from the same training run "
            "and that your scikit-learn version is compatible."
        )


st.markdown(
    """
    <div class="footer">
      GLUCOGUIDE &nbsp; • &nbsp; TYPE 2 DIABETES RISK PREDICTION<br>
      Academic machine learning project · Not a medical device
    </div>
    """,
    unsafe_allow_html=True
)
