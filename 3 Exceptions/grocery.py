dictionary= {

    }
while True :
    try:
        item = input().lower()
    except EOFError:
        break
    if item == "":
        break
    elif item in dictionary:
        dictionary[item] += 1
    else:
        dictionary[item] = 1
s = sorted(dictionary.items())
for item,n in s:
    print(f"{n} {item.upper()}")