def main():
    plate = input("plate: ").upper()
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")

def is_valid(s):
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        for char in s:
            if char.isdigit():
                digit1 = s.index(char)
                if s[digit1:].isdigit() and int(char) != 0:
                    return True
                else:
                    return False
        return True
    else:
        return False
     


if __name__ == "__main__":
    main()        