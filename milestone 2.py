# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('/mnt/data/healthcare-dataset-stroke-data.csv')

# Display dataset information
print("Dataset Info:")
print(data.info())
print("\nFirst 5 Rows:")
print(data.head())

# ----------- Data Visualization -----------

# Visualize Residence_type distribution
sns.countplot(data['Residence_type'])
plt.title("Distribution of Residence Type")
plt.show()

# Visualize work_type distribution
sns.countplot(data['work_type'])
plt.title("Distribution of Work Type")
plt.show()

# Visualize smoking_status distribution
sns.countplot(data['smoking_status'])
plt.title("Distribution of Smoking Status")
plt.show()

# Visualize avg_glucose_level distribution
sns.histplot(data['avg_glucose_level'], kde=True)
plt.title("Average Glucose Level Distribution")
plt.show()

# ----------- Data Cleaning and Encoding -----------

# Handle missing values in BMI column
data['bmi'].fillna(data['bmi'].mean(), inplace=True)

# Encode categorical columns
label_encoder = LabelEncoder()
data['Residence_type'] = label_encoder.fit_transform(data['Residence_type'])
data['work_type'] = label_encoder.fit_transform(data['work_type'])
data['smoking_status'] = label_encoder.fit_transform(data['smoking_status'])
data['gender'] = label_encoder.fit_transform(data['gender'])

# Drop irrelevant columns
data = data.drop(['id'], axis=1)

# Save the preprocessed dataset
data.to_csv('preprocessed_stroke_data.csv', index=False)
print("Preprocessed dataset saved as 'preprocessed_stroke_data.csv'.")