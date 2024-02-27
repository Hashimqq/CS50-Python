camel = input("camelCase: ")
e = ""
for x in camel:
    if x.isupper():
        e = e + "_" + x.lower()
    else:
        e += x
print("snake_case:", e)