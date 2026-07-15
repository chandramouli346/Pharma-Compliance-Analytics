import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# PHARMA COMPLIANCE ANALYTICS PROJECT
# ==========================================================

# ==========================================================
# STEP 1 : Read Cleaned Dataset
# ==========================================================

df = pd.read_csv("data/pharma_compliance_cleaned.csv")

print("=" * 70)
print("        PHARMA COMPLIANCE ANALYTICS")
print("=" * 70)

print("\nFirst 5 Records")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

# ==========================================================
# STEP 2 : Key Performance Indicators (KPIs)
# ==========================================================

print("\n" + "=" * 70)
print("KEY PERFORMANCE INDICATORS (KPIs)")
print("=" * 70)

total_cases = len(df)
average_risk = df["Risk_Score"].mean()
critical_cases = (df["Severity"] == "Critical").sum()
open_capa = (df["CAPA_Status"] == "Open").sum()
closed_capa = (df["CAPA_Status"] == "Closed").sum()

print(f"\nTotal Compliance Cases : {total_cases}")
print(f"Average Risk Score     : {average_risk:.2f}")
print(f"Critical Cases         : {critical_cases}")
print(f"Open CAPA              : {open_capa}")
print(f"Closed CAPA            : {closed_capa}")

# ==========================================================
# STEP 3 : Department-wise Compliance Cases
# ==========================================================

department_counts = df["Department"].value_counts()

plt.figure(figsize=(8,5))

department_counts.plot(
    kind="bar",
    color="steelblue",
    edgecolor="black"
)

plt.title("Department-wise Compliance Cases", fontsize=14)
plt.xlabel("Department")
plt.ylabel("Number of Cases")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

plt.show()

# ==========================================================
# STEP 4 : Severity Distribution
# ==========================================================

severity_counts = df["Severity"].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    severity_counts,
    labels=severity_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Severity Distribution", fontsize=14)

plt.axis("equal")

plt.show()

# ==========================================================
# STEP 5 : CAPA Status Distribution
# ==========================================================

capa_counts = df["CAPA_Status"].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    capa_counts,
    labels=capa_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("CAPA Status Distribution", fontsize=14)

plt.axis("equal")

plt.show()

# ==========================================================
# STEP 6 : Root Cause Analysis
# ==========================================================

root_counts = df["Root_Cause"].value_counts()

plt.figure(figsize=(10,6))

root_counts.plot(
    kind="bar",
    color="purple",
    edgecolor="black"
)

plt.title("Root Cause Analysis", fontsize=14)
plt.xlabel("Root Cause")
plt.ylabel("Number of Cases")
plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

plt.show()

# ==========================================================
# STEP 7 : Plant-wise Compliance Cases
# ==========================================================

plant_counts = df["Plant"].value_counts()

plt.figure(figsize=(8,5))

plant_counts.plot(
    kind="bar",
    color="green",
    edgecolor="black"
)

plt.title("Plant-wise Compliance Cases", fontsize=14)
plt.xlabel("Plant")
plt.ylabel("Number of Cases")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

plt.show()

# ==========================================================
# STEP 8 : Product-wise Compliance Cases
# ==========================================================

product_counts = df["Product"].value_counts()

plt.figure(figsize=(8,5))

product_counts.plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Product-wise Compliance Cases", fontsize=14)
plt.xlabel("Product")
plt.ylabel("Number of Cases")
plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

plt.show()

# ==========================================================
# STEP 9 : Monthly Compliance Trend
# ==========================================================

df["Audit_Date"] = pd.to_datetime(df["Audit_Date"])

df["Month"] = df["Audit_Date"].dt.to_period("M").astype(str)

monthly_cases = df.groupby("Month").size()

plt.figure(figsize=(12,6))

monthly_cases.plot(
    kind="line",
    marker="o",
    linewidth=2
)

plt.title("Monthly Compliance Trend", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Number of Compliance Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()

# ==========================================================
# END OF EDA
# ==========================================================

print("\n" + "=" * 70)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nCharts Generated Successfully:")
print("1. Department-wise Compliance Cases")
print("2. Severity Distribution")
print("3. CAPA Status Distribution")
print("4. Root Cause Analysis")
print("5. Plant-wise Compliance Cases")
print("6. Product-wise Compliance Cases")
print("7. Monthly Compliance Trend")

print("\nNext Module : Flask Dashboard Development")