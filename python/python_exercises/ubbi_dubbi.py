def main():
    print(ubbi_dubbi())

def ubbi_dubbi():
    strin = input("word: ")
    my_string = [ ]
    for i in strin:
        if i in 'aeiou':
            my_string.append('ub' + i)
        else:
            my_string.append(i)

    return ''.join(my_string)
if __name__ == "__main__":
    main()