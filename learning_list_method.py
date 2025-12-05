# # numbers = [
#     10, 2, 4, 7, 5, 9, 6, 8, 1 ]
# print(numbers)

# Menambahkan data ke dalam list
# numbers.append(99)
# print(numbers)

# Menambahkan data ke dalam list tapi ada indeks
# numbers.insert(5,100)
# print(numbers)

# Menghapus data yang ada di list
# numbers.pop(0)
# print(numbers)

# numbers.remove(6)
# print(numbers)

# Sorting
# numbers.sort()
# print(numbers)

# Menjumlahkan Angka di list
numbers = [5, 6, 7, 8, 9, 10, 4, 7]
# print(angka)
init_number = 0

for number in numbers:
    # print(number)
    init_number = init_number + number

print(init_number)
print(sum(numbers))
print(max(numbers))
print(min(numbers))