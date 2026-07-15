import streamlit as st
import pandas as pd
import plotly.express as px
from docx import Document
from docx.shared import Pt
from io import BytesIO
from datetime import datetime

st.set_page_config(
    page_title="Pharma Compliance Dashboard",
    page_icon="💊",
    layout="wide"
)

st.markdown("""
<h1 style='text-align:center;'>
💊 Pharma Compliance Analytics Dashboard
</h1>

<h4 style='text-align:center; color:gray;'>
Compliance Monitoring | Data Analytics | Business Intelligence
</h4>
""", unsafe_allow_html=True)

st.divider()
# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/pharma_compliance_cleaned.csv")

# ==========================================
# Sidebar Filters
# ==========================================

st.sidebar.header("🔍 Filters")

company = st.sidebar.selectbox(
    "Select Company",
    ["All"] + sorted(df["Company"].unique().tolist())
)

department = st.sidebar.selectbox(
    "Select Department",
    ["All"] + sorted(df["Department"].unique().tolist())
)

plant = st.sidebar.selectbox(
    "Select Plant",
    ["All"] + sorted(df["Plant"].unique().tolist())
)

severity = st.sidebar.selectbox(
    "Select Severity",
    ["All"] + sorted(df["Severity"].unique().tolist())
)


# ==========================================
# Apply Filters
# ==========================================

filtered_df = df.copy()

if company != "All":
    filtered_df = filtered_df[
        filtered_df["Company"] == company
    ]

if department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == department
    ]

if plant != "All":
    filtered_df = filtered_df[
        filtered_df["Plant"] == plant
    ]

if severity != "All":
    filtered_df = filtered_df[
        filtered_df["Severity"] == severity
    ]


# ==========================================
# KPI Calculations
# ==========================================

total_cases = len(filtered_df)

average_risk = (
    round(filtered_df["Risk_Score"].mean(), 2)
    if total_cases > 0 else 0
)

critical_cases = (
    filtered_df["Severity"] == "Critical"
).sum()

open_capa = (
    filtered_df["CAPA_Status"] == "Open"
).sum()

closed_capa = (
    filtered_df["CAPA_Status"] == "Closed"
).sum()
# ==========================================
# KPI Cards
# ==========================================

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("📋 Total Cases", f"{total_cases:,}")
col2.metric("⚠ Average Risk", f"{average_risk:.2f}")
col3.metric("🚨 Critical Cases", f"{critical_cases:,}")
col4.metric("📂 Open CAPA", f"{open_capa:,}")
col5.metric("✅ Closed CAPA", f"{closed_capa:,}")
# ==========================================
# Department & Severity
# ==========================================

st.divider()

col1, col2 = st.columns(2)

# Department Chart

with col1:

    st.subheader("📊 Department-wise Compliance Cases")

    department_counts = (
        filtered_df["Department"]
        .value_counts()
        .reset_index()
    )

    department_counts.columns = ["Department", "Cases"]

    fig_department = px.bar(
        department_counts,
        x="Department",
        y="Cases",
        text="Cases",
        color_discrete_sequence=["#4F81BD"],
        template="plotly_white"
    )

    fig_department.update_traces(textposition="outside")

    fig_department.update_layout(
        height=420,
        title_x=0.5
    )

    st.plotly_chart(fig_department, width="stretch")

# Severity Chart
with col2:

    st.subheader("🥧 Severity Distribution")

    severity_counts = (
        filtered_df["Severity"]
        .value_counts()
        .reset_index()
    )

    severity_counts.columns = ["Severity", "Cases"]

    fig_severity = px.pie(
        severity_counts,
        names="Severity",
        values="Cases",
        hole=0.4,
        template="plotly_white"
    )

    fig_severity.update_layout(
        height=420,
        title="Severity Distribution",
        title_x=0.5
    )

    st.plotly_chart(fig_severity, width="stretch")

# ==========================================
# CAPA & Root Cause
# ==========================================

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("📋 CAPA Status")

    capa_counts = (
        filtered_df["CAPA_Status"]
        .value_counts()
        .reset_index()
    )

    capa_counts.columns = ["CAPA Status", "Cases"]

    fig_capa = px.pie(
        capa_counts,
        names="CAPA Status",
        values="Cases",
        hole=0.4,
        template="plotly_white"
    )

    fig_capa.update_layout(
        height=420,
        title_x=0.5
    )

    st.plotly_chart(fig_capa, width="stretch")

with col2:

    st.subheader("📊 Root Cause Analysis")

    root_counts = (
        filtered_df["Root_Cause"]
        .value_counts()
        .reset_index()
    )

    root_counts.columns = ["Root Cause", "Cases"]

    fig_root = px.bar(
        root_counts,
        x="Root Cause",
        y="Cases",
        text="Cases",
        color_discrete_sequence=["#2E8B57"],
        template="plotly_white"
    )

    fig_root.update_traces(textposition="outside")

    fig_root.update_layout(
        height=420,
        title_x=0.5
    )

    st.plotly_chart(fig_root, width="stretch")
# ==========================================
# Plant & Product
# ==========================================

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏭 Plant-wise Compliance Cases")

    plant_counts = (
        filtered_df["Plant"]
        .value_counts()
        .reset_index()
    )

    plant_counts.columns = ["Plant", "Cases"]

    fig_plant = px.bar(
        plant_counts,
        x="Plant",
        y="Cases",
        text="Cases",
        color_discrete_sequence=["#F39C12"],
        template="plotly_white"
    )

    fig_plant.update_traces(textposition="outside")

    fig_plant.update_layout(
        height=420,
        title_x=0.5
    )

    st.plotly_chart(fig_plant, width="stretch")

with col2:

    st.subheader("💊 Product-wise Compliance Cases")

    product_counts = (
        filtered_df["Product"]
        .value_counts()
        .reset_index()
    )

    product_counts.columns = ["Product", "Cases"]

    fig_product = px.bar(
        product_counts,
        x="Product",
        y="Cases",
        text="Cases",
        color_discrete_sequence=["#8E44AD"],
        template="plotly_white"
    )

    fig_product.update_traces(textposition="outside")

    fig_product.update_layout(
        height=420,
        title_x=0.5
    )

    st.plotly_chart(fig_product, width="stretch")
# ==========================================
# Monthly Compliance Trend
# ==========================================

st.divider()
st.subheader("📈 Monthly Compliance Trend")

filtered_df = filtered_df.copy()

filtered_df["Audit_Date"] = pd.to_datetime(filtered_df["Audit_Date"])

monthly_cases = (
    filtered_df
    .groupby(filtered_df["Audit_Date"].dt.to_period("M"))
    .size()
    .reset_index(name="Cases")
)

monthly_cases["Audit_Date"] = monthly_cases["Audit_Date"].astype(str)

fig_monthly = px.line(
    monthly_cases,
    x="Audit_Date",
    y="Cases",
    markers=True,
    title="Monthly Compliance Trend",
    template="plotly_white"
)
fig_monthly.update_traces(
    line_color="#3498DB",
    line_width=3,
    marker=dict(size=8)

)

fig_monthly.update_layout(
    height=500,
    title_x=0.5
)


st.plotly_chart(fig_monthly, width="stretch")

# ==========================================
# Create Word Report
# ==========================================

document = Document()

document.add_heading("Pharma Compliance Analytics Report", 1)
document.add_paragraph("Prepared By : Madharapu Chandramouli")
document.add_paragraph("")
document.add_paragraph(f"Generated On : {datetime.now().strftime('%d-%m-%Y %H:%M')}")

document.add_heading("Dashboard Summary", level=2)

document.add_paragraph(f"Total Compliance Cases : {total_cases}")
document.add_paragraph(f"Average Risk Score : {average_risk}")
document.add_paragraph(f"Critical Cases : {critical_cases}")
document.add_paragraph(f"Open CAPA : {open_capa}")
document.add_paragraph(f"Closed CAPA : {closed_capa}")

document.add_heading("Applied Filters", level=2)

document.add_paragraph(f"Company : {company}")
document.add_paragraph(f"Department : {department}")
document.add_paragraph(f"Plant : {plant}")
document.add_paragraph(f"Severity : {severity}")

document.add_heading("Business Insights", level=2)

document.add_paragraph(
    "• This report summarizes the current compliance cases after applying the selected filters."
)

document.add_paragraph(
    "• High-risk and critical deviations should be reviewed immediately."
)

document.add_paragraph(
    "• Departments with more deviations require additional monitoring."
)

document.add_heading("Recommendations", level=2)

document.add_paragraph("• Improve CAPA closure process.")
document.add_paragraph("• Conduct periodic GMP training.")
document.add_paragraph("• Review recurring root causes.")
document.add_paragraph("• Increase internal compliance audits.")

buffer = BytesIO()

document.save(buffer)

buffer.seek(0)


st.download_button(
    label="📄 Download Word Report",
    data=buffer,
    file_name="Pharma_Compliance_Report.docx",
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    width="stretch"
)
st.success("Dashboard loaded successfully. Apply filters and download the report.")