import itertools
number = [0, 1, 2, 3]
counter = itertools.combinations_with_replacement(number, 2)
for item in counter:
    print(item, end=', ')