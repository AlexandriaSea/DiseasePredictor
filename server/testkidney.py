import pickle

with open("top_features.pkl", "rb") as f:
    top_features_kidney = pickle.load(f)

print("Top Features for Kidney Prediction:", top_features_kidney)
