def simplecalculator():
    operator = input("What is the operation you would like to perform? ")
    number1 = input("What is the first number? ")
    number2 = input("What is the second number? ")
    answer = eval("{} {} {}".format(number1, operator, number2))
    print("{} {} {} = {}".format(number1, operator, number2, answer))

def calculator():
    equation = input("What is the function you want to evaluate? ")
    print("{} = {}".format(equation, eval(equation)))

user = input("Would you like to use the simple calculator or the calculator?")
if user == "simple calculator":
    simplecalculator()
if user == "calculator":
    calculator()
