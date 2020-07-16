from typing import List


class Player:
    def __init__(self, name: str, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def move(self, direction: str, game):
        def commit():
            directions = {
                "north": self.current_room.n_to,
                "east": self.current_room.e_to,
                "south": self.current_room.s_to,
                "west": self.current_room.w_to,
            }

            if directions[direction] is not None:
                self.current_room = directions[direction]
                game.valid_action = True
            else:
                print(f"\nThere is nothing {direction} of you.\n")
                game.valid_action = False

        return commit

    def take(self, item_name: str, game):
        def commit():
            if item_name is None:
                print("\nPlease select an item.")
                game.valid_action = False
            elif item_name in [item.name for item in self.current_room.items]:
                active_item = next(
                    (
                        item
                        for item in self.current_room.items
                        if item.name == item_name
                    ),
                    None,
                )
                self.items.append(active_item)
                self.current_room.items.remove(active_item)
                active_item.on_take()
                game.valid_action = True
            else:
                print(f"There is no {item_name} in this room.")
                game.valid_action = False

        return commit

    def drop(self, item_name, game):
        def commit():
            if item_name is None:
                print("\nPlease select an item")
                game.valid_action = False
            elif item_name in [item.name for item in self.items]:
                active_item = next(
                    (item for item in self.items if item.name == item_name), None
                )
                self.current_room.items.append(active_item)
                self.items.remove(active_item)
                active_item.on_drop()
                game.valid_action = True
            else:
                print(f"There is no {item_name} in your inventory.")
                game.valid_action = False

        return commit

    def view_inventory(self):
        if len(self.items) > 0:
            print("You have:")
            for item in self.items:
                print(item.name)
        else:
            print("There is nothing in your inventory.")
