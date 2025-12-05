# 1. Dasar (input, Output, Variabel, Tipe Data)
# a. buatlah program yang menerima input nama dan umur, lalu mencetaknya dalam format "Nama saya [nama] dan saya berumur [umur] tahun."
nama = input("Masukkan nama Anda: ")
umur = input("Masukkan umur Anda: ")
print(f"Nama saya {nama} dan saya berumur {umur} tahun.")

print('-'*20)
# b. Buat program untuk menghiyung luas persegi panjang
# Rumus = panjang * lebar
 
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))    
luas = panjang * lebar
print(f"Luas persegi panjang adalah: {luas}")

print('-'*20)
x = 10
y = 3.14
nama = "huhu"
is_student = True

print(type(x))
print(type(y))
print(type(nama))
print(type(is_student))