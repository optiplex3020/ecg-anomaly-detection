import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix

# Évaluation
loss, acc = model.evaluate(X_test, y_test)
print(f"Accuracy sur les données de test : {acc:.2f}")

# Matrice de confusion
y_pred = (model.predict(X_test) > 0.5).astype("int32")
print(classification_report(y_test, y_pred))

# Courbe d'apprentissage
plt.plot(history.history['accuracy'], label='Train acc')
plt.plot(history.history['val_accuracy'], label='Val acc')
plt.title("Courbe d'apprentissage")
plt.xlabel("Épochs")
plt.ylabel("Accuracy")
plt.legend()
plt.grid()
plt.show()