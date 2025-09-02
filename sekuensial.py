var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i + 1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, next elements: {next_element}")

# array mecari nilai terbesar
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)

# ====================================================================================================================
#  Mengisi Array (List) Secara Sekuensial
# Membuat sebuah list kosong
angka_kuadrat = []
# Kita akan mengisinya dengan 5 angka kuadrat pertama
jumlah_elemen = 5

for i in range(jumlah_elemen):
    # Menghitung nilai kuadrat (i+1)^2
    nilai = (i + 1) ** 2
    # Memasukkan nilai ke dalam list
    angka_kuadrat.append(nilai)
    print(f"Iterasi ke-{i+1}: Menambahkan {nilai}, list sekarang: {angka_kuadrat}")

print(f"\nHasil akhir list: {angka_kuadrat}")

# ====================================================================================================================
# Menghitung Nilai Rata-rata Elemen Array
nilai_ujian = [85, 90, 78, 92, 88]
total_nilai = 0

# Menjumlahkan semua elemen secara sekuensial
for nilai in nilai_ujian:
    total_nilai = total_nilai + nilai # atau total_nilai += nilai

# Menghitung rata-rata
jumlah_data = len(nilai_ujian)
rata_rata = total_nilai / jumlah_data

print(f"Total nilai: {total_nilai}")
print(f"Jumlah data: {jumlah_data}")
print(f"Nilai rata-rata: {rata_rata}")

# Cara lebih singkat dengan fungsi bawaan
# print(f"Rata-rata (cara cepat): {sum(nilai_ujian) / len(nilai_ujian)}")

# ====================================================================================================================
# Mengalikan Setiap Elemen Array dengan Suatu Nilai
harga_awal = [10000, 25000, 40000, 15000]
faktor_kenaikan = 1.1 # Kenaikan harga 10%

print(f"Harga sebelum kenaikan: {harga_awal}")

# Loop menggunakan indeks untuk bisa mengubah nilai di dalam list
for i in range(len(harga_awal)):
    harga_awal[i] = int(harga_awal[i] * faktor_kenaikan)

print(f"Harga setelah kenaikan 10%: {harga_awal}")


# ====================================================================================================================
# Mencari Nilai Terbesar atau Terkecil
data_angka = [23, 56, 12, 78, 45, 99, 34]

# Mencari nilai terbesar
nilai_terbesar = data_angka[0] # Asumsikan elemen pertama adalah yang terbesar
for angka in data_angka:
    if angka > nilai_terbesar:
        nilai_terbesar = angka

# Mencari nilai terkecil
nilai_terkecil = data_angka[0] # Asumsikan elemen pertama adalah yang terkecil
for angka in data_angka:
    if angka < nilai_terkecil:
        nilai_terkecil = angka

print(f"Dari data: {data_angka}")
print(f"Nilai terbesar adalah: {nilai_terbesar}")
print(f"Nilai terkecil adalah: {nilai_terkecil}")

# Cara lebih singkat dengan fungsi bawaan
# print(f"Terbesar (cara cepat): {max(data_angka)}")
# print(f"Terkecil (cara cepat): {min(data_angka)}")



# ====================================================================================================================
# Mencari Indeks Letak Suatu Nilai Ditemukan Pertama Kali
kode_produk = ['A01', 'B02', 'C03', 'D04', 'B02', 'E05']
produk_dicari = 'D04'
indeks_ditemukan = -1 # Nilai default jika tidak ditemukan

# Loop menggunakan enumerate untuk mendapatkan indeks dan nilai sekaligus
for i, kode in enumerate(kode_produk):
    if kode == produk_dicari:
        indeks_ditemukan = i
        break # Hentikan loop karena sudah ketemu

if indeks_ditemukan != -1:
    print(f"Produk '{produk_dicari}' ditemukan pertama kali pada indeks: {indeks_ditemukan}")
else:
    print(f"Produk '{produk_dicari}' tidak ditemukan.")

# Cara lebih singkat dengan method .index()
# try:
#     print(f"Indeks (cara cepat): {kode_produk.index(produk_dicari)}")
# except ValueError:
#     print("Produk tidak ditemukan.")