def main():
    my_list =[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    odd_elements(my_list)

def odd_elements(m):
    for i in range(1,len(m), 2):
        print(m[i])

main()