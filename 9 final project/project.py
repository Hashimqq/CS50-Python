import random
import time
import csv
from tabulate import tabulate
import sys


def get_difficulty(level):
    if level not in [1, 2, 3, 4]:
        print("Choose 1, 2, 3, or 4.")
        sys.exit(1)
    return level


def play_game(level, duration=30):
    start_time = time.time()
    end_time = start_time + duration
    score = 0

    while time.time() < end_time:
        x, y, l = generate_question(level)
        answer = input(f"{x} {l} {y} = ")
        if answer.strip() == "":
            print("Please provide an answer.")
            continue

        try:
            answer = int(answer)
        except ValueError:
            print("Please enter a number.")
            continue
        if check_answer(x, y, l, answer):
            score += 1

    return score


def generate_question(level):
    if level == 1:
        operation = random.choice(["+"])
        x = random.randint(1, 25)
        y = random.randint(1, 25)
    elif level == 2:
        operation = random.choice(["+", "-"])
        x = random.randint(1, 25)
        y = random.randint(1, 25)
    elif level == 3:
        operation = random.choice(["+", "-", "*"])
        x = random.randint(1, 25)
        y = random.randint(1, 25)
    elif level == 4:
        operation = random.choice(["+", "-", "*", "/"])
        x = random.randint(1, 25)
        y = random.randint(1, 25)
    return x, y, operation


def check_answer(x, y, operation, answer):
    if operation == "+":
        return answer == (x + y)
    elif operation == "-":
        return answer == (x - y)
    elif operation == "*":
        return answer == (x * y)
    elif operation == "/":
        return answer == int(x / y)


def csv_file(name, level, score):
    with open('project.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, level, score])


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <name> <level> <display_data>")
        sys.exit(1)

    name = sys.argv[1].capitalize()
    level = get_difficulty(int(sys.argv[2]))
    score = play_game(level)
    print("Score:", score)
    csv_file(name, level, score)

    choice = sys.argv[3]
    if choice.lower() == "y":
        with open("project.csv", "r") as file:
            reader = csv.reader(file)
            data = [["Name", "Level", "Score"]] + [row for row in reader]
            print(tabulate(data, headers='firstrow', tablefmt='grid'))


if __name__ == "__main__":
    main()
