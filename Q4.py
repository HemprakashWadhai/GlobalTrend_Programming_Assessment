#4. Using pandas, write a Python function to clean and preprocess a given DataFrame, which involves handling missing values, normalizing numerical columns, and encoding categorical columns.
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Example DataFrame
data = {
    'numeric_col1': [1, 2, None, 4, 5],
    'numeric_col2': [10, 20, 30, None, 50],
    'category_col': ['A', 'B', None, 'C', 'B'],
    'text_col': ['foo', 'bar', None, 'baz', 'qux']
}

df = pd.DataFrame(data)

def preprocess_data(df):
    # Handle missing values
    df = handle_missing_values(df)
    
    # Normalize numerical columns
    df = normalize_numerical_columns(df)
    
    # Encode categorical columns
    df = encode_categorical_columns(df)
    
    return df

def handle_missing_values(df):
    # Fill missing values in numerical columns with mean
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
    
    # Fill missing values in categorical columns with mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
    
    return df

def normalize_numerical_columns(df):
    # Initialize StandardScaler
    scaler = StandardScaler()
    
    # Normalize numerical columns
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    return df

def encode_categorical_columns(df):
    # Encode categorical columns using one-hot encoding
    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    return df

# Display the original DataFrame
print("Original DataFrame:")
print(df)
print()

# Preprocess the DataFrame
df_preprocessed = preprocess_data(df)

# Display the preprocessed DataFrame
print("Preprocessed DataFrame:")
print(df_preprocessed)
