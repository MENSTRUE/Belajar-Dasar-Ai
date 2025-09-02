x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
# menambahkan data
x ['Job'] = "Web Developer"
# menghapus data
del x['isMarried']
# mengubah data
x ['name'] = "Dicoding"

print(type(x))
print(x)

# salah dikarenakn tidak seperti array ataupun list
# print(x[0])

# yang benar seberti ini
print(x ['name'])