import random


def main():
    generate_integer(get_level())


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
            break
        except ValueError:
            print("Enter number from 1 to 3")
    return level


def generate_integer(level):
    global x, y
    score = 0
    for i in range(10):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        for attempt in range(3):

            answer = int(input(f"{x} + {y} = "))

            if answer == (x + y):
                score += 1
                break

            else:
                print("EEE")

            if attempt == 2 and answer != (x + y):
                print(f"{x} + {y} = {x + y}")


    print("Score: ",score)


if __name__ == "__main__":
    main()
