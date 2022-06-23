Menu = {
    "Bajo Taco": 4.00,
    "Burito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilli": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilli": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def dish_order():
    while True:
        try:
            item = input("Item: ").capitalize()
            print("Total: ", Menu[item], "$", sep="")
        except (EOFError, KeyError):
            break

dish_order()