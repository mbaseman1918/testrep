def creditcheck():
    card = input("What is your credit card number? ")
    card_list = []
    modified_card_list = []
    final_card_list = []
    counter = 0
    while len(card) != 16:
        card = input("Sorry that doesn't look like it was put in right.  What is you credit card number? ")
    for i in card[0:15]:
        card_list.append(int(i))
    for i in card_list[::-1]:
        counter += 1
        if counter % 2 == 1:
            modified_card_list.append(i*2)
        if counter % 2 == 0:
            modified_card_list.append(i)
    for i in modified_card_list:
        if i > 9:
            final_card_list.append(i - 9)
        else:
            final_card_list.append(i)
    print(card)
    print(card_list)
    print(modified_card_list)
    print(final_card_list)
    print(sum(final_card_list))
    if str(sum(final_card_list))[1] == card[-1]:
        print("Valid!")
    else:
        print("Card is not valid!!!  The authorities have been alerted criminal.")
creditcheck()
