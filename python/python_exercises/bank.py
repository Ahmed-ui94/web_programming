def main():
    greetings = input("Greetings: ")
    print(value(greetings))

def value(greetings):
    if greetings.startswith("hello"):
        return "$0"
    elif greetings.startswith('h'):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main() 