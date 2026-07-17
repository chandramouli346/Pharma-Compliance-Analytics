# 💊 Pharma Compliance Analytics Dashboard

An interactive **Pharmaceutical Regulatory Compliance Analytics Dashboard** developed using **Python, Streamlit, Pandas, Plotly, and Machine Learning**.

This project analyzes pharmaceutical compliance data to identify compliance trends, risk patterns, deviations, root causes, CAPA performance, and management-level insights.

The project also includes an experimental machine learning module to evaluate the feasibility of predicting high-risk compliance cases.

---

## 📌 Project Overview

Pharmaceutical companies must continuously monitor regulatory compliance, deviations, Corrective and Preventive Actions (CAPA), and operational risks.

This project transforms pharmaceutical compliance data into an interactive analytics dashboard that helps users monitor compliance performance, identify risk areas, analyze deviations, evaluate CAPA performance, and generate management-level insights.

The dashboard provides:

- Compliance KPI monitoring
- Management decision insights
- Department-wise compliance analysis
- Severity analysis
- CAPA status monitoring
- Root cause analysis
- Plant and product analysis
- Deviation analysis
- Risk analysis
- CAPA closure performance analysis
- Monthly compliance trend analysis
- Dynamic dashboard filtering
- Downloadable compliance analytics report
- Experimental machine learning risk prediction analysis

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze pharmaceutical compliance data
- Monitor important compliance KPIs
- Identify departments with higher compliance risk
- Monitor critical compliance cases
- Track open and closed CAPA cases
- Identify frequently occurring deviation types
- Analyze major root causes of compliance issues
- Compare compliance performance across departments
- Compare compliance cases across plants and products
- Measure CAPA closure performance
- Analyze monthly compliance trends
- Generate management-level decision insights
- Generate downloadable compliance reports
- Explore machine learning techniques for compliance risk prediction

---

## 📊 Dashboard Features

### 📌 Compliance Overview

The dashboard displays key compliance KPIs:

- Total Compliance Cases
- Average Risk Score
- Critical Cases
- Open CAPA Cases
- Closed CAPA Cases

These KPI cards provide a quick overview of the current compliance situation.

---

## 🎯 Management Decision Insights

The dashboard automatically generates management-level insights based on the currently filtered data.

The insights include:

- Highest Risk Department
- Department Risk Score
- Top Root Cause
- Most Common Deviation
- Slowest CAPA Closure Department
- Average CAPA Closure Time

These insights help management quickly identify areas that may require additional attention and corrective action.

---

## 🏢 Department & Severity Analysis

This section provides:

- Department-wise Compliance Cases
- Severity Distribution

The analysis helps users understand which departments have the highest number of compliance cases and how cases are distributed across different severity levels.

---

## 🔍 CAPA & Root Cause Analysis

This section includes:

- CAPA Status Distribution
- Root Cause Analysis

The CAPA analysis helps monitor corrective and preventive action status.

The root cause analysis helps identify the major causes contributing to pharmaceutical compliance issues.

---

## 🏭 Plant & Product Analysis

This section analyzes:

- Plant-wise Compliance Cases
- Product-wise Compliance Cases

It helps compare compliance activity across manufacturing locations and pharmaceutical product categories.

---

## ⚠️ Deviation Analysis

The dashboard analyzes different types of pharmaceutical compliance deviations.

Deviation categories may include:

- Cleaning
- Equipment
- Validation
- Documentation
- SOP
- Calibration

This analysis helps identify frequently occurring deviation categories that may require further investigation.

---

## 🚨 Risk Analysis

The dashboard calculates and visualizes the average risk score for each department.

This helps identify departments with comparatively higher compliance risk and supports management prioritization.

---

## ⏱️ CAPA Performance Analysis

The CAPA Performance section analyzes:

- Average Case Closure Time
- Department-wise Average Closure Time

This helps management identify departments where compliance cases may take longer to resolve.

---

## 📈 Monthly Compliance Trend

The dashboard provides a monthly compliance trend chart based on audit dates.

This helps users monitor changes in the number of compliance cases over time and identify possible increases or decreases in compliance activity.

---

## 🔎 Dynamic Filters

The dashboard includes interactive sidebar filters for:

- Company
- Department
- Plant
- Severity

All KPIs, charts, management insights, and downloadable reports dynamically update based on the selected filters.

---

## 📄 Downloadable Compliance Analytics Report

The dashboard allows users to generate and download a Word-based compliance analytics report.

The report includes:

- Executive Summary
- Key Performance Indicators
- Management Decision Insights
- Business Insights
- Recommendations

The report is generated dynamically using the currently filtered dashboard data.

---

## 🤖 Machine Learning Risk Prediction Analysis

An experimental machine learning module was developed to explore the prediction of high-risk pharmaceutical compliance cases.

### Prediction Target

A binary `High_Risk` target was created using the `Risk_Score` column:

- Risk Score >= 70 → High Risk (`1`)
- Risk Score < 70 → Not High Risk (`0`)

### Input Features

The following features were selected for model training:

- Company
- Department
- Plant
- Deviation Type
- Severity
- Root Cause
- Product

The `Risk_Score` column was not included as an input feature because the prediction target was created from `Risk_Score`. Including it would cause data leakage.

### Data Preprocessing

The selected categorical features were converted into numerical features using one-hot encoding.

The dataset was then divided into:

- 80% Training Data
- 20% Testing Data

A stratified train-test split was used to maintain the target class distribution.

### Machine Learning Models

Two classification algorithms were evaluated:

1. Logistic Regression
2. Random Forest Classifier

### Model Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Classification Report
- Confusion Matrix
- ROC-AUC Score

### Model Limitation

The experimental analysis showed limited predictive relationships between the available input features and the high-risk target.

The Logistic Regression model achieved an ROC-AUC score close to random classification, indicating that the selected features did not contain sufficient predictive information for reliable high-risk classification.

Therefore, the machine learning component is presented as a **prototype and feasibility analysis** rather than a production-ready pharmaceutical compliance risk prediction system.

A real-world implementation would require validated historical pharmaceutical regulatory and compliance data with meaningful relationships between predictive features and compliance outcomes.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Data Analysis

- Pandas

### Data Visualization

- Plotly

### Dashboard Development

- Streamlit

### Machine Learning

- Scikit-learn
- Logistic Regression
- Random Forest Classifier

### Report Generation

- python-docx

### Styling

- HTML
- CSS

### Version Control

- Git
- GitHub

---

## 📁 Project Structure

```text
Pharma-Compliance-Analytics/
│
├── dashboard.py
├── prediction_model.py
├── requirements.txt
├── README.md
│
├── data/
│   └── pharma_compliance_cleaned.csv
│
└── styles/
    └── style.css
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/chandramouli346/Pharma-Compliance-Analytics.git
```

### 2. Navigate to the Project Folder

```bash
cd Pharma-Compliance-Analytics
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard

```bash
streamlit run dashboard.py
```

The Streamlit application will open in your web browser.

---

## 🤖 Run the Machine Learning Analysis

To run the experimental high-risk prediction analysis:

```bash
python prediction_model.py
```

The terminal will display model evaluation results for Logistic Regression and Random Forest.

---

## 📦 Requirements

The main Python libraries required for this project are:

```text
streamlit
pandas
plotly
scikit-learn
python-docx
```

---

## 💡 Key Business Insights

The dashboard can help identify:

- Departments with higher compliance risk
- Major causes of pharmaceutical compliance deviations
- Frequently occurring deviation types
- Critical compliance cases requiring attention
- CAPA cases that remain open
- Departments with slower case closure times
- Differences in compliance activity across plants
- Product categories with higher numbers of compliance cases
- Monthly changes in compliance activity

---

## ✅ Recommendations

Based on compliance analytics, organizations can consider:

- Conducting periodic GMP and SOP training
- Improving CAPA monitoring and follow-up
- Strengthening preventive maintenance programs
- Investigating recurring root causes
- Prioritizing critical and high-risk compliance cases
- Monitoring departments with longer closure times
- Improving documentation and process controls
- Using continuous compliance monitoring to reduce future risk

---

## 🚀 Future Enhancements

Future improvements may include:

- Integration with validated real-world pharmaceutical regulatory datasets
- Improved machine learning models using historical compliance data
- Interactive compliance risk prediction
- Predictive compliance risk scoring
- Automated compliance alerts
- Real-time data integration
- Advanced anomaly detection
- Role-based dashboard access
- PDF and Excel report generation
- Cloud database integration
- Model monitoring and retraining

---

## ⚠️ Disclaimer

This project is developed for **educational, portfolio, and analytics demonstration purposes**.

The machine learning component is experimental and should not be used for real-world pharmaceutical regulatory, quality, safety, or compliance decisions without validated data, appropriate model validation, and review by qualified domain experts.

---


## ⭐ Project Summary

This project demonstrates an end-to-end data analytics workflow:

**Data Cleaning → Data Analysis → Interactive Dashboard → Management Insights → Compliance Reporting → Machine Learning Feasibility Analysis**

The project combines data analytics, visualization, dashboard development, reporting, and machine learning to demonstrate how pharmaceutical compliance data can be transformed into useful business and management insights.