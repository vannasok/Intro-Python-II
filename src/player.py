# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []
        self.react = ['take', 'drop']

    def __str__(self):
        return(f'\n{self.name}\n@{self.current_room}\nwith items:{self.items}\n')

    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(f"you @ {self.current_room}")
        else:
            print("!!! End of road !!!")

    def action(self, cmd):
        cmdItemList = []
        actionCmd = None
        tokenList = cmd.split()

        for token in tokenList:
            if token in self.react:
                actionCmd = token
            else:
                cmdItemList.append(token.lower())

        if actionCmd == 'take':
            for takeItem in cmdItemList:
                itemTaken = False

                for roomItem in self.current_room.items:
                    if roomItem.name == takeItem:
                        self.items.append(roomItem)
                        itemTaken = roomItem.on_take()
                        break

                if not(itemTaken):
                    print(
                        f'Can not take {takeItem}\n')

        if actionCmd == 'drop':
            for dropItem in cmdItemList:
                itemDropped = False

                for playerItem in self.items:
                    if playerItem.name == dropItem:
                        self.items.remove(playerItem)
                        itemDropped = playerItem.on_drop()
                        break

                if not(itemDropped):
                    print(
                        f'Can not drop {dropItem}\n ')
