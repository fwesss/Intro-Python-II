from room import Room
from player import Player

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
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
        self.valid_move = True

    def quit_game(self):
        print("\nThanks for playing!\n")
        self.playing = False


if __name__ == "__main__":
    name = input("What is your name?\n")
    player = Player(name, room["outside"])
    print(f"\nWelcome {player.name}!\n")

    game = Game()
    choices = {
        "n": player.move("north", game),
        "e": player.move("east", game),
        "s": player.move("south", game),
        "w": player.move("west", game),
        "q": game.quit_game,
    }

    while game.playing:
        if game.valid_move:
            print(f"\n{player.current_room.name}")
            print(f"{player.current_room.description}\n")

        choice = input(
            "Where do you want to go?\n[n]orth [e]ast [s]outh [w]est or [q]uit"
        )
        if choice not in choices:
            print("\nPlease choose a valid action.\n")
            game.valid_move = False
        else:
            choices[choice]()
