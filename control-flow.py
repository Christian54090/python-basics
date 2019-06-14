is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print("it's a lovely day")

print("Enjoy your day")

price = 1000000
good_credit = True

if good_credit:
    down_payment = int(price * 0.1)
else:
    down_payment = int(price * 0.2)

print("The down payment is $" + str(down_payment))
