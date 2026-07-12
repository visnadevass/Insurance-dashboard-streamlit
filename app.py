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
# Load Dataset
# ----------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Data/Cleaned/insurance_cleaned.csv")
    return df

df = load_data()
# ----------------------------------------------------
# Sidebar Filters
# ----------------------------------------------------
st.sidebar.header("📂 Dashboard Filters")

# Marketing Channel Filter
selected_channels = st.sidebar.multiselect(
    "Select Marketing Channel",
    options=sorted(df["Marketing Channel"].unique()),
    default=sorted(df["Marketing Channel"].unique())
)

# Device Category Filter
selected_devices = st.sidebar.multiselect(
    "Select Device Category",
    options=sorted(df["Device Category"].unique()),
    default=sorted(df["Device Category"].unique())
)

# Apply Filters
filtered_df = df[
    (df["Marketing Channel"].isin(selected_channels)) &
    (df["Device Category"].isin(selected_devices))
]
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

st.divider()

# ----------------------------------------------------
# Dataset Information
# ----------------------------------------------------
st.subheader("📁 Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", filtered_df.shape[0])

with col2:
    st.metric("Columns", filtered_df.shape[1])

st.write("### Column Names")

st.write(list(df.columns))

with st.expander("View Dataset Preview"):
    st.dataframe(filtered_df.head())