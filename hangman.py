import random
with open("english.txt") as f:
    word_list = f.read()
ref_word_list = word_list.split()
final_list = []
for i in ref_word_list:
    if len(i) < 5:
        continue
    else:
        final_list.append(i)
def hangman():
    word = random.choice(final_list)
    blanks = []
    for i in word:
        blanks.append("_ ")
    print("".join(blanks))
    guesses = 10
    prev_guess = []
    while guesses > 0:
        user = input("What is your guess? ")
        while not (user.isalpha() and len(user) == 1):
            user = input("What is your guess? ")
        while user in prev_guess:
            user = input("You already guessed that.  What is your guess? ")
        prev_guess.append(user)
        counter = 0
        tracker = 0
        for i in word:
            if user == i:
                blanks[counter] = i
            else:
                tracker += 1
            counter += 1
        print("".join(blanks))
        if "_ " not in blanks:
            return "You win!  You had {} guesses left.".format(guesses)
        if tracker == len(word):
            guesses -= 1
        print(guesses)
    if guesses == 0:
        return "You lost.  The word was {}.".format(word)

play = "yes"
while play.lower() in ["yes", "y"]:
    print(hangman())
    play = input("Would you like to play again? ")
