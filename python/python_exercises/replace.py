def main():
    valu = input("")
    print(play(valu))
def play(n):
    lst = []
    for i in n:
        if i in ' ':
            lst.append('...')
        else:
            lst.append(i)
    return ''.join(lst)

if __name__ == "__main__":
    main()

      