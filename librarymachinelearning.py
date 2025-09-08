# ==============================
# Library Machine Learning - Contoh Lengkap (Fix)
# ==============================

# 1️⃣ Scikit-learn (KNN pada dataset iris)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

print("=== Scikit-learn ===")
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print("Akurasi KNN:", accuracy_score(y_test, y_pred))

# ==============================
# 2️⃣ TensorFlow (Regresi linear sederhana)
import tensorflow as tf
import numpy as np

print("\n=== TensorFlow ===")
X_tf = np.array([1, 2, 3, 4], dtype=float)
y_tf = np.array([3, 5, 7, 9], dtype=float)

# Gunakan Input layer untuk mencegah warning
model_tf = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1)
])

model_tf.compile(optimizer='sgd', loss='mean_squared_error')
model_tf.fit(X_tf, y_tf, epochs=500, verbose=0)

# Prediksi harus 2D array
prediksi_tf = model_tf.predict(np.array([[10.0]]))
print("Prediksi TensorFlow untuk x=10:", prediksi_tf[0][0])

# ==============================
# 3️⃣ PyTorch (Regresi linear sederhana)
import torch
import torch.nn as nn

print("\n=== PyTorch ===")
X_pt = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_pt = torch.tensor([[3.0], [5.0], [7.0], [9.0]])

model_pt = nn.Linear(in_features=1, out_features=1)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model_pt.parameters(), lr=0.01)

for epoch in range(500):
    optimizer.zero_grad()
    outputs = model_pt(X_pt)
    loss = criterion(outputs, y_pt)
    loss.backward()
    optimizer.step()

x_test_pt = torch.tensor([[10.0]])
y_pred_pt = model_pt(x_test_pt)
print("Prediksi PyTorch untuk x=10:", y_pred_pt.item())
