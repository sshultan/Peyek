# Tuple adalah immuttable
# a tuple is an ordered, immutable collection of elements. The term "immutable" signifies that once a tuple is created, its contents cannot be changed, added to, or removed

numbers = (5, 6, 7, 8, 9, 10, 2, 3, 4, 1)

print(numbers)

print("-"*20)
# Unpack
nama = ("Stella", "Dori", "Muto", "Bahlil")
nama_angka = ["SandDISK", "Vgen", "Magnum", "Sampoerna"]
# normal plan
# a = nama[0]
# b = nama[1]
# c = nama[2]
# d = nama[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Mode Singkat

# a, b, c, d = nama
e, f, g, h = nama_angka
# a,_,_,_, = nama 
# _ ini akan dianggap menjadi variabel yang gak akan digunakan 

# cara sederhana apabila cuma membutuhkan satu variabel saja
a, *b = nama
# *b artinya semua sisa Value selain a, dimasukkan ke dalam b, dan type data menjadi array

print(a)
print(b)
print(type(b))

