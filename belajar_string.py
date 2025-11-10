# 1. cara membuat String

data = "ini adalah string"

print(data)
print(type(data))

"""
    1. dengan menggunakan sigle quote '...'
    2. dengan menggunakan double quote "..."
"""

data = "menggunakan single quote"
print(data)

data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")
# 2. cara membuat String dengan tanda \
print('mari shalat jum\'at tepat waktu')
print('g\'day isn\'t it?')

# blackslash \
print("C:\\user\\fauzi")

# tab \t
print("fauzi\twahid")

# backspace \b
print("fauzi \bwahid")

# newline \n \r
print("ini baris pertama \nini baris kedua") #LF - line feed
print("ini baris pertama \rini baris kedua") #CR - carriage return
print("ini baris pertama \r\nini baris kedua") #CRLF - carriage return line feed

# 3. string literal atau raw string
print("C:\\new folder") #normal string
print(r"C:\new folder") #raw string
# multiline string
print("""
nama : fauzi wahid
kelas : 12 RPL 2
alamat : jakarta
""")

print(r"""
nama : fauzi wahid
kelas : 12 RPL 2
website : www.fauziwahid.com
""")
