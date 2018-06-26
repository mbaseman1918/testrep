class Bankaccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amt):
        self.balance += amt
        return "Thank you {}.  You have deposited {}.  Your balance is now {}.".format(self.name,amt,self.balance)
