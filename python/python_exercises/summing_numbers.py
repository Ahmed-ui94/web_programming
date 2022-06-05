def mysum(lst1, steps = 0):
    output = 0
    for i in range(steps,len(lst1)):
        output += lst1[i]
    print(output)



lst = [12,56,34]
# preface  with * when you want turn an iterable into separate arguments
# like this mysum(*lst)
mysum(lst)
