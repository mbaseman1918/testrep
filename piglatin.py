import string
answer = "yes"
while answer.lower() == "yes" or answer.lower() == "y":
    word = input("Word? ")
    word_list = list(word)
    if word[0].lower() not in ["a", "e", "i", "o", "u"]:
        for i in word:
            if i not in ["a", "e", "i", "o", "u"]:
                word_list.append(i)
                word_list.remove(i)
            else:
                break
        pig_latin = "".join(word_list) + "ay"
        pig_latin = pig_latin[0].upper() + pig_latin[1:]
        #pig_latin = word[1].upper() + word[2:] + word[0].lower() + "ay"
    elif word[0].lower() in ["i", "a"] and len(word) == 1:
        pig_latin = word.upper() + "yay"
    else:
        pig_latin = word[0].upper() + word[1:] + "yay"
    print(pig_latin)
    answer = input("Would you like to put in another word? ")
