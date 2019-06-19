# for x in "Python":
    # print(x)

# for x in ['a', 'b', 'c']:
    # print(x)

# for x in range(0, 10, 2):
    # print(x)

names = ["John", "Mary"]

for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")
