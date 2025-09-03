def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)

# fungsi terbagi menjadi dua jenis.
# 1. Built-in Functions -> bawaan
# 2. User-defined Functions
# def mencari_luas_persegi_panjang(panjang,lebar):
#     luas_persegi_panjang = panjang*lebar
#     return luas_persegi_panjang
#
# persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
# print(persegi_panjang_pertama)
#
# persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
# print(persegi_panjang_kedua)

# =============================================================================================
# Library dalam Python terdiri dari dua jenis.
# 1. Python Standard Library -> tidak perlu istalasi
# 2. External Library -> harus import

# =============================================================================================
# Argumen
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

print(persegi_panjang_pertama)

# menulis argumentnya / parameternya


# Positional Argument
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)

print(persegi_panjang_pertama)

# ========================================================================================
# parameter
# 1. Positional-or-Keyword
# parameter default dalam Python
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

# 2. Positional-Only
def penjumlahan(a, b, /):
    return a + b

print(penjumlahan(8, 50))
# Deklarasi Tetap Wajib: Anda tetap harus menulis nama untuk semua parameter, seperti (a, b, /)
# Fungsi / Sebenarnya: Hanya mengubah cara memanggil fungsinya. penjumlahan(8, 50) diizinkan, tapi penjumlahan(a=8, b=50) akan error.
# print(penjumlahan(a=8, b=50))

# 3. Keyword-Only
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting(pesan="Selamat sore!",nama="Dicoding"))

# Tanda * di sana berfungsi sebagai penanda yang memaksa semua parameter di sebelah kanannya
# (nama dan pesan) menjadi keyword-only. Artinya, saat Anda memanggil fungsi tersebut,
# Anda harus secara eksplisit menyebutkan nama parameternya.

# 4. Var-Positional (Variadic Positional Parameter)
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

# parameter *args mengumpulkan semua argumen posisi yang diberikan saat pemanggilan fungsi dan membungkusnya menjadi tuple "args"

# 5. Var-Keyword (Variadic Keyword Parameter)
def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

# *kwargs: Mengumpulkan semua argumen keyword (pakai nama, nama="Dicoding") menjadi DICTIONARY.

# Fungsi Anonim (Lambda Expression)
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))

# Variabel Global dan Lokal
a = 10

def add(b):
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)

# Variabel Lokal
def add(a, b):
    lokal_var = 5
    result = a+b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)

# beda dengan fungsi procedure tanpa return
def greeting():
    print("Halo Selamat Datang!")

greeting()



