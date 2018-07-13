with open("c_list.csv", "r") as f:
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

class person():
    def __init__(self, name, fav_fruit, fav_color):
        self.name = name
        self.fav_fruit = fav_fruit
        self.fav_color = fav_color

    def create(self, contact_dict, headings_list):
        contact_dict[self.name] = {headings[0]: self.name, headings[1]: self.fav_fruit, headings[2]: self.fav_color}

    def retrieve():
        pass

    def update():
        pass

    def delete():
        pass

Frank = person("Frank", "bananas", "blue")
Frank.create(contacts, headings)

print(contacts)
