import argparse
from datetime import datetime

# ==============================
# Membuat parser argumen
# ==============================
parser = argparse.ArgumentParser(description="Program sapaan berdasarkan nama dan tanggal lahir")

# Argumen wajib: nama
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")

# Argumen wajib: tanggal lahir
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan tanggal lahir Anda (format: dd-mm-yyyy)")

# Parsing argumen
args = parser.parse_args()

# ==============================
# Menghitung usia
# ==============================
try:
    # Konversi string tanggal lahir ke datetime object
    tgl_lahir = datetime.strptime(args.tanggallahir, "%d-%m-%Y")
except ValueError:
    print("Format tanggal lahir salah. Gunakan format dd-mm-yyyy.")
    exit(1)

# Hitung usia
today = datetime.today()
usia = today.year - tgl_lahir.year - ((today.month, today.day) < (tgl_lahir.month, tgl_lahir.day))

# ==============================
# Tentukan sapaan
# ==============================
if usia < 30:
    sapaan = "kakak"
else:
    sapaan = "bapak"

# ==============================
# Tampilkan hasil
# ==============================
print(f"Terima kasih telah menggunakan panggildicoding.py, {sapaan} {args.nama}")
print(f"Usia Anda saat ini: {usia} tahun")
