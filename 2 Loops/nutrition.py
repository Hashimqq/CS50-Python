item = input("item: ")
e = [
    {"apple": 130},
    {"Avocado": 50},
    {"Kiwifruit": 90},
    {"pear": 100},
    {"Sweet Cherries": 100}
]
for c in e:
    if item in c:
        print("Calories:", c[item])