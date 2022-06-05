Amount_due = 50
change_owed = 50
total_required = 0

while True:
    coin = int(input("insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        Amount_due = Amount_due - coin
        
        if Amount_due <= 0:
            print("change owed: ", total_required + Amount_due)
            break
        print('amount due: ', Amount_due)
    else:
        print("coin not acceptable")
        break



