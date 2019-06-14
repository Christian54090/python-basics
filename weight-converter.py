weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit == "L":
    print("Your weight is " + str(weight / 2.2) + " kilograms")
elif unit == "K":
    print("Your weight is " + str(weight * 2.2) + " pounds")
