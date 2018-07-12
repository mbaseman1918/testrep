class person(object):
    def __init__(self, name, fav_fruit, fav_color):
        self.name = name
        self.fav_fruit = fav_fruit
        self.fav_color = fav_color

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
print(contacts)
