def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    a = ["CS50", "ECTO88", "NRVOUS"]
    for i in range(len(a)):
        if s == a[i]:
            return True
    return False

if __name__ == '__main__':
    main()