def validation(name):
    """
    Memvalidasi nama
    """
    for word in name.replace(" ", ""):
        if not word.isalpha():
            result = {
                'Valid': False,
                'status': 'Terkandung Angka!!!'
            }
            return result
    
    print("-"*10)
    return (f"Nama Kamu adalah {name}")
    
name = input("Masukkan nama anda: ")
print(validation(name))
