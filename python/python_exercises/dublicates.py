linked = [11, 11, 11, 43, 43, 60]

def dublicate_remover(n):
    lst = []
    for i in n:
        if i not in lst:
            lst.append(i)

    return lst

print(dublicate_remover(linked))

