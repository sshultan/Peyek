trying = 0
secret_number = 9
limit = 3

while trying < limit:
    guest_number = input("Masukkan number 1 - 9 : ")
    guest_number = int(guest_number)
    
    if guest_number == secret_number:
        print("Selamat Kamu Sudah Menebak Secret")
        break
    elif trying == 1:
        print("Kesempatan Kamu tersisa 1!!")
    else:
        print("Kamu Salah Menebak, Coba Lagi")
    
    trying += 1