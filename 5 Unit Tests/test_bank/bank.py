def main():
    greeting = input("Greating: ")
    print("$", value(greeting))


def value(greeting):
    if greeting == "Hello":
        return 0
    elif greeting == "Hello, Newman":
        return 0
    elif greeting.startswith("H"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
