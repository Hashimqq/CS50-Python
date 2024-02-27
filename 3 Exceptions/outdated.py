m = [
    "January","February","March",
    "April","May","June","July",
    "August","September","October",
    "November","December"
]
while True:
    try:
        i = input("Date(D/M/Y) : ")
        month, day, year = i.split("/")
        month = int(month)
        day = int(day)
        year = int(year)

        if month < 1 or month > 12:
            continue
        elif day < 1 or day > 31:
            continue
        elif len(str(year)) != 4:
            continue
        print(f"{year}-{month:02}-{day:02}")
        break
    except ValueError:
        pass
