import joblib
import pandas as pd

model = joblib.load("model.pkl")


def preprocess(data: dict):
    df = pd.DataFrame([data])

    expected = [
        "genre_match",
        "expectation",
        "trailer_quality",
        "actor_favorite",
        "plot_complexity",
        "watching_mood"
    ]

    return df.reindex(columns=expected)


def predict(data: dict):
    try:
        X = preprocess(data)
        pred = model.predict(X)[0]

        label_map = {
            0: "Puas 😍",
            1: "Biasa saja 😐",
            2: "Kecewa 😡"
        }

        return {
            "status": "success",
            "prediction": int(pred),
            "label": label_map[pred]
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }