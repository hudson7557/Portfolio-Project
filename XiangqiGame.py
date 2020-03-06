# Author: Scott Hudson
# Date: 03/04/2020
# Description: This is the Xiangqi game program which contains multiple classes
# for playing the game Xiangqi, also known as Chinese chess.

class XiangqiGame:

    def __init__(self):
        """
        Starts a game of Xiangqi as a list object. The board has a
        coordinate grid with A-I on top and
        1-10 on the left side. Open spaces denoted by a single space " ".
        """

        self._game_state = "UNFINISHED"

        self._board = [[" ", " ", " ", " ", general("black", "E1"), " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [soldier("black", "A4"), " ", soldier("black", "C4"), " ", soldier("black", "E4"), " ", soldier("black", "G4"), " ", soldier("black", "I4")],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [soldier("red", "A7"), " ", soldier("red", "C7"), " ", soldier("red", "E7"), " ", soldier("red", "G7"), " ", soldier("red", "I7")],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", general("red", "E10"), " ", " ", " ", " "]]

        self._convertAlpha = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
                           "G": 6, "H": 7, "I": 8}

        self._convertNum = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5,
                           "7": 6, "8": 7, "9": 8, "10": 9}


    def display_board(self):
        """
        Method for displaying the targeted Xiangqi board
        """
        for line in self._board:
            print(line)

    def make_move(self, target_coordinates, move_to_coordinates):
        """
        This method checks to make sure the move is targeting valid coordinates.
        Once it knows the coordinates are valid it will call the target objects
        movement method and see's if the result is True. If the result is True
        it moves the pieces and returns True.
        :param target_coordinates: string of coordinates
        :param move_to_coordinates: string of coordinates
        :return: True of False
        """

        # make sure the move is targeting a piece on the board using the
        # dictionaries to check if the string is valid or not.
        if target_coordinates[0] not in self._convertAlpha or \
                target_coordinates[1:] not in self._convertNum:
            print("inconceivable!")
            return

        # make sure the coordinates being targets actually contain a piece
        if self._board[self._convertNum[target_coordinates[1:]]][
            self._convertAlpha[target_coordinates[0]]] == " ":
            print("No valid piece in location")
            return

        # make sure the coordinates being moved to are on the board using the
        # dictionaries to check if the string is valid or not.
        if move_to_coordinates[0] not in self._convertAlpha or \
                move_to_coordinates[1:] not in self._convertNum:
            print("Nah dog")
            return

        # make sure the move_to_coordinates are on the board.
        # get the target pieces object
        current_piece = self._board[self._convertNum[target_coordinates[1:]]][
            self._convertAlpha[target_coordinates[0]]]

        # call the target pieces movement ability with the new coordinates
        # each piece contains it's own control flow to check if a move is valid
        # if the move is valid the pieces movement returns true and the piece is
        # moved on the list.
        if current_piece.movement(move_to_coordinates) == True:

            # moves the piece
            self._board[self._convertNum[move_to_coordinates[1:]]][
                self._convertAlpha[move_to_coordinates[0]]] = current_piece

            # the object has been moved in the list and we can change it's old
            # position to an empty space.
            self._board[self._convertNum[target_coordinates[1:]]][
                self._convertAlpha[target_coordinates[0]]] = " "
            return True

        else:
            return False

    def display_character(self, target_coordinates):
        """
        Method to display a piece on the board. Used primarily for checking to
        see if a piece was created accurately.
        :param target_coordinates: coordinates of the target piece
        """
        current_piece = self._board[self._convertNum[target_coordinates[1:]]][
            self._convertAlpha[target_coordinates[0]]]
        print(current_piece._color, current_piece._name,
              current_piece._location, current_piece._character)

    def get_game_state(self):
        """
        Method allowing users to check the current state of the game.
        :return:
        """
        return self._game_state

class game_pieces:
    """
    A super class for all the other game pieces that gets used to streamline
    initializing different pieces.
    """

    def __init__(self, color, location):
        self._color = color
        self._location = location
        self._convertAlpha = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
                           "G": 6, "H": 7}  # used for coordinate translation
        self._convertNum = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5,
                           "7": 6, "8": 7, "9": 8, "10": 9}

class general(game_pieces):
    """
    This class creates a General object, it inherits from game_pieces and adds
    additional data members specific to the General.
    """

    def __init__(self, color, location):
        self._name = "General"
        self._character = "師"
        super().__init__(color, location)

    def movement(self, next_location):
        """
        This is the General's specific movement method. It will check to make
        sure that the input movement is allowed for the General.
        :param next_location: the spot the General is moving to.
        :return: True or False
        """

        # gets the index numbers for an objects location
        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        if self._color == "red":
            # check to make sure the move call is actually changing the location
            if old_x != new_x and old_y != new_y:
                print("You doink")
                return False

            # see if the x axis is changing
            if old_x != new_x:
                if new_x == old_x + 1 or new_x == old_x - 1:
                    # if the x axis is changing we make sure it's only one
                    # space being moved
                    if 3 <= new_x <= 5:
                        # if the move is in the palace the pieces location is
                        # updated and True is returned.
                        self._location = next_location
                        return True
                    else:
                        print("Not allowed")
                        return False
                else:
                    print("Not allowed")
                    return False



            # first we check to see if the y axis is changing
            if old_y != new_y:
                # if y axis is changing we make sure it's only one space moved
                if new_y == old_y + 1 or new_y == old_y - 1:
                    # then we make sure the move is in the palace
                    if  7 <= new_y <= 9:
                        # if the move is in the palace the pieces location is
                        # updated and True is returned.
                        self._location = next_location
                        return True
                    else:
                        print("3")
                        return False
                else:
                    print("2")
                    return False

            else:
                print("1")
                return False

        if self._color == "black":
            # check to make sure the move is not going diagonally
            if old_x != new_x and old_y != new_y:
                print("You doink")
                return False

            # see if the x axis is changing
            if old_x != new_x:
                if new_x == old_x + 1 or new_x == old_x - 1:
                    # if the x axis is changing we make sure it's only one
                    # space being moved
                    if 3 <= new_x <= 5:
                        # if the move is in the palace the pieces location is
                        # updated and True is returned.
                        self._location = next_location
                        return True
                    else:
                        print("Not allowed")
                        return False
                else:
                    print("Not allowed")
                    return False

            # first we check to see if the y axis is changing
            if old_y != new_y:

                # if y axis is changing we make sure it's only one space moved
                if new_y == old_y + 1 or new_y == old_y - 1:

                    # then we make sure the move is in the palace
                    if 0 <= new_y <= 2:

                        # if the move is in the palace the pieces location is
                        # updated and True is returned.
                        self._location = next_location
                        return True
                    else:
                        print("3")
                        return False
                else:
                    print("2")
                    return False

            else:
                print("1")
                return False

class soldier(game_pieces):

    def __init__(self, color, location):
        self._name = "Soldier"
        self._character = "兵"
        super().__init__(color, location)

    def movement(self, next_location):

        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        if self._color == "red":

            # check to see if the red soldier has crossed the river or not.
            if old_y >= 6:

                # we subtract 1 from the old_y axis to make sure the move is
                # only one space and that the piece has moved forward. At this
                # point the soldier can't move left or right which is why there
                # is a check to make sure it maintains it's x value.
                if old_y - 1 == new_y and old_x == new_x:
                    print("moved forward")
                    self._location = next_location
                    return True

                else:
                    print("Nopers")
                    return False
            # if the soldier has crossed the river yet.
            if old_y < 6:

                if old_y - 1 == new_y and old_x == new_x:
                    print("Moved forward")
                    self._location = next_location
                    return True

                if (old_x - 1 == new_x or old_x + 1 == new_x) and\
                        old_y == new_y:
                    self._location = next_location
                    print("Moved left or right")
                    return True
                else:
                    print("Impossible")
                    return False

        if self._color == "black":

            # check to see if the red soldier has crossed the river or not.
            if old_y <= 5: # HAS AN ERROR IN IT HERE, going to work on if when
                # I'm not tired.

                # we subtract 1 from the old_y axis to make sure the move is
                # only one space and that the piece has moved forward. At this
                # point the soldier can't move left or right which is why there
                # is a check to make sure it maintains it's x value.
                if old_y + 1 == new_y and old_x == new_x:
                    print("moved forward")
                    self._location = next_location
                    return True

                else:
                    print("Nopers")
                    return False
            # if the soldier has crossed the river yet.
            if old_y > 5:

                if old_y + 1 == new_y and old_x == new_x:
                    print("Moved forward")
                    self._location = next_location
                    return True

                if (old_x - 1 == new_x or old_x + 1 == new_x) and \
                        old_y == new_y:
                    self._location = next_location
                    print("Moved left or right")
                    return True
                else:
                    print("Impossible")
                    return False

board1 = XiangqiGame()
board1.display_board()
board1.make_move("E1", "E2")
print("break")
board1.display_board()
board1.make_move("A4", "A5") # dope
board1.make_move("A5", "A6") # crossing the river
board1.make_move("A6", "B6") # True, moved one to the right
"""board1.make_move("D5", "D6") # false, backwards
board1.make_move("D5", "D3") # false, more than one space moved.
board1.make_move("D5", "A1") # false, impossible move
board1.make_move("D5", "C5") # true, moved left
board1.make_move("C5", "D5") # true, moved right
board1.make_move("D5", "C4") # false, diagonal move
board1.make_move("D5", "D2") # false, more than one space moved left
board1.make_move("D5", "D10") # false, more than one space moved right"""
board1.display_board()