import random


def guessing_game():
    guess_number = random.randint(20, 30)

    number_of_guess = 3
    while number_of_guess > 0:
        user_input = get_userinput()
        if user_input is None:
            raise ValueError("missing name value")
        if user_input > guess_number:
            print("Too high")

        elif user_input < guess_number:
            print("Too low")

        else:
            print("you did it correctly")
            break
        number_of_guess -= 1
    # noticing the user he has utilised his number of chances
    if number_of_guess <= 0:
        print("no more chances")


def get_userinput():
    # checking whether user input is interger
    try:
        user_input = int(input("guess number: "))

    except ValueError:
        print("its not an interger")
    else:
        return user_input


guessing_game()
