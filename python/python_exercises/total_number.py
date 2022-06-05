def using_for_loop():
    num = '75869'
    count = []
    for i in range(len(num)):
        count.append(i)
    
    print(len(count))
# another method to calculate the total number of digits of a number
def using_while_loop():
    counter = 0
    number = 76869
    while number !=0:
        number = number//10
        counter += 1         
    
    print(counter)