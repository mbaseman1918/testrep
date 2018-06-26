def numbertophrase():
    ones_dict1 = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    ones_dict2 = {0: "", 1: "-one", 2: "-two", 3: "-three", 4: "-four", 5: "-five", 6: "-six", 7: "-seven", 8: "-eight", 9: "-nine"}
    teens_dict1 = {0: "ten", 1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen", 5: "fifteen", 6: "sixteen", 7: "seventeen", 8: "eighteen", 9: "nineteen"}
    teens_dict2 = {0: " and ten", 1: " and eleven", 2: " and twelve", 3: " and thirteen", 4: " and fourteen", 5: " and fifteen", 6: " and sixteen", 7: " and seventeen", 8: " and eighteen", 9: " and nineteen"}
    tens_dict1 = {0: "", 1: "", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    tens_dict2 = {0: "", 1: "", 2: "-twenty", 3: "-thirty", 4: "-forty", 5: "-fifty", 6: "-sixty", 7: "-seventy", 8: "-eighty", 9: "-ninety"}
    number = input("\nWhat is the number you want to convert? ")
    while not number.isdigit():
        number = input("Sorry, please type in a number with digits only: ")
    intnumber = int(number)
    if intnumber == 0:
        print("Zero")
    elif len(number) == 1:
        print("{}".format(ones_dict1[intnumber].capitalize()))
    elif len(number) == 2:
        if int(number[-2]) == 1:
            print("{}".format(teens_dict1[int(number[-1])].capitalize()))
        else:
            print("{}{}".format(tens_dict1[int(number[-2])].capitalize(), ones_dict2[int(number[-1])]))
    elif len(number) == 3:
        if int(number[-2]) == 1:
            print("{}-hundred{}".format(ones_dict1[int(number[-3])].capitalize(), teens_dict2[int(number[-1])]))
        else:
            print("{}-hundred{}{}".format(ones_dict1[int(number[-3])].capitalize(), tens_dict2[int(number[-2])], ones_dict2[int(number[-1])]))


user = "yes"
while user.lower() in ["yes","y"]:
    numbertophrase()
    user = input("\nWould you like to input another number? ")
