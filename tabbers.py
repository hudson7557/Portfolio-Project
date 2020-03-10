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


                # moves the piece
                self._board[self._convertNum[move_to_coordinates[1:]]][
                    self._convertAlpha[move_to_coordinates[0]]] = current_piece

                # the object has been moved in the list and we can change it's old
                # position to an empty space.
                self._board[self._convertNum[target_coordinates[1:]]][
                    self._convertAlpha[target_coordinates[0]]] = " "

                # change who's turn it is
                if current_piece.get_color().lower() == 'red':
                    self._player_turn = 'black'
                if current_piece.get_color().lower() == 'black':
                    self._player_turn = 'red'
                return True

        self._board = [
            [Chariot("black", "A1"), Horse("black", "B1"),
             Elephant("black", "C1"), Advisor("black", "D1"),
             General("black", "E1"), Advisor("black", "F1"),
             Elephant("black", "G1"), Horse("black", "H1"),
             Chariot("black", "I1")],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", Cannon("black", "B3"), " ", " ", " ", " ", " ",
             Cannon("black", "H3"), " "],
            [Soldier("black", "A4"), " ", Soldier("black", "C4"), " ",
             Soldier("black", "E4"), " ", Soldier("black", "G4"), " ",
             Soldier("black", "I4")],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [Soldier("red", "A7"), " ", Soldier("red", "C7"), " ",
             Soldier("red", "E7"), " ", Soldier("red", "G7"), " ",
             Soldier("red", "I7")],
            [" ", Cannon("red", "B8"), " ", " ", " ", " ", " ",
             Cannon("red", "H8"), " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [Chariot("red", "A10"), Horse("red", "B10"), Elephant("red", "C10"),
             Advisor("red", "D10"),
             General("red", "E10"), Advisor("red", "F10"),
             Elephant("red", "G10"), Horse("red", "H10"),
             Chariot("red", "I10")]]


        if current_piece.get_name() in ["General", "Chariot", "Cannon",
                                        "Elephant", "Horse"]:
            # the movement for these four is passed the board, and the
            # move_to_coordinates
            if current_piece.movement(self, move_to_coordinates) == True:

                # check to see if the general is the piece being taken
                if self._board[self._convertNum[
                move_to_coordinates[1:]]][self._convertAlpha[
                move_to_coordinates[0]]].get_name() == "General":

                    # the game state is changed to reflect which ever color took
                    # a general has won
                    self._game_state = current_piece.get_color().upper() + \
                                       "_WON"

                # if the movement is valid for the piece _move_completion is
                # called which handles the actual movement of the piece within
                # the board.
                self._move_completion(target_coordinates, move_to_coordinates,
                                      current_piece)
            # if the move cannot be completed by the piece make_move() returns
            # false.
            else:
                return False