start = 25
end = 50
print("prime number between",start,"and", end,"are")

for num in range(start, end+1):
    #prime numbers start from above 1
    if num > 1:
        for i in range(2,num):
            #check for prime numbers
            if (num%i==0):
                #its not prime number if it produces 0
                break
        else:
            print(num)