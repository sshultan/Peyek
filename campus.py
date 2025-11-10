# latihan konversi satuan temperature

# program konversi Celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

# CELCIUS KALKULATOR
# celcius = float(input("Masukkan suhu dalam celcius: "))

# print("Suhu Awal ", celcius, " Celcius")

# reamur_celcius = (4 / 5) * celcius
# print("suhu dalam satuan Reamur: ", reamur_celcius, "R")

# fahrenheit_celcius = (9 / 5) * celcius + 32
# print("suhu dalam satuan Fahrenheit: ", fahrenheit_celcius, "F")

# kelvin_celcius = celcius + 273
# print("suhu dalam satuan Kelvin: ", kelvin_celcius, "K")

# REAMUR KALKULATOR
# reamur = float(input("Masukkan suhu dalam Reamur: "))
# print("Suhu Awal", reamur, " Reamur")

# celcius_reamur = (5 / 4) * reamur
# print("suhu dalam satuan Celcius: ", celcius_reamur, "C")

# fahrenheit_reamur = (9 / 4) * reamur + 32
# print("suhu dalam satuan Fahrenheit: ", fahrenheit_reamur, "F")

# kelvin_reamur = (5 / 4) * reamur + 273
# print("suhu dalam satuan Kelvin: ", kelvin_reamur, "K")

# FAHRENHEIT KALKULATOR
# fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
# print("Suhu Awal ", fahrenheit, "F")

# fahrenheit_celcius = round((5 / 9) * (fahrenheit - 32))
# print("suhu dalam satuan Celcius: ", fahrenheit_celcius, "C")

# fahrenheit_reamur = round((4 / 9) * (fahrenheit - 32))
# print("suhu dalam satuan Reamur: ", fahrenheit_reamur, "R")

# fahrenheit_kelvin = round((5 / 9 * (fahrenheit - 32)) + 273)
# print("suhu dalam satuan Kelvin: ", fahrenheit_kelvin, "K")

# KELVIN KALKULATOR
kelvin = float(input("Masukkan suhu dalam Kelvin: "))
print("Suhu Awal ", kelvin, "K")

kelvin_celcius = kelvin - 273
print("suhu dalam satuan Celcius: ", kelvin_celcius, "C")

kelvin_reamur = round((4 / 5) * (kelvin - 273))
print("suhu dalam satuan Reamur: ", kelvin_reamur, "R")

kelvin_kelvin = ((9 / 5) * (kelvin - 273)) + 32
print("suhu dalam satuan Fahrenheit: ", kelvin_kelvin, "F")
