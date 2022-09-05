def main():
    player1 = computer_score(input("player1: "))
    player2 = computer_score(input("player2: "))

    # compare and print the
    if player1 > player2:
        print("player1 wins!")
    else:
        print("player2 wins!")


# function to compute the syllables in the word
def computer_score(word):
    dict = {
        "a": 1,
        "b": 3,
        "c": 3,
        "d": 2,
        "e": 1,
        "f": 4,
        "g": 2,
        "h": 4,
        "i": 1,
        "j": 8,
        "k": 5,
        "l": 1,
        "m": 3,
        "n": 1,
        "o": 1,
        "p": 3,
        "q": 10,
        "r": 1,
        "s": 1,
        "t": 1,
        "u": 1,
        "v": 4,
        "w": 4,
        "x": 8,
        "y": 4,
        "z": 10,
    }
    list1 = [dict[i] for i in word.lower() if i.isalpha()]

    return sum(list1)


if __name__ == "__main__":
    main()
