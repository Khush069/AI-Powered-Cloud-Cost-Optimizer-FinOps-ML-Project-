def detect_anomalies(df):
    threshold = df['cost'].mean() + 2 * df['cost'].std()
    anomalies = df[df['cost'] > threshold]
    return anomalies