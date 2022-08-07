import inflect

p = inflect.engine()

lst = [] 
def user_input():
    while True:
        try:
            name = input("Name: ")
            lst.append(name)
        except(EOFError):
            print()
            break
    return lst
prin = "Adhieu, Adhieu, to" 
output = p.join(lst)

user_input() 
print("Adieu Adieu to " + output)