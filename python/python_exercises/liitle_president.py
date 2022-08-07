import random

def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        n = int(input("level: "))
        if n not in (1, 2, 3):
            n = int(input("level: "))
        else:
            break
    return n

def generate_integer(level):
    score = 0
    trials = 1
    for i in range(1, 11):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        while True:
            print(f'{x} + {y} = ', end="")
            answer = int(input())
            if answer == (x + y):
                score += 1
                break
            elif answer != (x + y) and trials != 3:
                print("EEE")
                trials += 1
                continue
            else:
                print(f'{x} + {y} = {x + y}')
                break
    print(f'score: {score}')


if __name__ == "__main__":
    main()