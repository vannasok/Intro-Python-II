# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.item = []

    def __str__(self):
        return(f"\n{self.name}\n{self.description}\n")

    def add_item(self, item):
        self.item.append(item)

    def print_item(self):
        print("Items in this room: ")
        if len(self.item) > 0:
            for i in self.item:
                print(i.name, i.description)
        else:
            print("There are no items in this room!")
