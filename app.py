import streamlit as st
import pandas as pd

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Insurance Website Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------------------------
# Dashboard Title
# ----------------------------------------------------
st.title("📊 Insurance Website Analytics Dashboard")

st.markdown("""
Welcome to the interactive dashboard for analysing customer behaviour on an insurance company's website.

Use the filters on the left to explore:

- Marketing channel performance
- Device category performance
- Revenue
- Insurance quotes
- Policy purchases
- Customer engagement
""")