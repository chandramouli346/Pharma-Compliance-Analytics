import pandas as pd

# ==========================================================
# PHARMA COMPLIANCE ANALYTICS PROJECT
# Module 1 : Data Understanding & Basic Data Cleaning
# Author : Madharapu Chandramouli
# ==========================================================

# ==========================================================
# STEP 1 : Read Dataset
# ==========================================================

df = pd.read_csv("data/pharma_compliance_dataset_10000.csv")

# ==========================================================
# STEP 2 : Dataset Overview
# ==========================================================

print("=" * 70)
print("        PHARMA COMPLIANCE DATASET OVERVIEW")
print("=" * 70)

print("\nFirst 10 Records")
print(df.head(10))

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# ==========================================================
# STEP 3 : Remove Duplicate Rows
# ==========================================================

print("\n" + "=" * 70)
print("             DUPLICATE ROW CLEANING")
print("=" * 70)

print("\nDataset Shape Before Cleaning")
print(df.shape)

print("\nDuplicate Rows Before Cleaning")
print(df.duplicated().sum())

# Remove duplicate rows and reset index
df = df.drop_duplicates().reset_index(drop=True)

print("\nDataset Shape After Cleaning")
print(df.shape)

print("\nDuplicate Rows After Cleaning")
print(df.duplicated().sum())

# ==========================================================
# STEP 4 : Department Cleaning
# ==========================================================

print("\n" + "=" * 70)
print("             DEPARTMENT COLUMN CLEANING")
print("=" * 70)

print("\nDepartment Values Before Cleaning")
print(df["Department"].unique())

# Remove leading and trailing spaces
df["Department"] = df["Department"].str.strip()

# Convert text to Title Case
df["Department"] = df["Department"].str.title()

# Correct spelling mistakes
df["Department"] = df["Department"].replace({
    "Prodction": "Production"
})

# Correct abbreviations
df["Department"] = df["Department"].replace({
    "Qa": "QA",
    "Qc": "QC"
})

print("\nDepartment Values After Cleaning")
print(df["Department"].unique())

# ==========================================================
# STEP 5 : Severity Cleaning
# ==========================================================

print("\n" + "=" * 70)
print("              SEVERITY COLUMN CLEANING")
print("=" * 70)

print("\nSeverity Values Before Cleaning")
print(df["Severity"].unique())

# Remove extra spaces
df["Severity"] = df["Severity"].str.strip()

# Convert text to Title Case
df["Severity"] = df["Severity"].str.title()

# Correct spelling mistakes
df["Severity"] = df["Severity"].replace({
    "Hgh": "High"
})

print("\nSeverity Values After Cleaning")
print(df["Severity"].unique())

# ==========================================================
# STEP 6 : Risk Score Cleaning
# ==========================================================

print("\n" + "=" * 70)
print("               RISK SCORE CLEANING")
print("=" * 70)

print("\nRisk Score Summary Before Cleaning")
print(df["Risk_Score"].describe())

# Display invalid values
invalid_scores = df[
    (df["Risk_Score"] < 1) |
    (df["Risk_Score"] > 100)
]

print("\nSample Invalid Risk Scores")
print(invalid_scores[["Compliance_ID", "Risk_Score"]].head())

# Keep only valid Risk Scores (1-100)
df = df[
    (df["Risk_Score"] >= 1) &
    (df["Risk_Score"] <= 100)
].reset_index(drop=True)

print("\nRisk Score Summary After Cleaning")
print(df["Risk_Score"].describe())

print("\nDataset Shape After Risk Score Cleaning")
print(df.shape)

# ==========================================
# Date Column Cleaning
# ==========================================

print("\n" + "=" * 70)
print("DATE COLUMN CLEANING")
print("=" * 70)

print("\nData Types Before Conversion")
print(df[["Audit_Date", "Closure_Date"]].dtypes)

# Convert to datetime
df["Audit_Date"] = pd.to_datetime(df["Audit_Date"], errors="coerce")
df["Closure_Date"] = pd.to_datetime(df["Closure_Date"], errors="coerce")

print("\nData Types After Conversion")
print(df[["Audit_Date", "Closure_Date"]].dtypes)

print("\nMissing Dates")
print(df[["Audit_Date", "Closure_Date"]].isnull().sum())

# ==========================================================
# STEP 8 : Missing Value Handling
# ==========================================================

print("\n" + "=" * 70)
print("MISSING VALUE HANDLING")
print("=" * 70)

print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

# Fill missing values in Remarks
df["Remarks"] = df["Remarks"].fillna("No Remarks")

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# ==========================================================
# STEP 9 : Save Cleaned Dataset
# ==========================================================

df.to_csv("data/pharma_compliance_cleaned.csv", index=False)

print("\n" + "=" * 70)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nCleaned Dataset Saved Successfully")
print("File : data/pharma_compliance_cleaned.csv")

print("\nFinal Dataset Shape")
print(df.shape)

print("\nData Cleaning Module Completed Successfully!")