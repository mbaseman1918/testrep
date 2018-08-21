
class contactlist():
    def __init__(self, contact_list):

        with open(contact_list, "r") as f:
            lines = f.read().split("\n")
            lines = lines[:-1]
            headings = lines[0].split(",")
            print(headings)
            print(lines)
            # book = f.read()
            # print(book)
            contacts = {}
            for object in lines[1:]:
                print(object)
                index = object.split(",")[0]
                counter = 0
                contacts[index] = {}
                for item in object.split(","):
                    print(item)
                    contacts[index][headings[counter]] = item
                    counter += 1
        self.contacts = contacts
        self.headings = headings

    def create(self):
        name = input("What is the name of the person? ")
        fav_fruit = input("What is this person's favorite fruit? ")
        fav_color = input("What is this person's favorite color? ")
        self.contacts[name] = {self.headings[0]: name, self.headings[1]: fav_fruit, self.headings[2]: fav_color}
        return f"\nThe following information has been added to the contact list:\n {self.contacts[name]}\n"

    def retrieve():
        name = input("What is the name of the person? ")
        return f"\nThe following information is associated with {name}"

    def update():
        name = input("What is the name of the person? ")
        trait = input("What is the trait you would like to update? ")

    def delete():
        name = input("What is the name of the contact you would like to delete? ")

contact_book = contactlist("c_list.csv")
print(contact_book.create())
print(contact_book.contacts)
