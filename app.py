import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

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

# ----------------------------------------------------
# Dashboard Information
# ----------------------------------------------------

st.sidebar.title("📊 Dashboard Information")

st.sidebar.markdown("""
**Project**

Insurance Website Analytics Dashboard

**Module**

Data Science Project Lifecycle

**Developer**

Visna De Vass

**Dataset**

Insurance Website Analytics Dataset
""")

st.sidebar.divider()

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

# Download filtered dataset
st.sidebar.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_insurance_data.csv",
    mime="text/csv"
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

st.plotly_chart(fig_users, width="stretch")
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

st.plotly_chart(fig_revenue, width="stretch")
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

st.plotly_chart(fig_policy, width="stretch")
st.info(
    """
**Business Insight**

Aggregator channels recorded the highest number of insurance policy purchases, making them the most valuable acquisition channel.
"""
)



# ----------------------------------------------------
# Device Category Analysis
# ----------------------------------------------------
st.divider()

st.header("📱 Device Category Performance")

# Users by Device
device_users = (
    filtered_df
    .groupby("Device Category")["Users"]
    .sum()
    .reset_index()
)

fig_device_users = px.bar(
    device_users,
    x="Device Category",
    y="Users",
    color="Users",
    title="Users by Device Category",
    text_auto=True
)

st.plotly_chart(fig_device_users, width="stretch")

st.info("""
**Business Insight**

Mobile devices generated the highest number of users, showing that most visitors access the insurance website using smartphones.
""")

# Revenue by Device
device_revenue = (
    filtered_df
    .groupby("Device Category")["Revenue"]
    .sum()
    .reset_index()
)

fig_device_revenue = px.bar(
    device_revenue,
    x="Device Category",
    y="Revenue",
    color="Revenue",
    title="Revenue by Device Category",
    text_auto=".2f"
)

st.plotly_chart(fig_device_revenue, width="stretch")

st.info("""
**Business Insight**

Mobile devices generated the highest total revenue, indicating that mobile users contribute significantly to business performance.
""")

# Policies Purchased by Device
device_policy = (
    filtered_df
    .groupby("Device Category")["TotalNumberOfInsurancePoliciesPurchaed"]
    .sum()
    .reset_index()
)

fig_device_policy = px.bar(
    device_policy,
    x="Device Category",
    y="TotalNumberOfInsurancePoliciesPurchaed",
    color="TotalNumberOfInsurancePoliciesPurchaed",
    title="Policies Purchased by Device Category",
    text_auto=True
)

st.plotly_chart(fig_device_policy, width="stretch")

st.info("""
**Business Insight**

Mobile users purchased the largest number of insurance policies, making mobile the strongest device category for overall sales.
""")



# ----------------------------------------------------
# Conversion Rate by Device
# ----------------------------------------------------

st.subheader("📈 Policy Conversion Rate by Device")

conversion = (
    filtered_df
    .groupby("Device Category")
    .agg({
        "Users":"sum",
        "TotalNumberOfInsurancePoliciesPurchaed":"sum"
    })
)

conversion["Conversion Rate (%)"] = (
    conversion["TotalNumberOfInsurancePoliciesPurchaed"]
    / conversion["Users"]
) * 100

conversion = conversion.reset_index()

fig_conversion = px.bar(
    conversion,
    x="Device Category",
    y="Conversion Rate (%)",
    color="Conversion Rate (%)",
    text_auto=".2f",
    title="Policy Conversion Rate by Device"
)

st.plotly_chart(fig_conversion, width="stretch")

st.info("""
**Business Insight**

The conversion rate compares insurance policies purchased with the number of users for each device category.

This helps identify which device converts visitors into customers most efficiently rather than simply attracting the highest traffic.
""")



# ----------------------------------------------------
# Customer Behaviour Analysis
# ----------------------------------------------------

st.divider()

st.header("📈 Customer Behaviour Analysis")

fig_hist = px.histogram(
    filtered_df,
    x="Revenue",
    nbins=30,
    title="Revenue Distribution"
)

st.plotly_chart(fig_hist, width="stretch")

st.info("""
**Business Insight**

Revenue is positively skewed. Most observations generate little or no revenue,
while a small number contribute exceptionally high revenue.

This indicates that only a relatively small proportion of customer sessions
generate substantial business value.
""")


fig_scatter = px.scatter(
    filtered_df,
    x="Pages / Session",
    y="Revenue",
    color="Marketing Channel",
    title="Pages per Session vs Revenue"
)

st.plotly_chart(fig_scatter, width="stretch")

st.info("""
**Business Insight**

There is little relationship between the number of pages viewed and revenue.

Browsing more pages does not necessarily result in purchasing an insurance policy,
suggesting that website engagement alone is not enough to increase sales.
""")



fig_quotes = px.scatter(
    filtered_df,
    x="Users",
    y="TotalNumberOfInsuranceQuotes",
    color="Device Category",
    title="Users vs Insurance Quotes"
)

st.plotly_chart(fig_quotes, width="stretch")

st.info("""
**Business Insight**

There is a strong positive relationship between website users and insurance quote requests.

As more visitors access the website, the number of insurance quotes generally increases,
although this does not always translate into policy purchases.
""")



st.subheader("🔥 Correlation Matrix")

numeric_df = filtered_df.select_dtypes(include="number")

corr = numeric_df.corr()

fig, ax = plt.subplots(figsize=(10,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="Blues",
    fmt=".2f",
    ax=ax
)

st.pyplot(fig)

st.info("""
**Business Insight**

The strongest relationship is between Policies Purchased and Revenue,
confirming that policy sales are the primary driver of business income.

Users and Insurance Quotes also show a strong positive relationship,
indicating that increased website traffic leads to more quote requests.

Most remaining correlations are weak, suggesting that simply increasing
website engagement does not automatically increase revenue.
""")



st.divider()

st.header("📋 Marketing Channel Summary")
summary = (
    filtered_df
    .groupby("Marketing Channel")
    .agg({
        "Users":"sum",
        "Revenue":"sum",
        "TotalNumberOfInsurancePoliciesPurchaed":"sum",
        "TotalNumberOfInsuranceQuotes":"sum"
    })
    .sort_values(
        by="Revenue",
        ascending=False
    )
    .reset_index()
)
st.dataframe(summary, width="stretch")

st.info("""
**Business Insight**

Aggregators generated the highest revenue despite attracting fewer users than Organic Search.

This suggests that aggregator websites deliver higher-quality leads and better customer conversion.
""")

st.divider()

st.caption(
    "Insurance Website Analytics Dashboard | "
    "Developed using Python, Streamlit and Plotly"
)
