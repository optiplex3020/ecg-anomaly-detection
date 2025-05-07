import wfdb
import os
import matplotlib.pyplot as plt
from collections import Counter

# Dossier contenant les enregistrements
data_dir = 'mitdb'

# Choix d’un enregistrement (ex. : 100)
record_name = '100'

# Lecture du signal et des annotations
record = wfdb.rdrecord(os.path.join(data_dir, record_name))
annotation = wfdb.rdann(os.path.join(data_dir, record_name), 'atr')

# Affichage du signal ECG (lead 1 seulement)
plt.figure(figsize=(15, 3))
plt.plot(record.p_signal[:,0], label='Lead I')
plt.title(f'Signal ECG - Record {record_name}')
plt.xlabel('Samples')
plt.ylabel('Amplitude (mV)')
plt.grid()
plt.legend()
plt.show()

# Statistiques sur les annotations
labels = annotation.symbol
count = Counter(labels)
print("Distribution des battements :")
for k, v in count.items():
    print(f"{k}: {v} fois")