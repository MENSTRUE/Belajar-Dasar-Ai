# list
list = [1,3,4,5,6,7,6,8,0]

print(list)
print(len(list))

# set
list1 = set([2,4,3,5,6,7,8,0])
print(list1)
print(len(list1))

# string
list2 = "belajar"

print(list2)
print(len(list2))

# min max
angka = [11,13,15,17,19,21,23]
print(min(angka))
print(max(angka))

# count
ganjil = [1,3,5,7,9,11,33,51,99]
print(ganjil.count(11))

string = "aku sebenarnya adalah ultraman yang menyamar"
substring = "a"
print(string.count(substring))

# In dan Not In
kalimat = "berduaan sama kamu itu beban seumur hidup aku"
print('sama' in kalimat)
print('aku' in kalimat)
print('sekar' in kalimat)
print('itu' not in kalimat)

# Memberikan Nilai untuk Multiple Variable
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

# sort (mengurutkan)
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
# mebalikannya
kendaraan.sort(reverse=True)

print(kendaraan)

# Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya
# Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).
