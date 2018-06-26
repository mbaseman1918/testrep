#Create New Contact
#Retrieve Contact
#Update Existing Contact
#Delete Contact

phonebook = {}
another_use = "yes"
def display():
    for i in phonebook:
        print("\nName: {} {}\nPhone number: ({}) {}-{}\nQuote: {}".format(phonebook[i]["First name"], phonebook[i]["Last name"], phonebook[i]["Phone number"][:3], phonebook[i]["Phone number"][3:6], phonebook[i]["Phone number"][6:], phonebook[i]["Quote"]))

def create():
    firstname = input("What is your first name? ")
    lastname = input("What is your last name? ")
    number = input("What is your phone number? (please enter only digits) ")
    while len(number) != 10 or number.isdigit() != True:
        number = input("Please enter an all digits phone number (number must be 10 digits): ")
    phrase = input("What quote would you like associated with your name? ")
    #password = input("What would you like your password to be? ")
    phonebook[lastname] = {"First name": firstname, "Last name": lastname, "Phone number": number, "Quote": phrase}

def search():
    criteria = input("What is your search criteria?\nFirst name, last name, or phone number?\n")
    while criteria.lower() not in ["first name", "last name", "phone number"]:
        criteria = input("\n \nSorry, I don't recognize that search criteria?\nPlease type one of the following\nfirst name\nlast name\nphone number\n \n What is your search criteria? ")
    search = input("What is the {} of the person you are looking for? ".format(criteria.lower()))
    counter = 0
    for i in phonebook:
        if phonebook[i][criteria.capitalize()] == search:
            print("\nName: {} {}\nPhone number: ({}) {}-{}\nQuote: {}".format(phonebook[i]["First name"], phonebook[i]["Last name"], phonebook[i]["Phone number"][:3], phonebook[i]["Phone number"][3:6], phonebook[i]["Phone number"][6:], phonebook[i]["Quote"]))
            break
        else:
            counter += 1
    if counter == len(phonebook):
        print("Sorry, the information given did not correspond to a listing in this phonebook.")

def update():
    update_firstname = input("What is the first name in the listing you would like to update? ")
    update_lastname = input("What is the last name in the listing you would like to update? ")
    counter = 0
    for i in phonebook:
        if phonebook[i]["First name"] == update_firstname and phonebook[i]["Last name"] == update_lastname:
            update_value = input("What value would you like to update? ")
            while update_value.lower() not in ["first name", "last name", "phone number"]:
                update_value = input("Sorry, I didn't recognize that value.  What value would you like to update? ")
            phonebook[i][update_value.capitalize()] = input("What is the updated information? ")
            while phonebook[i][update_value.capitalize()] == phonebook[i]["Phone number"] and len(phonebook[i][update_value.capitalize()]) != 10:
                phonebook[i][update_value.capitalize()] = input("That phone number looks wrong.  Please enter an all digits phone number (number must be 10 digits): ")
            print("Your information has been updated.")
            print("\nName: {} {}\nPhone number: ({}) {}-{}\nQuote: {}".format(phonebook[i]["First name"], phonebook[i]["Last name"], phonebook[i]["Phone number"][:3], phonebook[i]["Phone number"][3:6], phonebook[i]["Phone number"][6:], phonebook[i]["Quote"]))
            break
        else:
            counter += 1
    if counter == len(phonebook):
        print("Sorry, the information given did not correspond to a listing in this phonebook.")

def delete():
    delete_entry1 = input("What is the first name of the entry you would like to delete? ")
    delete_entry2 = input("What is the last name of the entry you would like to delete? ")
    counter = 0
    for i in phonebook:
        if phonebook[i]["First name"] == delete_entry1 and phonebook[i]["Last name"] == delete_entry2:
            confirmation = input("\n\nThe following listing was found:\nName: {} {}\nPhone number: ({}) {}-{}\nQuote: {}\n\nIs this the listing you want to delete? ".format(phonebook[i]["First name"], phonebook[i]["Last name"], phonebook[i]["Phone number"][:3], phonebook[i]["Phone number"][3:6], phonebook[i]["Phone number"][6:], phonebook[i]["Quote"]))
            while confirmation.lower() not in ["yes", "y", "no", "n"]:
                confirmation = input("Please state yes or no:  ")
            if confirmation.lower() in ["no", "n"]:
                print("That was close.")
                break
            elif confirmation.lower() in ["yes", "y"]:
                del phonebook[i]
                break
        counter +=1
    if counter == len(phonebook):
        print("Sorry, the information given did not correspond to a listing in this phonebook.")

while another_use.lower() in ["yes", "y"]:
    user = input("\nWhat would you like to do?\nCreate a new contact in the phonebook: (create)\nSearch for someone in the phonebook: (search)\nUpdate information in the phonebook: (update)\nDelete a listing in the phonebook: (delete)\nDisplay all listings: (display)\n")
    while user.lower() not in ["create", "search", "update", "delete", "display"]:
        user = input("\n\nSorry I didn't catch that.\nWhat would you like to do?\nCreate a new contact in the phonebook: (create)\nSearch for someone in the phonebook: (search)\nUpdate information in the phonebook: (update)\nDelete a listing in the phonebook: (delete)\nDisplay all listings: (display)\n")
    if user.lower() == "display":
        display()
    elif user.lower() == "create":
        create()
    elif user.lower() == "search":
        search()
    elif user.lower() == "update":
        update()
    elif user.lower() == "delete":
        delete()
    another_use = input("\nWould you like to do anything else with the phonebook? ")
    while another_use.lower() not in ["yes", "y", "no", "n"]:
        another_use = input("\nSorry, I didn't catch that.\nWould you like to do anything else with the phonebook? (yes or no) ")


print("This is the last line of code.")
