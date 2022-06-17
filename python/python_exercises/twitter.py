
def twiter():
    input1 = input("Input: ")
    st1 = []
    for st in input1:
        if st not in 'aeoiuAEOIU':
            st1.append(st)
    return ''.join(st1)
   
    
print(twiter())