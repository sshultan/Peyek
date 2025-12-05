# n = 1

# while n < 20:
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)
#     n += 1
    
    
    

# for item in range(1, 16):
#     if item % 3 == 0 and item % 5 == 0:
#         print("FizzBuzz")
#     elif item % 3 == 0:
#         print("Fizz")
#     elif item % 5 == 0:
#         print("Buzz")
#     else:
#         print(item)

names = []

while True:
    input_name = input("Masukkan Nama (ketik 'stop' untuk berhenti): ")

    if input_name == "stop":
        print("-" *30)
        break
    
    names.append(input_name)
    

for name in names:
    print(name)