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