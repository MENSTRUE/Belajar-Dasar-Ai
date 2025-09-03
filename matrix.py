matriks = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

print(matriks)

#  jika pake numpy
import numpy

matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])
print(matriks)


# bandingkan ukuran memori yang digunakan jika kita menggunakan matriks Python dan matriks NumPy
import numpy
import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)

# ================================================================================================
# Deklarasi Matriks
matriks = [[1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]]

print(matriks)

# Deklarasi dengan nilai default
matriks = [[0 for j in range(4)] for i in range(3)]

print(matriks)


# Akses Elemen Matriks

var_mat = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]

print(var_mat[2][1])

# =================================================================
# Operasi Matriks pada Python

# Membuat matriks 2x2
var_mat = [[5, 0],
          [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
    def_mat[i][j] = var_mat[i][j]*2

print(def_mat)

# simplenya
import numpy as np

var_mat = np.array([[5, 0],
                    [1, -2]])

result = var_mat * 2

print(result)