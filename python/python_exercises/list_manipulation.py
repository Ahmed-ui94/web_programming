def main():    
    list = []
    # length of list
    lenth = int(input("Enter the length of the list:"))
    #calling list_inputs to fill the list
    list_inputs(lenth, list)
    #calling the square_even_numbers() to square the even numbers
    square_even_numbers(list)
    print(list)

# taking the user inputs to fill the list
def list_inputs(n, m):
    for i in range(n):
        value = int(input("value: "))
        m.append(value)

# a function that squares the evev numbers in the list
def square_even_numbers(l):
    for i in range(len(l)):
        if l[i]%2 == 0:
            l[i] *= l[i]

# calling main() for it to print the list items
if __name__ == "__main__":
    main()