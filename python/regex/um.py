import re

def main():
    print(count(input("Text: ")))


def count(text):
    if matches := re.findall(r'\bum\b', text, re.I):
        
        return f'{len(matches)}'


if __name__ == "__main__":
    main()