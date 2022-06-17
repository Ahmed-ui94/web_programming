fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 50,
    "grapes": 60,
    "honey drew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectrine": 60,
    "orange": 80,
    "peach": 80,
    "pineaple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tagerine": 50,
    "watermelon": 80,
}
for key, valu in fruits.items():
    key.capitalize()

#function to output the calories and take input from user
def main():
    fruit1 = input("Fruit: ")
    if fruit1 in fruits:
        print("item:", fruit1)
        print("calories: ", fruits[fruit1])


main()
