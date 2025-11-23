# Program untuk menentukan grade berdasarkan nilai akhir
# Nilai ≥ 85 → A
# Nilai ≥ 70 → B
# Nilai ≥ 55 → C
# Nilai ≥ 40 → D
# Nilai < 40 → E

# nilai = int(input("Masukkan nilai akhir: "))

# if nilai >= 85:
#     print ("A")
# elif nilai >= 70:
#     print ("B")
# elif nilai >= 55:
#     print ("C")
# elif nilai >= 40:
#     print ("D")
# else:
#     print ("E")
    
# Program untuk mencetak angka dari 1 sampai 20 menggunakan while loop

# a = 1
# while a <= 20:
#     print (a)
#     a += 1
# print("Selesai\n")

# Program untuk menghitung jumlah dari 1 sampai 100 menggunakan for loop
# jumlah = 0
# for i in range(1, 101):
#     jumlah += i
# print("Jumlah dari 1 sampai 100 adalah:", jumlah)

# Ptogram tebak angka
import random

angka_rahasia = random.randint(1, 5)
tebakan = int(input("Tebak angka antara 1 sampai 5: "))
if tebakan == angka_rahasia:
    print("Selamat! Tebakan Anda benar.")
else:
    print("Maaf, tebakan Anda salah. Angka yang benar adalah", angka_rahasia)

# list and dictionary