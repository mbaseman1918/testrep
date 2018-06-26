class ATM:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.interest = .001
        self.transaction = []

    def check_balance(self):
        self.transaction.append("Your current balance is ${}.".format(self.balance))
        return "Your current balance is ${}.".format(self.balance)

    def deposit(self, amt):
        self.balance += amt
        self.transaction.append("Thank you {}.  You have deposited ${}, your current balance is ${}.".format(self.name, amt, self.balance))
        return "Thank you {}.  You have deposited ${}, your current balance is ${}.".format(self.name, amt, self.balance)

    def check_withdrawal(self, amt):
        if self.balance - amt > 0:
            self.transaction.append("Hello {}.  You are able to withdraw ${} from ${}.  The remaining balance will be ${}".format(self.name, amt, self.balance, (self.balance - amt)))
            return "Hello {}.  You are able to withdraw ${} from ${}.  The remaining balance will be ${}".format(self.name, amt, self.balance, (self.balance - amt))
        else:
            self.transaction.append("Hello {}.  You do not have sufficient funds in your account to withdraw ${}.  Your current balance is ${}.".format(self.name, amt, self.balance))
            return "Hello {}.  You do not have sufficient funds in your account to withdraw ${}.  Your current balance is ${}.".format(self.name, amt, self.balance)

    def withdraw(self, amt):
        self.balance -= amt
        self.transaction.append("Thank you {}.  You have withdrawn ${}, your current balance is ${}.".format(self.name, amt, self.balance))
        return "Thank you {}.  You have withdrawn ${}, your current balance is ${}.".format(self.name, amt, self.balance)

    def calc_interest(self):
        interest = self.interest * self.balance
        self.transaction.append("The interest calculated on the account is ${}.".format(interest))
        return "The interest calculated on the account is ${}.".format(interest)

    def transactions(self):
        print("{} the following is your transaction history:\n".format(self.name))
        for i in self.transaction:
            print(i)

accounts = {"matt":ATM("matt")}
print(accounts["matt"].check_balance())
print(accounts["matt"].deposit(100))
print(accounts["matt"].check_withdrawal(20))
print(accounts["matt"].withdraw(20))
print(accounts["matt"].calc_interest())
accounts["matt"].transactions()

def userinterface():
    user = ""
    while user.lower() != "done":
        username = input("What is your name? ")
        while username not in accounts:
            decision = input("That account does not currently exist.  Would you like to create it? ")
            if decision.lower() in ["yes", "y"]:
                accounts[username] = ATM(username)
            else:
                username = input("What is your name? ")
        usertrans = int(input("What would you like to do?\n1 for deposit\n2 for withdrawal check\n3 for withdraw\n4 for check balance\n5 for transaction history\n"))
        if usertrans == 1:
            amount = int(input("What is the amount you would like to deposit? "))
            print(accounts[username].deposit(amount))
        elif usertrans == 2:
            amount = int(input("How much are you planning to withdraw? "))
            print(accounts[username].check_withdrawal(amount))
        elif usertrans == 3:
            amount = int(input("How much would you like to withdraw? "))
            print(accounts[username].withdraw(amount))
        elif usertrans == 4:
            print(accounts[username].check_balance())
        elif usertrans == 5:
            accounts[username].transactions()
        user = input("If you are done type 'done' if not type continue: ")
userinterface()
