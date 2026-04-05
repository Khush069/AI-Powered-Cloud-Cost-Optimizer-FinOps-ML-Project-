import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# -------------------------------
# Load Data
# -------------------------------
def load_data():
    df = pd.read_csv("data/cost_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

# -------------------------------
# Anomaly Detection
# -------------------------------
def detect_anomalies(df):
    threshold = df['cost'].mean() + 2 * df['cost'].std()
    anomalies = df[df['cost'] > threshold]
    return anomalies

# -------------------------------
# Cost Prediction
# -------------------------------
def predict_cost(df):
    df = df.copy()
    df['day'] = range(len(df))

    X = df[['day']]
    y = df['cost']

    model = LinearRegression()
    model.fit(X, y)

    future_day = np.array([[len(df) + 1]])
    prediction = model.predict(future_day)

    return prediction[0]

# -------------------------------
# Recommendations
# -------------------------------
def generate_recommendations(anomalies):
    recommendations = []

    for _, row in anomalies.iterrows():
        if row['service'] == 'Compute':
            recommendations.append("Check idle VMs or downsize instances")
        elif row['service'] == 'Storage':
            recommendations.append("Review unused storage or snapshots")
        else:
            recommendations.append(f"Investigate cost spike in {row['service']}")

    return recommendations

# -------------------------------
# Run Project
# -------------------------------
if __name__ == "__main__":
    df = load_data()

    print("\n📊 Raw Data:\n", df)

    anomalies = detect_anomalies(df)
    print("\n🚨 Anomalies:\n", anomalies)

    prediction = predict_cost(df)
    print(f"\n📈 Predicted Next Cost: {prediction}")

    recs = generate_recommendations(anomalies)
    print("\n💡 Recommendations:")
    for r in recs:
        print("-", r)