import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
import joblib

data = pd.read_csv("training_data.csv")
X = data[["subject_knowledge", "engagement", "management", "preparedness", "professionalism"]]
y = data["recommended_training"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "training_model.pkl")
print("Random Forest model trained and saved as training_model.pkl")
