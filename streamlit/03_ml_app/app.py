# This is a Streamlit application for machine learning model training and evaluation.
import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.svm import SVR, SVC
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np
import pickle
from sklearn.compose import ColumnTransformer

def preprocess_data(X, y, problem):
    # Fill missing values
    imp = IterativeImputer()
    X_imputed = pd.DataFrame(imp.fit_transform(X), columns=X.columns)
    
    # Identify categorical columns
    categorical_cols = X_imputed.select_dtypes(include=['object', 'category']).columns

    # Create a ColumnTransformer to apply encoding to categorical columns
    if categorical_cols.any():
        label_encoders = {col: LabelEncoder() for col in categorical_cols}
        for col in categorical_cols:
            X_imputed[col] = label_encoders[col].fit_transform(X_imputed[col])

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)
    
    return X_scaled, y

# Function to train and evaluate models
def train_and_evaluate(X_train, X_test, y_train, y_test, model):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return predictions

# Main application function
def main():
    st.title("Machine Learning Application")
    st.write("Welcome to the machine learning application. This app allows you to train and evaluate different machine learning models on your dataset.")

    # Initialize data variable
    data = None  # Ensures data is defined at the start

    # Data upload or example data selection
    data_source = st.sidebar.selectbox("Do you want to upload data or use example data?", ["Upload", "Example"])
    
    if data_source == "Upload":
        uploaded_file = st.sidebar.file_uploader("Choose a file", type=['csv', 'xlsx', 'tsv'])
        if uploaded_file is not None:
            if uploaded_file.type == "text/csv":
                data = pd.read_csv(uploaded_file)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                data = pd.read_excel(uploaded_file)
            elif uploaded_file.type == "text/tab-separated-values":
                data = pd.read_csv(uploaded_file, sep='\t')
    else:
        dataset_name = st.sidebar.selectbox("Select a dataset", ["titanic", "tips", "iris"])
        data = sns.load_dataset(dataset_name)

    # Ensure data is available before checking `.empty`
    if data is not None and not data.empty:
        st.write("Data Head:", data.head())
        st.write("Data Shape:", data.shape)
        st.write("Data Description:", data.describe())
        st.write("Column Names:", data.columns.tolist())

        # Select features and target
        features = st.multiselect("Select features columns", data.columns.tolist())
        target = st.selectbox("Select target column", data.columns.tolist())
        problem_type = st.selectbox("Problem Type", ["Classification", "Regression"])
        
        if features and target and problem_type:
            X = data[features]
            y = data[target]
            
            st.write(f"You have selected a {problem_type} problem.")
            
            # Button to start analysis
            if st.button("Run Analysis"):
                # Pre-process data
                X_processed, y_processed = preprocess_data(X, y, problem_type)
                
                # Train-test split
                test_size = st.slider("Select test split size", 0.1, 0.5, 0.2)
                X_train, X_test, y_train, y_test = train_test_split(X_processed, y_processed, test_size=test_size, random_state=42)

                # Model selection based on problem type
                model_options = ['Linear Regression', 'Decision Tree', 'Random Forest', 'SVM'] if problem_type == 'Regression' else ['Decision Tree', 'Random Forest', 'SVM']
                selected_model = st.sidebar.selectbox("Select model", model_options)
                
                # Initialize model
                model = {
                    'Linear Regression': LinearRegression(),
                    'Decision Tree': DecisionTreeRegressor() if problem_type == 'Regression' else DecisionTreeClassifier(),
                    'Random Forest': RandomForestRegressor() if problem_type == 'Regression' else RandomForestClassifier(),
                    'SVM': SVR() if problem_type == 'Regression' else SVC()
                }[selected_model]

                # Train and evaluate model
                predictions = train_and_evaluate(X_train, X_test, y_train, y_test, model)
                
                # Display results
                st.write("Model training and evaluation complete.")

if __name__ == "__main__":
    main()