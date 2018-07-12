
cards = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10, 'J':10, 'Q':10, 'K':10}
while True:
    first_card = input('What\'s your first card? ')
    second_card = input('What\'s your second card? ')
    third_card = input('What\'s your third card? ')
    total =  cards[first_card] + cards[second_card] + cards[third_card]
    if total > 21:
        print("Already Busted")
    elif total == 21:
        print("Blackjack!")
    elif 21 > total >= 17:
        print("Stay")
    elif 17 > total:
        print("Hit")
