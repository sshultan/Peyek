# check_palindrome("A man a plan a canal Panama")
# check_palindrome("race a car")

def is_palindrome(text):
    teks_bersih = text.replace(" ", "").lower()
    
    if teks_bersih == teks_bersih[::-1]:
        print("is palindrome teks")

    return teks_bersih == teks_bersih[::-1]

is_palindrome("A man a plan a canal Panama")
is_palindrome("race a car")
print(is_palindrome("race a car"))