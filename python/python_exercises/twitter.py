
def main():
    input1 = input("Input: ")
    print(shorten(input1))


def shorten(word):
    st1 = []
    for st in word:
        if st not in 'aeoiuAEOIU':
            st1.append(st)
    return ''.join(st1)
   
    
if __name__ == "__main__":
    main()