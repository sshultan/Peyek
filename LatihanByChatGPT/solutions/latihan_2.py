def validation_age(age):
    """
    Memvalidasi umur dari < 0 and > 120
    """
    if age < 0 or age > 120:
        result = {
            "success": False,
            "data": None,
            "message": "Umur di luar batas"
        }
        return result

    result = {
        "success": True,
        "data": age,
        "message": "Umur Kamu memenuhi kriteria!!!"
    }
    return result

try:
    umur = int(input("Masukkan umur anda: "))
    hasil = validation_age(umur)
    print(hasil["message"])
except :
    print("Masukkan Angka!!!!")