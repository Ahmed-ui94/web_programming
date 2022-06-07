# translating  latin words
def pig_latin():
    word = input("word: ").lower()
    if word[0] in "aeiou":
        word = word + "way"
    else:
        word = word[1:] + word[0] + "ay"
    print(word.capitalize())


pig_latin()
