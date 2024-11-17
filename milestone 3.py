# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report

# Load preprocessed dataset
data = pd.read_csv('preprocessed_stroke_data.csv')

# Split dataset into features (X) and target (y)
X = data.drop('stroke', axis=1)
y = data['stroke']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ----------- Build and Evaluate Models -----------

# Define models
models = {
    "Linear Regression": LinearRegression(),
    "Logistic Regression": LogisticRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Lasso Regression": Lasso(alpha=0.1)
}

# Train and evaluate models
for name, model in models.items():
    model.fit(X_train, y_train)
    
    if name in ["Linear Regression", "Ridge Regression", "Lasso Regression"]:
        # Regression Metrics
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"{name} - Mean Squared Error (MSE): {mse:.4f}")
    else:
        # Classification Metrics
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"{name} - Accuracy: {acc:.4f}")
        print("Classification Report:")
        print(classification_report(y_test, y_pred))