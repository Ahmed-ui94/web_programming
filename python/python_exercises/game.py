import random
# this main function 
def main():
    rand = generate_random()
    user_guess(rand)

# generate random integer and the maximum number 
def generate_random():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise ValueError("its not a positve integer!")
        except ValueError:
            ...
        else:
            break
    number = random.randint(1, level)
    return number
# get user guess and examine its validity
def user_guess(n):
    guess = int(input("Guess: "))
    while True:
        if guess > n:
            print("Too large!")
            guess = int(input("Guess: "))
        elif guess < n:
            print("Too small!")
            guess = int(input("Guess: "))
        else:
            print("just right!")
            break

if __name__ == "__main__":
    main()