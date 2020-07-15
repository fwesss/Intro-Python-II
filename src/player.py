from room import Room


class Player:
    def __init__(self, name: str, current_room: Room):
        self.name = name
        self.current_room = current_room

    def move(self, direction, game):
        def commit():
            directions = {
                "north": self.current_room.n_to,
                "east": self.current_room.e_to,
                "south": self.current_room.s_to,
                "west": self.current_room.w_to,
            }

            if directions[direction] is not None:
                self.current_room = directions[direction]
                game.valid_move = True
            else:
                print(f"\nThere is nothing {direction} of you.\n")
                game.valid_move = False

        return commit
