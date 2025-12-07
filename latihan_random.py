import random

from psutil import users

# simpel impelmentasi random
# for number in range(10):
#     print(random.randint(1, 20))

# Implementasi dengan array,
## cara lama

person = ["Junaidi", "Deankt", "Ade", "Mada", "Boti", "Dio", "Sisil"]

# lower_limit = 0
# upper_limit = len(person) - 1

# random_person = random.randint(lower_limit, upper_limit)

# winner = person[random_person]

# print(winner)

## cara Baru

winner = random.choice(person)
print(winner)