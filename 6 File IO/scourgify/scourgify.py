import csv
import sys


def main():
    check()
    x = []
    try:

        with open(sys.argv[1], "r") as file:
            #     reader = csv.DictReader(file)
            #     for row in reader:
            #         students.append({"name": row["name"], "house": row["house"]})
            # for student in students:
            #     if sys.argv[1] :
            #         print(f"{student['name']}  {student['house']}")

            reader = csv.DictReader(file)
            for row in reader:
                s_n = row['name'].split(",")
                x.append({"first": s_n[1].lstrip(), "last": s_n[0], "house": row["house"]})
            print(x)
    except FileNotFoundError:
        sys.exit(f"could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as new:
        writer = csv.DictWriter(new, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in x:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


def check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == '__main__':
    main()
