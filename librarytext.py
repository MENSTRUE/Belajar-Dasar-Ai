# ==============================
# Library Text Processing
# ==============================

# Modul string bawaan Python
import string  # Opsional, karena sebagian fungsi string sudah built-in

# Contoh variabel string
teks = "hello world"

# 1️⃣ Upper: Ubah semua huruf menjadi kapital
teks_upper = teks.upper()
print("Upper:", teks_upper)  # Output: HELLO WORLD

# 2️⃣ Lower: Ubah semua huruf menjadi kecil
teks_lower = teks.lower()
print("Lower:", teks_lower)  # Output: hello world

# 3️⃣ Split: Pisahkan teks berdasarkan spasi
teks_split = teks.split()
print("Split:", teks_split)  # Output: ['hello', 'world']

# 4️⃣ Title: Jadikan setiap awal kata kapital
teks_title = teks.title()
print("Title:", teks_title)  # Output: Hello World

# 5️⃣ Zfill: Tambahkan nol di awal string
angka = "42"
angka_zfill = angka.zfill(5)  # Panjang total 5 karakter
print("Zfill:", angka_zfill)  # Output: 00042

# ==============================
# Regex (Regular Expression)
# ==============================

import re  # Harus di-import untuk pakai regex

# Contoh pola regex:
# ^a     -> Awal string harus 'a'
# ...    -> Diikuti 3 karakter apa saja
# s$     -> Akhir string harus 's'
pola = '^a...s$'
string_tes = 'abyss'

# Mencocokkan string dengan pola regex
hasil = re.match(pola, string_tes)

if hasil:
    print("Regex: Pencarian berhasil.")
else:
    print("Regex: Pencarian gagal.")

# ==============================
# Contoh Regex lain: validasi email sederhana
# ==============================

email = "contoh@email.com"
pola_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Pola sederhana untuk email

if re.match(pola_email, email):
    print("Email valid")
else:
    print("Email tidak valid")
