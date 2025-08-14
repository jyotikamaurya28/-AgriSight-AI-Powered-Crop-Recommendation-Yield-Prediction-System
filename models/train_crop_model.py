# models/train_crop_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load processed data
df = pd.read_csv("processed_crop_data.csv")

# Features and label
X = df.drop("label", axis=1)
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "models/crop_recommendation_model.pkl")

print("✅ Crop recommendation model trained and saved as 'crop_recommendation_model.pkl'")
