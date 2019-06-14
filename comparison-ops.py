import random

temp = random.choice([31, 17, 7])

if temp > 30:
    print("It's a hot day")
elif temp < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")

name = input("What is your name? ")
if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name can be a maximum of 50 character")
else:
    print("name looks good!")
