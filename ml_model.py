import numpy as np
from sklearn.ensemble import RandomForestClassifier

X = np.array([[1],[2],[3],[4],[5],[7],[9],[12],[15],[20]])


y = np.array([0,0,0,0,0,1,1,2,2,2])


model = RandomForestClassifier()
model.fit(X, y)

def predict_threat(time_gap):
    prediction = model.predict([[time_gap]])[0]

    if prediction == 0:
        return "GREEN"
    elif prediction == 1:
        return "YELLOW"
    else:
        return "RED"
