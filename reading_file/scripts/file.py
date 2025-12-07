# ###Reading File .txt
# users = open("../file/user.txt", "r")

# read => membaca keseluruhan file
# print(users.read())

# readline() => ini hanya membaca 1 line saja
# print(users.readline())

# ##Implementasi For untuk membaca file tanpa tahu ada berapa line di dalam file
# index = 1
# arrays = users.readlines()
# for line in arrays:
#     print(f"{index}. {line}")
#     index += 1

# users.close()

# Menulis file => .txt
users = open("../file/user.txt", "r+")

# print(users.read())
print(users.read())
users.write("HUJAN TERUS")
users.close()