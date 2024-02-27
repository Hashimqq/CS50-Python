cents = 50
amount = 0
while amount < cents:
    print("Amount Due:", cents - amount)
    coin = int(input("Insert Coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        amount += coin
    else:
        print("Invalid Coin:")

owed = amount - cents

if owed > 0:
    print("Change Owed:", owed)
else:
    print("Change Owed: 0")


