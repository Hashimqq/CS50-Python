def main():

    time = input("E: ")

    if convert(time) >= 7.00 and convert(time) <= 8.00:
        print("breakfast time ")
    elif convert(time)>= 12.00 and convert(time) <=13.00:
        print("lunch time")
    elif convert(time) >= 18.00 and convert(time) <= 19.00:
        print("dinner time")
    else:
        print("No")

def convert(a):
    hours, minutes = map(int, a.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()