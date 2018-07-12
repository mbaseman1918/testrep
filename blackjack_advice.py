cards1 = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10, 'J':10, 'Q':10, 'K':10}
cards2 = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10, 'J':10, 'Q':10, 'K':10}
first_card = input('What\'s your first card? ')
second_card = input('What\'s your second card? ')
if cards1[first_card] != 11:
    print("Your card is not an Ace.")
total1 = cards1[first_card] + cards1[second_card]
total2 = cards1[first_card] + cards2[second_card]
total3 = cards2[first_card] + cards1[second_card]
total4 = cards2[first_card] + cards2[second_card]
totals = [total1, total2, total3, total4]
for i in totals:
    if i > 21:
        print("Already busted.")
    elif i == 21:
        pass
    elif 21 > i >= 17:
        pass
    elif 17 > i:
        pass
