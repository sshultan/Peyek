kondisi = 1

while kondisi < 10:
    print("* " * kondisi)
    kondisi += 1
    
# print("Finish")
print("=" * 40)


for bintang in range(1, 26):
    print("* " * bintang)
    

print("=" * 40)

n = 1

while n < 20:
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
    n += 1