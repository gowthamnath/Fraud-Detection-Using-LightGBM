Fraud Detection using LightGBM
Overview

This project focuses on detecting fraudulent financial transactions from a dataset containing transaction details. It uses data preprocessing, exploratory data analysis (EDA), SMOTE for handling class imbalance, and a LightGBM classifier to predict fraudulent transactions.

The model achieves high accuracy due to class balancing and feature engineering.

Dataset

Filename: Fraud Detection.csv

Number of rows: 1,272,524

Number of columns: 11

Columns used for modeling:

type (transaction type)

amount (transaction amount)

oldbalanceOrg (initial balance of origin account)

newbalanceOrig (new balance of origin account)

oldbalanceDest (initial balance of destination account)

newbalanceDest (new balance of destination account)

isFraud (target variable, 0 = non-fraud, 1 = fraud)

Dropped columns: step, nameOrig, nameDest, isFlaggedFraud (not relevant for prediction)

Libraries Used

Data handling: pandas, numpy

Visualization: matplotlib, seaborn

Preprocessing: sklearn.preprocessing.LabelEncoder, imblearn.over_sampling.SMOTE

Modeling: lightgbm.LGBMClassifier

Evaluation: sklearn.metrics.classification_report

Model saving: joblib

Steps Performed
1. Data Loading

Loaded the CSV dataset into a pandas DataFrame.

Displayed first 5 rows and checked shape and null values.

2. Exploratory Data Analysis (EDA)

Checked summary statistics of numerical columns using df.describe().

Visualized popular transaction types with a bar chart.

Checked fraud occurrence by transaction type.

Observed that TRANSFER and CASH_OUT are more prone to fraud.

Calculated overall fraud percentage: 0.13%, indicating class imbalance.

3. Data Preprocessing

Dropped irrelevant columns.

Encoded type column using LabelEncoder into Type_Encoded.

Split dataset into features X and target y.

4. Handling Class Imbalance

Used SMOTE (Synthetic Minority Oversampling Technique) to balance the dataset.

Verified class distribution after resampling.

5. Train-Test Split

Split resampled data into training and testing sets (80% train, 20% test).

6. Model Training

Used LightGBM classifier with:

Boosting type: gbdt

Objective: binary

Learning rate: 0.05

Number of leaves: 31

Maximum depth: 3

Estimators: 200

Unbalanced class handling: is_unbalance=True

Trained on X_train and y_train.

7. Model Evaluation

Predicted on X_test.

Classification report metrics:

Accuracy: 99%

Precision, Recall, F1-score: all ~0.99

Model performs very well due to SMOTE balancing.

8. Streamlit App

After building and saving the LightGBM model (lgb_model.pkl), a Streamlit web app was created to allow users to interactively predict fraudulent transactions.
