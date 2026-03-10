import sys
import os
import streamlit as st
import pandas as pd

# Add project root to path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

# Imports from your project
from pipeline.data_pipeline import run_pipeline
from ai.ai_analytics import ask_question
from ai.auto_analyst import auto_analyze
from scripts.generate_reports import map_columns

st.set_page_config(page_title="AI Quick Commerce BI", layout="wide")

st.title("🚀 AI Quick Commerce Business Intelligence")

st.write("Upload a dataset to analyze quick commerce performance.")

# -----------------------------
# File Upload
# -----------------------------

uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    mapper = map_columns(df)

    # -----------------------------
    # Run Data Pipeline
    # -----------------------------

    st.subheader("Data Pipeline")

    if st.button("Run Data Cleaning Pipeline"):

        temp_file = "temp_uploaded.csv"

        df.to_csv(temp_file, index=False)

        df_clean, clean_path = run_pipeline(temp_file)

        st.success("Pipeline completed successfully")

        st.write("Clean Dataset Preview")

        st.dataframe(df_clean.head())

    # -----------------------------
    # AI Business Questions
    # -----------------------------

    st.subheader("Ask AI Business Question")

    question = st.text_input("Example: revenue by city")

    if st.button("Analyze Question"):

        result = ask_question(df, mapper, question)

        if isinstance(result, str):

            st.success(result)

        else:

            st.write(result)

            if isinstance(result, pd.Series):

                st.bar_chart(result)

    # -----------------------------
    # Automatic AI Analysis
    # -----------------------------

    st.subheader("AI Automatic Business Analysis")

    if st.button("Run Full AI Analysis"):

        report = auto_analyze(df, mapper)

        col1, col2 = st.columns(2)

        with col1:

            st.write("### Key Metrics")

            st.write(report["metrics"])

            st.write("### Top Platforms")

            st.bar_chart(report["platforms"])

        with col2:

            st.write("### Top Cities")

            st.bar_chart(report["cities"])

            st.write("### Popular Categories")

            st.bar_chart(report["categories"])

        st.write("### AI Insights")

        for insight in report["insights"]:

            st.write("•", insight)

        st.success(report["recommendation"])