# exception pada spesifik cases
# try:
#     level = int(input("Masukkan angka:"))
#     level = level/0
#     print(level)
# except ZeroDivisionError:
#     print(f"Angka {level} tidak bisa dibagi 0")
# except ValueError:
#     print("Tolong masukkan angka")
    

# General Exception
try:
    name = input("Masukkan nama anda: ")
    valid = True
    for n in name.replace(" ", ""):
        if not n.isalpha():
            print("Nama tidak boleh mengandung angka!!")
            valid = False
            break
    if valid:
        age = int(input("Masukkan umur anda: "))

        print("-"*20)
        print(f"Nama anda {name}")
        print(f"Umur anda {age}")
except :
    print("Format yang dimasukkan salah")