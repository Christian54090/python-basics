def increment(number: int, by: int=5) -> tuple:
    return (number, number + by)

print(increment(2, by=3))
print(increment(2))
