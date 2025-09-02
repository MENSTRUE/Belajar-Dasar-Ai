import array

x = array.array("i",[1, 2, 3, 4, 5])
print(x)
print(type(x))

# Python kita dapat mendeklarasikan array menggunakan dua cara
# Pertama dengan memanfaatkan list dan kedua menggunakan library Python

# menggunakan list Ada dua cara untuk melakukan deklarasi array menggunakan list, yakni berikut.
# Mendefinisikan Isi Array
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

# Mendefinisikan Nilai Default
var_arr = [0 for i in range(10)]
print(var_arr)

# jika kita ubah nilai defaultnya
var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)

# Mengakses Elemen Array
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr[0])
