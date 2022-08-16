import math
import re
import sys

Dict = {
    "12:00 AM" : "00:00",
    "1:00 AM" : "01:00",
    "2:00 AM" : "02:00",
    "3:00 AM" : "03:00",
    "4:00 AM" : "04:00",
    "5:00 AM" : "05:00",
    "6:00 AM" : "06:00",
    "7:00 AM" : "07:00",
    "8:00 AM" : "08:00",
    "9:00 AM" : "09:00",
    "10:00 AM" : "10:00",
    "11:00 AM" : "11:00",
    "12:00 AM" : "12:00",
    "10:00 AM" : "10:00",
}

def main():
    print(convert(input("Hours: ")))


def convert(h):
    pattern = r'^(([0-9]+):?(00)? (AM|PM)) to ([0-9]+):?(00)? (AM|PM)$'
    if matches := re.search(pattern, h):
        number = matches.group(1)
        num2 = matches.group(4)
        if number in Dict and num2 in Dict:








if __name__ == "__main__":
    main()