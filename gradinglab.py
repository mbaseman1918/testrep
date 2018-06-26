number_grade = int(input("What is your number grade? "))
while number_grade not in range(0,101):
    print("Sorry, I didn't catch that.  What is your number grade? ")
    number_grade = int(input("What is your number grade? "))
modifier = "not assigned"
if number_grade == 100:
    letter = "A"
    modifier = "+"
elif number_grade >= 90:
    letter = "A"
elif number_grade >= 80:
    letter = "B"
elif number_grade >= 70:
    letter = "C"
elif number_grade >= 60:
    letter = "D"
elif number_grade >= 50:
    letter = "F"
elif number_grade >= 0:
    letter = "F"
    modifier = "-"
while modifier == "not assigned":
    if number_grade % 10 >= 7:
        modifier = "+"
    elif number_grade % 10 >= 4:
        modifier = ""
    elif number_grade % 10 >= 0:
        modifier = "-"
print("You got a " + letter + modifier +".")
