# Affiche quelques fenêtres avec leurs labels
import matplotlib.pyplot as plt

for i in range(5):
    plt.plot(X[i])
    plt.title(f"Label : {'Normal' if y[i]==0 else 'Anormal'}")
    plt.show()