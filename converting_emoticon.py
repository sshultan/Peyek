message = input("")

emoji_mapping = {
    ":)": "😀",
    ":(": "😢",
    ":D": "😃",
    ":P": "😋",
    ";)": "😉",
    ":O": "😮",
    "<3": "❤️"
}

teks_split = message.split(" ")
# print(teks_split)
reply = ""

for m in teks_split:
    reply = reply + emoji_mapping.get(m, m) + " "

print(reply)

print("-" *20)

for symbol, emoji in emoji_mapping.items():
    message = message.replace(symbol, emoji)

print(message)