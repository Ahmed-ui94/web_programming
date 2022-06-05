# program to convert a camel case letters to snake case letters

def change_case(str):
    res = [str[0].lower()]
    for c in str[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
    
    return ''.join(res)

str = input("camel case:")
print(change_case(str))
            