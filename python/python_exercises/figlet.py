import sys
import random
from pyfiglet import Figlet


figlet = Figlet()

lst = figlet.getFonts()

s: str = input("Input: ")

if len(sys.argv) == 1:
    rand = random.choice(lst)
    figlet.setFont(font=rand)
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        figlet.setFont(font=sys.argv[2])
        print("output: ", figlet.renderText(s))
    else:
        sys.exit("invalid command line input ")

