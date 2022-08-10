
def main():
    fractions = input("fractions (x/y): ").split("/")
    percentage = convert(fractions)
    print(gauge(percentage))


def convert(fractions):
     
    x, y = fractions
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    return (int(x) / int(y)) * 100

#function to convert fraction to percentage
def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f'{int(percentage)}%'


if __name__ == "__main__":
    main()