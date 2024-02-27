import validators

i = input("What's your email address?")
z = validators.email(i)
if z is True:
    print("Valid")
else:
    print("Invalid")
