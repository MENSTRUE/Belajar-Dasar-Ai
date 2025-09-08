# ==============================
# Library Matematika (math)
# ==============================

import math  # Import modul math bawaan Python

# 1️⃣ Akar kuadrat
angka = 25
akar = math.sqrt(angka)
print(f"Akar kuadrat dari {angka} adalah {akar}")  # Output: 5.0

# 2️⃣ Konstanta pi
print("Nilai pi:", math.pi)  # Output: 3.141592653589793

# 3️⃣ Fungsi eksponensial (e^x)
x = 2
print(f"e^{x} =", math.exp(x))  # Output: 7.38905609893065

# 4️⃣ Fungsi logaritma natural
y = 10
print(f"ln({y}) =", math.log(y))  # Output: 2.302585092994046

# 5️⃣ Fungsi trigonometri
sudut_derajat = 90
sudut_radian = math.radians(sudut_derajat)  # Konversi derajat ke radian
print(f"sin({sudut_derajat}°) =", math.sin(sudut_radian))  # Output: 1.0
print(f"cos({sudut_derajat}°) =", math.cos(sudut_radian))  # Output: 6.123233995736766e-17 (≈0)

# 6️⃣ Pembulatan
angka_desimal = 3.7
print(f"Pembulatan {angka_desimal} ke bawah:", math.floor(angka_desimal))  # 3
print(f"Pembulatan {angka_desimal} ke atas:", math.ceil(angka_desimal))    # 4

# 7️⃣ Fungsi nilai mutlak
negatif = -15
print(f"Nilai mutlak dari {negatif} =", math.fabs(negatif))  # 15.0
