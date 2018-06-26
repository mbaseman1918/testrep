answer = "yes"
import random
while answer.lower() == "yes" or answer == "y":
    word1 = input("Give me a name: ")
    word2a = input("Give me an adjective: ")
    word2b = input("Give me an adjective: ")
    word2c = input("Give me an adjective: ")
    word3 = input("Give me a noun: ")
    word_list = [word2a, word2b, word2c]
    print("Please excuse {} who is far too {} to attend {} class.".format(word1, word_list[random.randint(0,2)], word3))
    answer = input("Would you like to play again? ")
    while answer != "yes" and answer != "no":
        input("Sorry, I didn't quite catch that.  Did you want to play again? ")
print("Thank you for playing my mad libs game.")
