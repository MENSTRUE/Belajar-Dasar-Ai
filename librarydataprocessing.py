# ==============================
# Library Pengolahan Data
# ==============================

# 1️⃣ Pandas: manipulasi data
import pandas as pd

# Membuat DataFrame dari dictionary
data = {
    'Nama': ['Wafa', 'Budi', 'Siti'],
    'Usia': [28, 35, 22],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya']
}

df = pd.DataFrame(data)
print("=== DataFrame Pandas ===")
print(df)

# 2️⃣ NumPy: array multidimensi
import numpy as np

matriks = np.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print("\n=== Array NumPy ===")
print(matriks)

# 3️⃣ Matplotlib: visualisasi data (plot garis)
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o', color='blue')
plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.grid(True)
plt.show()

# 4️⃣ Seaborn: visualisasi histogram
import seaborn as sns

# Load dataset bawaan Seaborn
tips = sns.load_dataset('tips')

plt.figure(figsize=(6,4))
sns.histplot(tips['total_bill'], kde=True, color='green')
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()
