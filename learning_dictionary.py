# Example Dictionary

user = {
    "name": "junaidi",
    "umur": 20,
    "is_admin": False
}
# adding key, and Value
user["username"] = "Juanini_Giraga"
user["name"] = "Multo"

# Getting with Key
temp = user.get("name")
print(temp)

print("-" *30)

# Aplikasi Terbilang
numbers = input("Masukkan angka: ")

numbers_mapping = {
    "0": "Nol",
    "1": "Satu",
    "2": "Dua",
    "3": "Tiga",
    "4": "Empat",
    "5": "Lima",
    "6": "Enam",
    "7": "Tujuh",
    "8": "Delapan",
    "9": "Sembilan",
}

output = ""

for n in numbers:
    terbilang = numbers_mapping.get(n, "Invalid")
    
    output = output + terbilang + " "
    
print(output)


numbers = int(input("Masukkan angka: "))

angka = {
    0: "Nol",
    1: "Satu",
    2: "Dua",
    3: "Tiga",
    4: "Empat",
    5: "Lima",
    6: "Enam",
    7: "Tujuh",
    8: "Delapan",
    9: "Sembilan",
    10: "Sepuluh",
    11: "Sebelas"
}

def terbilang(n):
    if n < 12:
        return angka[n]
    elif n < 20:
        return angka[n - 10] + " Belas"
    elif n < 100:
        return angka[n // 10] + " Puluh " + terbilang(n % 10)
    elif n < 200:
        return "Seratus " + terbilang(n - 100)
    elif n < 1000:
        return angka[n // 100] + " Ratus " + terbilang(n % 100)
    elif n < 2000:
        return "Seribu " + terbilang(n - 1000)
    elif n < 1_000_000:
        return terbilang(n // 1000) + " Ribu " + terbilang(n % 1000)
    else:
        return "Angka terlalu besar"

print(terbilang(numbers))
