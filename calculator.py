# (+ - / *, exit)
command = ""

while command != "exit":
    input_operasi = input("Operasi: ")
    
    if input_operasi == "exit":
        print("Terima kasih sudah menggunakan aplikasi calculator")
        break
    
    if input_operasi != "+" and input_operasi != "-" and input_operasi != "*" and input_operasi != "/":
        print("Operator Tidak Dikenali")
        continue
    
    a = int(input("angka pertama : "))
    b = int(input("angka kedua : "))
    
    if input_operasi == "+":
        result = a + b
    elif input_operasi == "-":
        result = a - b
    elif input_operasi == "*":
        result = a * b
    elif input_operasi == "/":
        result = a / b
    
    print(f"hasil :{result}")
    print("="*20)
    