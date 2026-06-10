# Viewer Satisfaction Prediction API

## Deskripsi

API ini digunakan untuk memprediksi tingkat kepuasan penonton terhadap sebuah film berdasarkan beberapa faktor seperti kesesuaian genre, ekspektasi, kualitas trailer, kesukaan terhadap aktor, kompleksitas alur cerita, dan kondisi mood penonton.

Output prediksi terdiri dari:

* 0 = Puas 😍
* 1 = Biasa 😐
* 2 = Kecewa 😡

---

## Instalasi Dependensi

Install library yang dibutuhkan:

```bash
pip install fastapi uvicorn pandas scikit-learn joblib
```

---

## Menjalankan Model

Buat model terlebih dahulu:

```bash
python train_model.py
```

Perintah tersebut akan menghasilkan file:

```text
model.pkl
```

---

## Menjalankan API

```bash
uvicorn main:app --reload
```

API dapat diakses melalui:

```text
http://127.0.0.1:8000/docs
```

---

## Endpoint

### POST /predict

Digunakan untuk melakukan prediksi tingkat kepuasan penonton.

### Contoh Request

```json
{
  "genre_match": 5,
  "expectation": 4,
  "trailer_quality": 5,
  "actor_favorite": 5,
  "plot_complexity": 2,
  "watching_mood": 5
}
```

### Contoh Response Sukses

```json
{
  "status": "success",
  "prediction": 0,
  "label": "Puas 😍"
}
```

### Contoh Response Error

```json
{
  "status": "error",
  "message": "..."
}
```
