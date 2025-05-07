import numpy as np

# Paramètres
window_size = 200  # taille de la fenêtre autour du battement
half_window = window_size // 2
signal = record.p_signal[:, 0]  # un seul canal

X = []
y = []

for i, pos in enumerate(annotation.sample):
    if pos - half_window < 0 or pos + half_window > len(signal):
        continue  # éviter les débordements

    beat_type = annotation.symbol[i]

    # Label : 0 = normal (N), 1 = anormal (tout autre)
    label = 0 if beat_type == 'N' else 1

    # Fenêtre centrée autour du battement
    segment = signal[pos - half_window : pos + half_window]
    X.append(segment)
    y.append(label)

X = np.array(X)
y = np.array(y)

print(f"{X.shape[0]} fenêtres extraites.")
print(f"Dimensions d'une fenêtre : {X.shape[1]} points")
print(f"Répartition des labels : {np.unique(y, return_counts=True)}")