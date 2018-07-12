class person(object):
    def __init__(self, name, fav_fruit, fav_color):
        self.name = name
        self.fav_fruit = fav_fruit
        self.fav_color = fav_color

with open("c_list.csv", "r") as f:
    lines = f.read().split("\n")
    lines = lines[:-1]
    print(lines)
    # book = f.read()
    # print(book)
contacts = []
