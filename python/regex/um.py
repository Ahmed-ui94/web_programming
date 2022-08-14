import re

def main():
    print(count(input("Text: ")))


def count(text):
    if matches := re.findall(r'\b[U|u][M|m]\b', text):
        
        return f'{len(matches)}'


if __name__ == "__main__":
    main()