def main():
    dict1 = {}
    inputs(dict1)
    for key, value in dict1.items():
        print(value, key)


def inputs(dict1):
    while True:
        try:
            item = input().capitalize()
            if item not in dict1:
                dict1[item] = 1
            else:
                dict1[item] = dict1[item] + 1
        except (EOFError, KeyError):
            break


main()
