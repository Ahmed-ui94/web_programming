def range1():
    for i in range(10, 20):    # generators in functions
        yield i

print (next(range1()))