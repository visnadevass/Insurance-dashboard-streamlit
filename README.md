# 📊 Insurance Website Analytics Dashboard

## 📖 Project Overview

This project presents an interactive **Insurance Website Analytics Dashboard** developed using **Python**, **Streamlit**, and **Plotly**.

The dashboard analyses website traffic, customer behaviour, marketing performance, and insurance policy sales. It allows users to explore business performance interactively through filters, charts, KPIs, and summary statistics.

---

## 🎯 Project Objectives

The dashboard was developed to:

- Analyse website traffic across marketing channels.
- Compare performance across device categories.
- Identify the most profitable marketing channels.
- Monitor insurance quotes and policy purchases.
- Present key business KPIs.
- Provide interactive data exploration through filters.

---

## 📂 Dataset

The dataset contains aggregated website analytics information including:

- Marketing Channel
- Device Category
- Users
- Pages per Session
- Average Session Duration
- Insurance Policies Purchased
- Revenue
- Insurance Quotes

**Dataset Size**

- Rows: **1,933**
- Columns: **8**

---

## 📊 Dashboard Features

### 📈 Key Performance Indicators (KPIs)

- Total Users
- Total Revenue
- Total Insurance Quotes
- Total Policies Purchased
- Average Revenue per Record
- Average Session Duration

---

### 📊 Marketing Channel Analysis

- Users by Marketing Channel
- Revenue by Marketing Channel
- Policies Purchased by Marketing Channel

---

### 📱 Device Category Analysis

- Users by Device
- Revenue by Device
- Policies Purchased by Device
- Policy Conversion Rate

---

### 📈 Customer Behaviour Analysis

- Revenue Distribution
- Pages per Session vs Revenue
- Users vs Insurance Quotes
- Correlation Heatmap

---

### 📋 Additional Features

- Interactive filters
- Download filtered dataset
- Marketing summary table
- Business insights
- Responsive Streamlit dashboard

---

## 💡 Key Business Insights

The analysis identified several important business findings:

- Organic Search generated the highest website traffic.
- Aggregators generated the highest revenue.
- Aggregators achieved the highest number of insurance policy purchases.
- Mobile devices generated the highest revenue and user activity.
- Revenue is highly right-skewed.
- Insurance policy purchases have the strongest relationship with revenue.
- Website traffic alone does not guarantee higher revenue.

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Matplotlib
- Seaborn

---

## 📁 Project Structure

```
InsuranceDashboard/
│
├── Data/
│   ├── Original/
│   └── Cleaned/
│
├── Images/
│
├── Notebooks/
│
├── app.py
├── utils.py
├── requirements.txt
└── README.md
```

---

## ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/visnadevass/Insurance-dashboard-streamlit.git
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 👨‍💻 Developer

**Visna Devass**

Data Science Project Lifecycle

Informatics Institute of Technology (IIT)

University of Westminster

---

## 📄 License

This project was developed for academic purposes.