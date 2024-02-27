from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid date")

    print(season(year, month, day))


def season(year, month, day):
    try:
        user = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid date"
    today = date.today()
    live = today - user
    minutes = int(live.total_seconds() / 60)
    final = p.number_to_words(minutes, andword="")
    return final.capitalize() + " minutes"


if __name__ == '__main__':
    main()
