num = 76542
reversed_num = 0
print("number before reversing: ", num)
# using while loop to reverse the interger
while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10
print("after reversing: ", reversed_num)
