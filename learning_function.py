def welcome_user(name):
    """
    Menampilkan pesan sambutan ke user
    """
    print(f"Welcome {name}")

names = ["junaidi", "Stella", "dori", "Ade", "Deankt"]

for name in names:
    welcome_user(name)

print("-" *20)

def user_level(user, level):
    """
    Menampilkan nama User dan Level User
    """
    print(f"Welcome {user}, Level {level}")
    print("Selamat Datang")

# not using keyword_argument
user_level(10, "HUHU")

# using keyword_argument
user_level(level=20, user="DEANKT")

print("-" *20)

# Belajar tentang Return Value

def multiply(a, b):
    """
    Mengalikan a dan b
    """
    return a * b

result = multiply(2, 20)
print(result)

def template(name):
    """
    fungsi untuk menampilkan nama user
    """
    print(name)
    
template("agung")

def welcome_user(name, level):
    # print(f"Welcome {name}, Level kamu{level}")
    # akan Me-Return Value = None
    # kecuali 
    return (f"Welcome {name}, Level kamu{level}")

result = welcome_user("agung", 20)
print(result)
