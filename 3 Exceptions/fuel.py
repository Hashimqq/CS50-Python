while True:
    try:
        i = input("Fraction: ")
        x, y = i.split("/")
        x = int(x)
        y = int(y)
        i = round(x / y * 100)
        if x > y:
            continue

    except ValueError:
        print("Please enter intger")
    except ZeroDivisionError:
        print("You can't divide by zero!")
