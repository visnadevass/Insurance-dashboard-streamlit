import streamlit as st
import pandas as pd
import plotly.express as px

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

selected_channels = st.sidebar.multiselect(
    "Select Marketing Channel",
    options=sorted(df["Marketing Channel"].unique()),
    default=sorted(df["Marketing Channel"].unique())
)

selected_devices = st.sidebar.multiselect(
    "Select Device Category",
    options=sorted(df["Device Category"].unique()),
    default=sorted(df["Device Category"].unique())
)

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
# KPI Cards
# ----------------------------------------------------
st.subheader("📈 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Total Users", f"{filtered_df['Users'].sum():,}")

with col2:
    st.metric("💰 Total Revenue", f"${filtered_df['Revenue'].sum():,.2f}")

with col3:
    st.metric("📄 Total Quotes", f"{filtered_df['TotalNumberOfInsuranceQuotes'].sum():,}")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "📑 Policies Purchased",
        f"{filtered_df['TotalNumberOfInsurancePoliciesPurchaed'].sum():,}"
    )

with col5:
    st.metric(
        "📈 Average Revenue",
        f"${filtered_df['Revenue'].mean():.2f}"
    )

with col6:
    st.metric(
        "⏱ Avg Session Duration",
        f"{filtered_df['Avg. Session Duration'].mean():.2f} sec"
    )

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

st.write(list(filtered_df.columns))

with st.expander("View Dataset Preview"):
    st.dataframe(filtered_df.head())



# ----------------------------------------------------
# Marketing Channel Analysis
# ----------------------------------------------------
st.divider()

st.header("📊 Marketing Channel Performance")

# Users by Marketing Channel
users_channel = (
    filtered_df
    .groupby("Marketing Channel")["Users"]
    .sum()
    .reset_index()
)

fig_users = px.bar(
    users_channel,
    x="Marketing Channel",
    y="Users",
    color="Users",
    title="Users by Marketing Channel",
    text_auto=True
)

st.plotly_chart(fig_users, use_container_width=True)
st.info(
    """
**Business Insight**

Organic Search attracted the largest number of users, indicating strong visibility in search engines.

However, high website traffic does not necessarily translate into the highest revenue.
"""
)

# Revenue by Marketing Channel
revenue_channel = (
    filtered_df
    .groupby("Marketing Channel")["Revenue"]
    .sum()
    .reset_index()
)

fig_revenue = px.bar(
    revenue_channel,
    x="Marketing Channel",
    y="Revenue",
    color="Revenue",
    title="Revenue by Marketing Channel",
    text_auto=".2f"
)

st.plotly_chart(fig_revenue, use_container_width=True)
st.info(
    """
**Business Insight**

Aggregators generated the highest revenue despite not attracting the largest number of users.

This suggests that aggregator websites attract more qualified customers who are more likely to purchase insurance policies.
"""
)

# Policies Purchased by Marketing Channel
policies_channel = (
    filtered_df
    .groupby("Marketing Channel")["TotalNumberOfInsurancePoliciesPurchaed"]
    .sum()
    .reset_index()
)

fig_policy = px.bar(
    policies_channel,
    x="Marketing Channel",
    y="TotalNumberOfInsurancePoliciesPurchaed",
    color="TotalNumberOfInsurancePoliciesPurchaed",
    title="Policies Purchased by Marketing Channel",
    text_auto=True
)

st.plotly_chart(fig_policy, use_container_width=True)
st.info(
    """
**Business Insight**

Aggregator channels recorded the highest number of insurance policy purchases, making them the most valuable acquisition channel.
"""
)