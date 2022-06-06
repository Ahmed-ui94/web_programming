def mean(*arg):
    num_iterations = 0
    sum_arg = 0
    for i in arg:
        sum_arg += i
        num_iterations += 1
        
    average = sum_arg // num_iterations
    print(sum_arg)
    return average

print(mean(3,4,5,6,9))