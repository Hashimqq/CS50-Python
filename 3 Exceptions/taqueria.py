try:
    total = 0
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    while True:
        i = input("Item: ").strip().title()
        if i in menu:
            total += menu[i]
            print(f"Total: ${total:.2f}")
        elif i == "":
            break
except EOFError:
    pass

# i'm sorry i used chatgpt to help me in check50 i tried everything it always gave me yellow , please don't delete my account