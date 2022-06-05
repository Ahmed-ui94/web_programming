# function for checking denominations 
total_paid = 0
Amount_due = 50


#condtion for checking denomination
while Amount_due >=0:
    coin = int(input("insert coin: "))
    if coin == 25:
        total_paid = total_paid + coin
        Amount_due = Amount_due - coin
        print("amount due: ", Amount_due)
    elif coin == 10:
        total_paid = total_paid + coin
        Amount_due = Amount_due - coin
        print("Amount due: ", Amount_due)
    elif coin == 5:
        total_paid = total_paid + coin
        Amount_due = Amount_due - coin
        print("amount due: ", Amount_due) 
    else:
        print("coin not acceptable")

# remaining balance
change_coin =total_paid - Amount_due
print('Change owed: ', change_coin)