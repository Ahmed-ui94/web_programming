def mysum(*arg):
    if not arg:
        return arg
    output = arg[0]
    for i in arg[1:]:
        output += i
    return output

print(mysum((1,2,3,4),(1,3,4,4)))