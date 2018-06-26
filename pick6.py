import random
def pick6():
    x = []
    for i in range(6):
        number = str(random.randint(1,99))
        x.append(number)
    return x

def num_matches(winning, ticket):
    counter = 0
    cash_dict = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
    if winning[0] == ticket[0]:
        counter += 1
    if winning[1] == ticket[1]:
        counter += 1
    if winning[2] == ticket[2]:
        counter += 1
    if winning[3] == ticket[3]:
        counter += 1
    if winning[4] == ticket[4]:
        counter += 1
    if winning[5] == ticket[5]:
        counter += 1
    if counter > 2:
        print(ticket)
    cash = cash_dict[counter]
    return cash

winning_ticket = pick6()
print("\nThe winning ticket numbers are {}\n".format(winning_ticket))
earnings = 0
expense = 0
for i in range(100000):
    expense += 2
    bought_ticket = pick6()
    earnings += num_matches(winning_ticket, bought_ticket)
balance = earnings - expense
print("\nYour expenses were {}.\n".format(expense))
print("Your earnings were {}.\n".format(earnings))
print("Your ending balance is {}.\n".format(balance))
print("Your ROI is {}%.\n".format((balance/expense)*100))
