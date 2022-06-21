
def main():
    while True:
        try: 
            fractions = input("fractions: ").split("/")
            x, y = int(fractions)
            if y == 0:
                raise ZeroDivisionError
        except (ValueError, ZeroDivisionError):
            continue
        else:
            return fuel_percent(x, y)
    
#function to convert fraction to percentage
def fuel_percent(x, y):
    percent = (x/y) * 100
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(int(percent),'%',sep="")


if __name__ == "__main__":
    main()