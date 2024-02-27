import random

while True:
    try:
        level = int(input("Level: "))
        i = int(input("Guess:"))
        coin = random.randint(1,level)
        if i > coin:
            print("Too large!")
        elif i < coin:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
