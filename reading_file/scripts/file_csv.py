# Membaca File CSV Tanpa menggunakan With Block
import csv

# data = open("../file/csv.csv", "r")

# data_file = csv.reader(data, delimiter=",")
# print(data_file) => output => object

# for row in data_file:
#     print(f"Nama: {row[0]}, Pekerjaan: {row[1]}, Location:{row[-1]}")

# data.close()

# Menggunakan With Block untuk membaca file csv

with open("../file/csv.csv", "r") as data:
    data_file = csv.reader(data, delimiter=",")
    
    for row in data_file:
        print(f"Nama: {row[0]}, Pekerjaan: {row[1]}, Location:{row[-1]}")

