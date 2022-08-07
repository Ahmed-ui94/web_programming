from random import random

def get_level():
    n = int(input("level: "))
    while True:
        if n not in (1, 2, 3):
            n = int(input("level: "))
        break