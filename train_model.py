import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# ======================
# DATASET POV PENONTON
# ======================
data = {
    "genre_match":        [5, 4, 3, 2, 1, 5, 4, 2, 3, 1],
    "expectation":        [5, 4, 4, 3, 2, 5, 3, 2, 4, 1],
    "trailer_quality":    [5, 4, 3, 3, 2, 5, 4, 2, 3, 1],
    "actor_favorite":     [5, 4, 2, 3, 1, 5, 4, 2, 3, 1],
    "plot_complexity":    [1, 2, 3, 4, 5, 1, 2, 4, 3, 5],
    "watching_mood":      [5, 4, 3, 3, 2, 5, 4, 2, 3, 1],

    # 0 = puas, 1 = biasa, 2 = kecewa
    "satisfaction":       [0, 0, 1, 1, 2, 0, 1, 2, 1, 2]
}

df = pd.DataFrame(data)

X = df.drop("satisfaction", axis=1)
y = df["satisfaction"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model viewer satisfaction berhasil dibuat 🍿")