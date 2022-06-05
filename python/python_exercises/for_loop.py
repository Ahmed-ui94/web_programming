#fibonacci series of numbers
num1 = 0
num2 = 1
for i in range(11):
    #current number
    print(num1)
    result = num1 + num2
    
    num1 = num2
    num2 = result