import inflect

p = inflect.engine()
name = [ ]

while True:
    try:
        user = input("Enter something: ")
    except EOFError:
        break
    name.append(user)

print("Adieu, adieu, to", p.join(name))