def predict_ecg(record_name, model, scaler, data_dir='mitdb', window_size=200):
    """
    Analyse un enregistrement ECG et prédit les anomalies avec le modèle fourni.
    """
    import wfdb
    import numpy as np
    import matplotlib.pyplot as plt
    from collections import Counter

    half_window = window_size // 2

    # Chargement du signal et des annotations
    record = wfdb.rdrecord(os.path.join(data_dir, record_name))
    annotation = wfdb.rdann(os.path.join(data_dir, record_name), 'atr')
    signal = record.p_signal[:, 0]

    X_pred = []
    labels = []
    positions = []

    for i, pos in enumerate(annotation.sample):
        if pos - half_window < 0 or pos + half_window > len(signal):
            continue
        beat_type = annotation.symbol[i]
        label = 0 if beat_type == 'N' else 1
        window = signal[pos - half_window : pos + half_window]
        X_pred.append(window)
        labels.append(label)
        positions.append(pos)

    # Prétraitement (scaling)
    X_pred = np.array(X_pred)
    X_scaled = scaler.transform(X_pred)

    # Prédiction
    y_hat = (model.predict(X_scaled) > 0.5).astype(int).flatten()

    # Statistiques
    count = Counter(y_hat)
    print(f"\n📊 Résumé des prédictions pour l’enregistrement {record_name} :")
    print(f"  - Normaux   : {count[0]} battements")
    print(f"  - Anormaux  : {count[1]} battements")
    print(f"  - Total     : {len(y_hat)} battements analysés")

    # Affichage courbe
    plt.figure(figsize=(12, 3))
    plt.plot(signal, alpha=0.6, label='Signal ECG')
    anomaly_positions = [positions[i] for i, pred in enumerate(y_hat) if pred == 1]
    plt.scatter(anomaly_positions, [signal[p] for p in anomaly_positions],
                color='red', label='Anomalies détectées', s=10)
    plt.title(f"Détection automatique des anomalies – Record {record_name}")
    plt.xlabel("Échantillons")
    plt.ylabel("Amplitude (mV)")
    plt.legend()
    plt.grid()
    plt.show()
