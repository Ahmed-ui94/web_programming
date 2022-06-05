def factorial_loop():

    # a program to print a factorial of a number
    number = int(input("number: "))
    for i in range(number-1, 0 , -1):
        number = number * i
    
    print(number)
def main():
    num = int(input(""))
    print(recursive_func(num))

def recursive_func(n: int):
    if n==0:
        print(0)

    else:
        return n * recursive_func(n-1)

main()                   