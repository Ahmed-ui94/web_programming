def mysum(arg):
    if not arg:
        return arg
    output = arg[0]
    for i in arg[1:]:
        if i.is_integer():
            output += i
        elif i.isalnum():
            i = int(i)
            output += i
        else:
            continue
    return output

print(mysum([38.0, 20.0, 30.0, "30", "f"]))