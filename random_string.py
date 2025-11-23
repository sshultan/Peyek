random_string = "Hello, World!"
print(random_string)
print(type(random_string))
print(random_string[:6])
print(random_string[0:4])
print(random_string[7:])

print("=" * 20)
# formated string
first_name = "Fauzi"
last_name = "Wahid"

message1 = first_name +"[" + last_name + "]"
message2= f"{first_name} [{last_name}]"
print(message1)
print(message2)

age = 20
pesan = "umur kamu adalah " + str(age) + " tahun"
pesan2 = f"umur kamu adalah {age} tahun"
print(pesan)
print(pesan2)

print("=" * 20)
# string method
course = "belajar python dasar sampai mahir"
length = len(course)
course_lower = course.lower()
course_upper = course.upper()

print(length)
print(course_lower)
print(course_upper)
print(course.title()) # setiap awal kata di buat besar
print(course.capitalize()) # huruf pertama saja yang besar
print(course.replace("a", "i"))
print(course.replace("belajar", "sharing" ))
print("=" * 20)

print(course)
language = "Java"

if language in course :
    print(f"iya ada {language} di dalam variable course")
else:
    print(f"tidak ada {language} di dalam variable course")