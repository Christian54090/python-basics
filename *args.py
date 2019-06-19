def multiply(*list):
    total = 1
    for x in list:
        total *= x

    return total

print(multiply(2, 3, 4, 5))
