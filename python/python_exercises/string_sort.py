def main():
    print(strsort())

def strsort():
    # provide separated by space as sentences
    string = input("write your words: ")
    string2 = []
    for i in sorted(string.split()):
        string2.append(i)
    return ', '.join(string2)

if __name__ == "__main__":
    main()