# ==============================
# Library File Management
# ==============================

# 1️⃣ OS: mengelola file dan direktori
import os

print("=== OS Library ===")
# Mendapatkan Current Working Directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Membuat folder baru (jika belum ada)
folder_baru = "contoh_folder"
if not os.path.exists(folder_baru):
    os.makedirs(folder_baru)
    print(f"Folder '{folder_baru}' berhasil dibuat.")
else:
    print(f"Folder '{folder_baru}' sudah ada.")

# ==============================
# 2️⃣ JSON: Serialisasi data ke format text
# ==============================
import json

print("\n=== JSON Library ===")
# Contoh JSON (string)
json_str = '{ "nama":"Buchori", "umur":22, "kota":"New York"}'

# Parsing JSON ke dictionary Python
data_dict = json.loads(json_str)
print("Umur dari JSON:", data_dict["umur"])

# Menyimpan dictionary Python ke file JSON
with open("data.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4)
    print("Data berhasil disimpan ke 'data.json'.")

# Membaca kembali file JSON
with open("data.json", "r") as json_file:
    data_baca = json.load(json_file)
    print("Data dari file JSON:", data_baca)

# ==============================
# 3️⃣ Pickle: Serialisasi data Python (binary)
# ==============================
import pickle

print("\n=== Pickle Library ===")
# Contoh dictionary
contoh_dictionary = {1: "6", 2: "2", 3: "f"}

# Menyimpan dictionary ke file pickle
with open("dict.pickle", "wb") as pickle_keluar:
    pickle.dump(contoh_dictionary, pickle_keluar)
    print("Dictionary berhasil disimpan ke 'dict.pickle'.")

# Membaca kembali file pickle
with open("dict.pickle", "rb") as pickle_masuk:
    data_pickle = pickle.load(pickle_masuk)
    print("Dictionary dari file pickle:", data_pickle)
