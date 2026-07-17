# ==========================================================
# PHARMA COMPLIANCE - HIGH RISK PREDICTION MODEL
# ==========================================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)


# ==========================================================
# 1. LOAD DATASET
# ==========================================================

df = pd.read_csv(
    "data/pharma_compliance_cleaned.csv"
)

print("Dataset Shape:", df.shape)


# ==========================================================
# 2. CREATE TARGET VARIABLE
# ==========================================================

# Risk Score >= 70 = High Risk (1)
# Risk Score < 70 = Not High Risk (0)

df["High_Risk"] = (
    df["Risk_Score"] >= 70
).astype(int)

print("\nHigh Risk Distribution:")

print(
    df["High_Risk"].value_counts()
)


# ==========================================================
# 3. SELECT FEATURES AND TARGET
# ==========================================================

features = [
    "Company",
    "Department",
    "Plant",
    "Deviation_Type",
    "Severity",
    "Root_Cause",
    "Product"
]

target = "High_Risk"

X = df[features]

y = df[target]

print("\nSelected Features:")

print(
    X.columns.tolist()
)


# ==========================================================
# 4. ENCODE CATEGORICAL FEATURES
# ==========================================================

# Convert categorical columns into numeric columns

X_encoded = pd.get_dummies(
    X,
    drop_first=True
)

print(
    "\nEncoded Data Shape:",
    X_encoded.shape
)


# ==========================================================
# 5. TRAIN-TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(
    "\nTraining Data Shape:",
    X_train.shape
)

print(
    "Testing Data Shape:",
    X_test.shape
)


# ==========================================================
# 6. LOGISTIC REGRESSION MODEL
# ==========================================================

logistic_model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced",
    random_state=42
)

# Train Logistic Regression
logistic_model.fit(
    X_train,
    y_train
)

# Make predictions
y_pred_logistic = logistic_model.predict(
    X_test
)

# Get prediction probabilities
y_prob_logistic = logistic_model.predict_proba(
    X_test
)[:, 1]


# ==========================================================
# 7. EVALUATE LOGISTIC REGRESSION
# ==========================================================

print(
    "\n===== Logistic Regression Results ====="
)

print(
    "Accuracy:",
    round(
        accuracy_score(
            y_test,
            y_pred_logistic
        ),
        4
    )
)

print(
    "Precision:",
    round(
        precision_score(
            y_test,
            y_pred_logistic
        ),
        4
    )
)

print(
    "Recall:",
    round(
        recall_score(
            y_test,
            y_pred_logistic
        ),
        4
    )
)

print(
    "F1 Score:",
    round(
        f1_score(
            y_test,
            y_pred_logistic
        ),
        4
    )
)

print(
    "ROC-AUC Score:",
    round(
        roc_auc_score(
            y_test,
            y_prob_logistic
        ),
        4
    )
)

print(
    "\nConfusion Matrix:"
)

print(
    confusion_matrix(
        y_test,
        y_pred_logistic
    )
)

print(
    "\nClassification Report:"
)

print(
    classification_report(
        y_test,
        y_pred_logistic
    )
)


# ==========================================================
# 8. RANDOM FOREST MODEL
# ==========================================================

random_forest_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight="balanced",
    random_state=42
)

# Train Random Forest
random_forest_model.fit(
    X_train,
    y_train
)

# Make predictions
y_pred_rf = random_forest_model.predict(
    X_test
)

# Get prediction probabilities
y_prob_rf = random_forest_model.predict_proba(
    X_test
)[:, 1]


# ==========================================================
# 9. EVALUATE RANDOM FOREST
# ==========================================================

print(
    "\n===== Random Forest Results ====="
)

print(
    "Accuracy:",
    round(
        accuracy_score(
            y_test,
            y_pred_rf
        ),
        4
    )
)

print(
    "Precision:",
    round(
        precision_score(
            y_test,
            y_pred_rf
        ),
        4
    )
)

print(
    "Recall:",
    round(
        recall_score(
            y_test,
            y_pred_rf
        ),
        4
    )
)

print(
    "F1 Score:",
    round(
        f1_score(
            y_test,
            y_pred_rf
        ),
        4
    )
)

print(
    "ROC-AUC Score:",
    round(
        roc_auc_score(
            y_test,
            y_prob_rf
        ),
        4
    )
)

print(
    "\nConfusion Matrix:"
)

print(
    confusion_matrix(
        y_test,
        y_pred_rf
    )
)

print(
    "\nClassification Report:"
)

print(
    classification_report(
        y_test,
        y_pred_rf
    )
)