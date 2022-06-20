def main():
    Camelcase = input("CamelCase: ")
    print(convert_camel_case(Camelcase))

def convert_camel_case(str):
    lst = []
    for i in str:
        if i.isupper():
            lst.append("_")
            ls = i.lower()
            lst.append(ls)
        else:
            lst.append(i)
    return ''.join(lst)

if __name__ == "__main__":
    main()

            