def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        if percentage is not None:
            print(gauge(percentage))
            break


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            print("Numerator should not be greater than denominator.")
            return None
        return round(x / y * 100)
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"


if __name__ == "__main__":
    main()
