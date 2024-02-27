from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    i = str(input("Input: "))
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(i))


elif len(sys.argv) ==3 and (sys.argv[1] in ["-f","--font"]):
    i = str(input("Input: "))
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(i))


else:
    print("Invalid usage")
    sys.exit(1)

