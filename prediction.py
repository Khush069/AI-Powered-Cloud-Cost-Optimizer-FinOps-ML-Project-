from sklearn.linear_model import LinearRegression
import numpy as np

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