# translating  latin words
def pig_latin(word):
   
    if word[0] in "aeiou":
        word = word + "way"
        return word
    else:
        word = word[1:] + word[0] + "ay"
        return word


pig_latin()
