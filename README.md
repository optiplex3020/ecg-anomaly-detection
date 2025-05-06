# ECG Anomaly Detection – IUT3 FISA

Ce projet a été réalisé dans le cadre de la veille technologique (R6-VT) à l’IUT3 – FISA.

## 🧠 Objectif

Détecter automatiquement les anomalies dans des signaux ECG (électrocardiogrammes) en utilisant des données réelles issues de la base MIT-BIH. Le système repose sur un modèle de machine learning entraîné à partir de segments centrés sur chaque battement cardiaque.

## 🧰 Technologies utilisées

- Python 3
- Google Colab / Jupyter
- Keras & TensorFlow
- `wfdb` pour la lecture des signaux ECG
- Matplotlib / NumPy / Scikit-learn

## 🔍 Contenu

- `ecg_project.ipynb` : notebook complet (chargement, prétraitement, entraînement, prédiction)
- `rapport.pdf` : rapport synthétique du projet
- Fonction `predict_ecg(record_name)` incluse pour appliquer le modèle sur de nouveaux patients

## 📦 Dataset

Les données proviennent de la base publique :  
[MIT-BIH Arrhythmia Database – PhysioNet](https://physionet.org/content/mitdb/1.0.0/)

## 💡 Cas d’usage

Un système de prédiction embarqué dans un dispositif Holter ECG peut identifier automatiquement les battements anormaux chez un patient et alerter un professionnel de santé.

---

✅ Projet réalisé par : Dylan ELENGA
📅 Année universitaire 2024–2025
