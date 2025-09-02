if 9>10:
print("Hello World!") #salah di penepatan print harusnya ada tab (IndentationError)

# SyntaxErrors
i = 1
while i<3 #kurang : saja tapi bisa error
    print("Dicoding")
    i+=1

# bentuk eror pasti
# File "<nama file>", line <nomor baris>
# <baris kode dengan kesalahan>
# ^
# <tipe kesalahan>: <pesan kesalahan>

# Exceptions
bukan_angka = '1'
bukan_angka + 2

# Penanganan Pengecualian
z=0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nilai nol.")

# other
var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")

# Raise Exception
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)
