class game_pieces:

    def __init__(self, color, location):
        self._color = color
        self._location = location
        self._converter = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
                           "G": 6, "H": 7}


    def display_character(self):
        print(self._name, self._location, self._color)




class general(game_pieces):

    def __init__(self, color, location):
        self._name = "General"
        super().__init__(color, location)

    def movement(self, next_location):
        old_x = self._converter[self._location[0]]
        old_y = self._location[1]
        new_x = self._converter[next_location[0]]
        new_y = next_location[1]
        print(old_x, old_y, new_x, new_y)


if old_x - 1 == new_x and old_y - 1 == new_y:
    if board.check_space(new_x, new_y) != " ":
        if self.get_color() != \
                board.check_space(new_x, new_y).get_color():
            self._location = next_location
            print("Piece taken")
            return True
        else:
            print("Can't take your own piece!")
            return False
    else:
        self._location = next_location
        print("Moved homie")
        return True

general = general("black", "D9")
general.display_character()
general.movement("E9")

if self._color == "red":
    # check to make sure the move to space is on the red side
    if 5 <= new_y <= 9:
        # if the piece is moving up & right
        if old_x + 2 == new_x and old_y - 2 == new_y:
            space = old_x
            expanse = old_y
            # check if the space in between the start and end point is
            # occupied.
            space += 1
            expanse -= 1
            # if the space is occupied the move cannot be completed
            if board.check_space(space, expanse) != " ":
                print("A piece is in your way, you cannot jump a "
                      "piece")
                return False
            # if the space being moved into is occupied we track that
            # a piece was taken
            if board1.check_space(new_x, new_y) != " ":
                self._location = next_location
                print("piece taken")
                return True
            # if the space is not occupied it's just a movement
            else:
                self._location = next_location
                print("Move completed")
                return True