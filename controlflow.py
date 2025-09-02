# Percabangan

hati = "cinta"

if hati == "cinta":
    print("dia menyukai kamu")
else:
    print("dia tidak menyukaimu")

# ketika null dia akan bernilai false
x = ""

if x:
    print("Ini True")

# Nilai yang sudah didefinisikan bernilai salah: None dan False.
# Angka nol dari semua tipe numerik: 0, 0.0, 0j, Decimal(0), Fraction(0,1).
# Urutan (sequence) dan koleksi (collection) yang kosong: "", (), {}, set(), range(0).

# else
tinggi_badan = 120

if tinggi_badan >=160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster")

# elfif
nilai = 65

if nilai>=80:
   print("Selamat! Anda mendapat nilai A")
   print("Pertahankan!")
elif nilai>=70:
   print("Hore! Anda mendapat nilai B")
   print("Tingkatkan!")
elif nilai>=60:
   print("Hmm.. Anda mendapat nilai C")
   print("Ayo semangat!")
else:
   print("Waduh, Anda mendapat nilai D")
   print("Yuk belajar lebih giat lagi!")

# kita dapat menambahkan operator pada percabangan
nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")

# Ternary Operators
lulus = True
print("selamat") if lulus else print("perbaiki")

# versi bentuk blok
# lulus = True
# if lulus:
#     print("Selamat")
# else:
#     print("Perbaiki")

# ternary tuple
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)

lulus1 = True
if lulus1:
    print("Selamat, Anda lulus!")
else:
    print("Perbaiki, Anda belum lulus.")

# for
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

# range
for i in range(10):
    print(i)

# range (start, stop, step)
for i in range(1,10,2):
    print(i)

# while
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment -> harus ada

# For Bersarang
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

# break
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

# continue
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

# Else setelah For
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

# Else setelah While
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

# pass
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

# List Comprehension
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

# 