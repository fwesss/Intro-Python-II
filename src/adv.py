from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    "outside": Room(
        "Outside Cave Entrance", "North of you, the cave mount beckons", []
    ),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
        [Item("Pants", "A necessity for any proper adventurer")],
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        [
            Item("Sword", "A sharp blade"),
            Item("Shield", "Capable of stopping enemy attacks"),
        ],
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
        [Item("Helmet", "Protects the head")],
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        [Item("Gold", "Lots of gold")],
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]


class Game:
    def __init__(self):
        self.playing = True
        self.valid_action = True

    def quit_game(self):
        print("\nThanks for playing!\n")
        self.playing = False


if __name__ == "__main__":
    name = input("What is your name?\n")
    player = Player(
        name, room["outside"], [Item("Shirt", "Provides mild protection from elements")]
    )
    print(f"\nWelcome {player.name}!\n")

    game = Game()

    while game.playing:
        if game.valid_action:
            print(f"\n{player.current_room.name}")
            print(f"{player.current_room.description}\n")

            if len(player.current_room.items) > 0:
                print("Items in the room:")
                for item in player.current_room.items:
                    print(item.name)
                    print(item.description)
            else:
                print("There is nothing in this room.")

        action = input(
            "\nWhat do you want to do?\n"
            "Go [n]orth, [e]ast, [s]outh, or [w]est,\n"
            "[get] | [take] or [drop] 'item',\n"
            "[i] | [inventory],\n"
            "[q]uit\n"
        )

        verb = action.split(" ")[0]
        item = None
        if len(action.split(" ")) > 1:
            item = action.split(" ")[1]

        actions = {
            "n": player.move("north", game),
            "e": player.move("east", game),
            "s": player.move("south", game),
            "w": player.move("west", game),
            "get": player.take(item, game),
            "take": player.take(item, game),
            "drop": player.drop(item, game),
            "i": player.view_inventory,
            "inventory": player.view_inventory,
            "q": game.quit_game,
        }

        if verb not in actions:
            print("\nPlease choose a valid action.\n")
            game.valid_action = False
        else:
            actions[verb]()
