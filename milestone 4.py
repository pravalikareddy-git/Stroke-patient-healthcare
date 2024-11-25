import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'your_dataset.csv' with your dataset's file path)
df = pd.read_csv('your_dataset.csv')

# Step 1: Basic Data Exploration

# Describe the dataset for numerical columns
print("Describe (Numerical):")
print(df.describe())

# Describe the dataset for categorical/object columns
print("\nDescribe (Object):")
print(df.describe(include=[object]))

# Info to get basic info about the dataframe (data types, non-null counts, etc.)
print("\nInfo:")
print(df.info())

# Shape of the dataset (number of rows and columns)
print("\nShape of the dataset:")
print(df.shape)

# Step 2: Data Quality Check (Null Values and Unique Values)

# Finding unique values for each column
print("\nUnique values in each column:")
print(df.nunique())

# Checking for missing (null) values
print("\nNull values in each column:")
print(df.isnull().sum())

# Percentage of missing values for each column
print("\nPercentage of missing values:")
print(df.isnull().mean() * 100)

# Step 3: Dealing with Missing Values

# Strategy for handling missing values (example: drop rows with missing target variable or use median for numerical columns)
# Here we'll use the median for numerical columns and drop rows with missing target column
df.fillna(df.median(), inplace=True)  # Impute numerical columns with median
df.dropna(subset=['target_column'], inplace=True)  # Drop rows where target column is null (adjust as needed)

# Step 4: Data Encoding (Specific Tasks)

# 1. Convert 'Residence_type' column to 0 (rural) and 1 (urban)
df['Residence_type'] = df['Residence_type'].map({'Rural': 0, 'Urban': 1})

# 2. Convert 'work_type' column to separate columns (Never_worked, Private, Self-employed)
df['Never_worked'] = (df['work_type'] == 'Never_worked').astype(int)
df['Private'] = (df['work_type'] == 'Private').astype(int)
df['Self_employed'] = (df['work_type'] == 'Self-employed').astype(int)

# Drop the original 'work_type' column
df.drop(columns=['work_type'], inplace=True)

# 3. Convert 'smoking_status' to 3 or 4 separate columns
df['smoking_status_Unknown'] = (df['smoking_status'] == 'Unknown').astype(int)
df['smoking_status_never_smoked'] = (df['smoking_status'] == 'never smoked').astype(int)
df['smoking_status_smokes'] = (df['smoking_status'] == 'smokes').astype(int)

# Drop the original 'smoking_status' column
df.drop(columns=['smoking_status'], inplace=True)

# 4. Create a new variable (dataset) for the data model, dropping the transformed columns
df_model = df.copy()  # Save the transformed dataset to be used for modeling
df_model.drop(columns=['Residence_type', 'work_type'], inplace=True)

# Step 5: Visualizing the Data (Min 5 Graphs)

# 1. Distribution of a numerical column (e.g., Age)
plt.figure(figsize=(8,6))
sns.histplot(df['Age'], kde=True, bins=20)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 2. Correlation heatmap of numerical features
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# 3. Distribution of 'smoking_status' categories (after encoding)
smoking_status_counts = df[['smoking_status_Unknown', 'smoking_status_never_smoked', 'smoking_status_smokes']].sum()
smoking_status_counts.plot(kind='bar', figsize=(8,6), color=['skyblue', 'orange', 'green'])
plt.title('Smoking Status Counts')
plt.ylabel('Count')
plt.show()

# 4. Boxplot for Age vs. Target (Assuming 'target_column' is the column of interest)
plt.figure(figsize=(8,6))
sns.boxplot(x='target_column', y='Age', data=df)
plt.title('Age vs Target Column')
plt.xlabel('Target')
plt.ylabel('Age')
plt.show()

# 5. Pie chart for Residence_type distribution
plt.figure(figsize=(8,6))
df['Residence_type'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
plt.title('Distribution of Residence Type')
plt.ylabel('')
plt.show()

# Final Output: Save the transformed dataset
df_model.to_csv('transformed_data.csv', index=False)