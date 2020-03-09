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

        self._board = [
            [Chariot("black", "A1"), Horse("black", "B1"), Elephant("black", "C1"), Advisor("black", "D1"),
             General("black", "E1"), Advisor("black", "F1"), Elephant("black", "G1"), Horse("black", "H1"),
             Chariot("black", "I1")],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", Cannon("red", "B3"), " ", " ", " ", " ", " ",
             Cannon("red", "B8"), " "],
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
            [Chariot("red", "A10"), Horse("red", "B10"), Elephant("red", "C10"), Advisor("red", "D10"),
             General("red", "E10"), Advisor("red", "F10"), Elephant("red", "G10"), Horse("red", "H10"),
             Chariot("red", "I10")]]

        self._convertAlpha = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
                              "G": 6, "H": 7, "I": 8}

        self._convertNum = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5,
                            "7": 6, "8": 7, "9": 8, "10": 9}

        self._player_turn = "red"

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
        # if the move targets the same space the move is considered invalid
        if target_coordinates == move_to_coordinates:
            print("invalid move")
            return False

        # make sure the coordinates being targeted actually contain a piece
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

        # make sure the space the piece is moving to is not holding one of their
        # own pieces.

        # see if the move_to space is occupied
        if self._board[self._convertNum[move_to_coordinates[1:]]][
            self._convertAlpha[move_to_coordinates[0]]] != " ":

            # if the space is occupied we check to make sure it is not a
            # friendly piece in the space
            if current_piece.get_color() == self._board[self._convertNum[
                move_to_coordinates[1:]]][self._convertAlpha[
                move_to_coordinates[0]]].get_color():
                print("Samezies")
                return False

        # call the target pieces movement ability with the new coordinates
        # each piece contains it's own control flow to check if a move is valid
        # if the move is valid the pieces movement returns true and the piece is
        # moved on the list.
        if current_piece.movement(self, move_to_coordinates) == True:

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
        if current_piece == " ":
            print("Space is empty.")
        else:
            print(current_piece._color, current_piece._name,
                  current_piece._location, current_piece._character)

    def get_game_state(self):
        """
        Method allowing users to check the current state of the game.
        :return:
        """
        return self._game_state

    def check_space(self, x_coord, y_coord):
        return self._board[y_coord][x_coord]


class GamePieces:
    """
    A super class for all the other game pieces that gets used to streamline
    initializing different pieces.
    """

    def __init__(self, color, location):
        self._color = color
        self._location = location
        self._convertAlpha = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
                              "G": 6, "H": 7,
                              "I": 8}  # used for coordinate translation
        self._convertNum = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5,
                            "7": 6, "8": 7, "9": 8, "10": 9}

    def get_color(self):
        return self._color


class General(GamePieces):
    """
    This class creates a General object, it inherits from game_pieces and adds
    additional data members specific to the General.
    """

    def __init__(self, color, location):
        self._name = "General"
        self._character = "師"
        super().__init__(color, location)

    def movement(self, board, next_location):
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
                    if 7 <= new_y <= 9:
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


class Soldier(GamePieces):

    def __init__(self, color, location):
        self._name = "Soldier"
        self._character = "兵"
        super().__init__(color, location)

    def movement(self, board, next_location):

        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        if self._color == "red":

            # check to see if the red soldier has crossed the river or not.
            if old_y >= 5:

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
            if old_y <= 4:

                if old_y - 1 == new_y and old_x == new_x:
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

        if self._color == "black":

            # check to see if the red soldier has crossed the river or not.
            if old_y <= 4:

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
            if old_y >= 5:

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


class Chariot(GamePieces):

    def __init__(self, color, location):
        self._name = "Chariot"
        self._character = "車"
        super().__init__(color, location)

    def movement(self, board, next_location):

        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        # moving left?
        if old_x > new_x and old_y == new_y:
            space = old_x
            while space != new_x:
                space -= 1
                if board.check_space(space, old_y) != " ":
                    if board.check_space(space, old_y).get_color() != \
                            self.get_color():
                        if space == new_x:
                            print("Take a piece")
                            self._location = next_location
                            return True
                        if space != new_x:
                            print("An opponents piece is in your way, "
                                  "try moving on to their space")
                            return False
                    else:
                        print("Same team!")
                        return False
            self._location = next_location
            return True

        # moving right?
        if old_x < new_x and old_y == new_y:
            space = old_x
            while space != new_x:
                space += 1
                if board.check_space(space, old_y) != " ":
                    if board.check_space(space, old_y).get_color() != \
                            self.get_color():
                        if space == new_x:
                            print("Take a piece")
                            self._location = next_location
                            return True
                        if space != new_x:
                            print("An opponents piece is in your way, "
                                  "try moving on to their space")
                            return False
                    else:
                        print("Same team!")
                        return False
            self._location = next_location
            print("Alonsy")
            return True

        # moving forward?
        if old_y > new_y and old_x == new_x:
            space = old_y
            while space != new_y:
                space -= 1
                if board.check_space(old_x, space) != " ":
                    if board.check_space(old_x, space).get_color() != \
                            self.get_color():
                        if space == new_y:
                            print("Take a piece")
                            self._location = next_location
                            return True
                        if space != new_y:
                            print("An opponents piece is in your way, "
                                  "try moving on to their space")
                            return False
                    else:
                        print("Same team!")
                        return False
            self._location = next_location
            print("Alonsy 2")
            return True

        # moving backwards?
        if old_y < new_y and old_x == new_x:
            space = old_y
            while space != new_y:
                space += 1
                if board.check_space(old_x, space) != " ":
                    if board.check_space(old_x, space).get_color() != \
                            self.get_color():
                        if space == new_y:
                            print("Take a piece")
                            self._location = next_location
                            return True
                        if space != new_y:
                            print("An opponents piece is in your way, "
                                  "try moving on to their space")
                            return False
                    else:
                        print("Same team!")
                        return False
            self._location = next_location
            print("Alonsy 3")
            return True

        else:
            print("False")
            return False


class Cannon(GamePieces):

    def __init__(self, color, location):
        self._name = "Cannon"
        self._character = "炮"
        super().__init__(color, location)

    def movement(self, board, next_location):

        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        # moving forwards?
        if old_y > new_y and old_x == new_x:
            space = old_y
            piece_counter = 0

            # if the move is not capturing something
            if board.check_space(new_x, new_y) == " ":
                # the while loop check to make sure nothing is in the way since
                # this is a non-capture move
                while space != new_y:
                    space -= 1
                    # if a space is not an empty space the move cannot be
                    # completed and false is returned.
                    if board.check_space(old_x, space) != " ":
                        print("A piece is in your way, you cannot jump a piece"
                              "unless you are capturing.")
                        return False
                # if all the spaces are empty the false statement never triggers
                # and we return true.
                print("Yes")
                self._location = next_location
                return True

            # if the move is a capture move
            if board.check_space(new_x, new_y) != " ":
                # first check the color, if they are different we check for a
                # jump, if it's friendly we return false.
                if board.check_space(new_x, new_y).get_color() != \
                        self.get_color():
                    # while loop checks to see how many pieces are in between
                    # the start and end (A to B) we take 1 off the new_y because
                    # we don't want to count the piece to be taken.
                    while space != new_y + 1:
                        space -= 1
                        # the number of pieces inbetween are tracked by
                        # incrementing the piece_counter
                        if board.check_space(old_x, space) != " ":
                            piece_counter += 1
                    # once the while loop is complete we check if there is only
                    # one piece, if there is only 1 the move goes through
                    if piece_counter == 1:
                        print("TAKE THE ENEMY")
                        self._location = next_location
                        return True
                    # if there is more than one piece to jump we return false.
                    else:
                        print("Can't jump more than one piece.")
                        return False

                else:
                    print("That's your own piece")
                    return False
        # moving backwards?
        if old_y < new_y and old_x == new_x:
            space = old_y
            piece_counter = 0

            # if the move is not capturing something
            if board.check_space(new_x, new_y) == " ":
                # the while loop check to make sure nothing is in the way since
                # this is a non-capture move
                while space != new_y:
                    space += 1
                    # if a space is not an empty space the move cannot be
                    # completed and false is returned.
                    if board.check_space(old_x, space) != " ":
                        print("A piece is in your way, you cannot jump a piece"
                              "unless you are capturing.")
                        return False
                # if all the spaces are empty the false statement never triggers
                # and we return true.
                self._location = next_location
                print("yes")
                return True

            # if the move is a capture move
            if board.check_space(new_x, new_y) != " ":
                # first check the color, if they are different we check for a
                # jump, if it's friendly we return false.
                if board.check_space(new_x, new_y).get_color() != \
                        self.get_color():
                    # while loop checks to see how many pieces are in between
                    # the start and end (A to B) we take 1 off the new_y because
                    # we don't want to count the piece to be taken.
                    while space != new_y - 1:
                        space += 1
                        # the number of pieces inbetween are tracked by
                        # incrementing the piece_counter
                        if board.check_space(old_x, space) != " ":
                            piece_counter += 1
                    # once the while loop is complete we check if there is only
                    # one piece, if there is only 1 the move goes through
                    if piece_counter == 1:
                        print("TAKE THE ENEMY")
                        self._location = next_location
                        return True
                    # if there is more than one piece to jump we return false.
                    else:
                        print("Can't jump more than one piece.")
                        return False

                else:
                    print("That's your own piece")
                    return False

        # moving right?
        if old_x < new_x and old_y == new_y:
            space = old_x
            piece_counter = 0

            # if the move is not capturing something
            if board.check_space(new_x, new_y) == " ":
                # the while loop check to make sure nothing is in the way since
                # this is a non-capture move
                while space != new_x:
                    space += 1
                    # if a space is not an empty space the move cannot be
                    # completed and false is returned.
                    if board.check_space(space, old_y) != " ":
                        print("A piece is in your way, you cannot jump a piece"
                              "unless you are capturing.")
                        return False
                # if all the spaces are empty the false statement never triggers
                # and we return true.
                self._location = next_location
                print("yes")
                return True

            # if the move is a capture move
            if board.check_space(new_x, new_y) != " ":
                # first check the color, if they are different we check for a
                # jump, if it's friendly we return false.
                if board.check_space(new_x, new_y).get_color() != \
                        self.get_color():
                    # while loop checks to see how many pieces are in between
                    # the start and end (A to B) we take 1 off the new_y because
                    # we don't want to count the piece to be taken.
                    while space != new_x - 1:
                        space += 1
                        # the number of pieces inbetween are tracked by
                        # incrementing the piece_counter
                        if board.check_space(space, old_x) != " ":
                            piece_counter += 1
                    # once the while loop is complete we check if there is only
                    # one piece, if there is only 1 the move goes through
                    if piece_counter == 1:
                        print("TAKE THE ENEMY")
                        self._location = next_location
                        return True
                    # if there is more than one piece to jump we return false.
                    else:
                        print("Can't jump more than one piece.")
                        return False

                else:
                    print("That's your own piece")
                    return False
        # moving left?
        if old_x > new_x and old_y == new_y:
            space = old_x
            piece_counter = 0

            # if the move is not capturing something
            if board.check_space(new_x, new_y) == " ":
                # the while loop check to make sure nothing is in the way since
                # this is a non-capture move
                while space != new_x:
                    space -= 1
                    # if a space is not an empty space the move cannot be
                    # completed and false is returned.
                    if board.check_space(space, old_y) != " ":
                        print("A piece is in your way, you cannot jump a piece"
                              "unless you are capturing.")
                        return False
                # if all the spaces are empty the false statement never triggers
                # and we return true.
                self._location = next_location
                print("yes")
                return True

            # if the move is a capture move
            if board.check_space(new_x, new_y) != " ":
                # first check the color, if they are different we check for a
                # jump, if it's friendly we return false.
                if board.check_space(new_x, new_y).get_color() != \
                        self.get_color():
                    # while loop checks to see how many pieces are in between
                    # the start and end (A to B) we take 1 off the new_y because
                    # we don't want to count the piece to be taken.
                    while space != new_x + 1:
                        space -= 1
                        # the number of pieces inbetween are tracked by
                        # incrementing the piece_counter
                        if board.check_space(space, old_y) != " ":
                            piece_counter += 1
                    # once the while loop is complete we check if there is only
                    # one piece, if there is only 1 the move goes through
                    if piece_counter == 1:
                        print("TAKE THE ENEMY")
                        self._location = next_location
                        return True
                    # if there is more than one piece to jump we return false.
                    else:
                        print("Can't jump more than one piece.")
                        return False

                else:
                    print("That's your own piece")
                    return False
        else:
            print("Because")
            return False


class Advisor(GamePieces):

    def __init__(self, color, location):
        self._name = "Advisor"
        self._character = "仕"
        super().__init__(color, location)

    def movement(self, board, next_location):
        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        if self._color == "red":
            # check to make sure the move to space is within the palace
            if 7 <= new_y <= 9 and 3 <= new_x <= 5:
                # if the piece is moving up & right
                if old_x + 1 == new_x and old_y - 1 == new_y:
                    self._location = next_location
                    print("Moved completed")
                    return True

                # if the piece is moving down & right
                if old_x + 1 == new_x and old_y + 1 == new_y:
                    self._location = next_location
                    print("Moved homie")
                    return True
                # if the piece is moving down & left
                if old_x - 1 == new_x and old_y + 1 == new_y:
                    self._location = next_location
                    print("Moved homie")
                    return True
                # if the piece is moving up & left
                if old_x - 1 == new_x and old_y - 1 == new_y:
                    self._location = next_location
                    print("Moved homie")
                    return True
                else:
                    print("Not a valid move with the Advisor")
            else:
                print("OB")
                return False

        if self._color == "black":
            # check to make sure the move to space is within the palace
            if 0 <= new_y <= 2 and 3 <= new_x <= 5:
                # if the piece is moving up & right
                if old_x + 1 == new_x and old_y - 1 == new_y:
                    self._location = next_location
                    print("Moved completed")
                    return True

                # if the piece is moving down & right
                if old_x + 1 == new_x and old_y + 1 == new_y:
                    self._location = next_location
                    print("Moved homie")
                    return True
                # if the piece is moving down & left
                if old_x - 1 == new_x and old_y + 1 == new_y:
                    self._location = next_location
                    print("Moved homie")
                    return True
                # if the piece is moving up & left
                if old_x - 1 == new_x and old_y - 1 == new_y:
                    self._location = next_location
                    print("Moved homie")
                    return True
                else:
                    print("Not a valid move with the Advisor")
            else:
                print("OB")
                return False


class Elephant(GamePieces):

    def __init__(self, color, location):
        self._name = "Elephant"
        self._character = "相"
        super().__init__(color, location)

    def movement(self, board, next_location):
        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        if self._color == "red":

            # check to make sure the move to space is on the red side
            if 5 <= new_y <= 9:

                # if the piece is moving up & right
                if old_x + 2 == new_x and old_y - 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x + 1, old_y - 1) != " ":
                        print("A piece is in your way, you cannot jump a "
                             "piece")
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        self._location = next_location
                        print("piece taken")
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        self._location = next_location
                        print("Move completed")
                        return True

                # if the piece is moving up & left
                if old_x - 2 == new_x and old_y - 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x - 1, old_y - 1) != " ":
                        print(
                            "A piece is in your way, you cannot jump a "
                            "piece")
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        self._location = next_location
                        print("piece taken")
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        self._location = next_location
                        print("Move completed")
                        return True

                # if the piece is moving down & right
                if old_x + 2 == new_x and old_y + 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x + 1, old_y + 1) != " ":
                        print(
                            "A piece is in your way, you cannot jump a "
                            "piece")
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        self._location = next_location
                        print("piece taken")
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        self._location = next_location
                        print("Move completed")
                        return True

                # if the piece is moving down & left
                if old_x - 2 == new_x and old_y + 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x - 1, old_y + 1) != " ":
                        print(
                            "A piece is in your way, you cannot jump a "
                            "piece")
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        self._location = next_location
                        print("piece taken")
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        self._location = next_location
                        print("Move completed")
                        return True

                # not a valid diagonal move
                else:
                    print("Not a 2 space diagonal move")
                    return False

            # out of bounds
            else:
                print("Out of bounds for the Red Elephants")
                return False

        if self._color == "black":

            # check to make sure the move to space is on the red side
            if 0 <= new_y <= 4:

                # if the piece is moving up & right
                if old_x + 2 == new_x and old_y - 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x + 1, old_y - 1) != " ":
                        print("A piece is in your way, you cannot jump a "
                             "piece")
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        self._location = next_location
                        print("piece taken")
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        self._location = next_location
                        print("Move completed")
                        return True

                # if the piece is moving up & left
                if old_x - 2 == new_x and old_y - 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x - 1, old_y - 1) != " ":
                        print(
                            "A piece is in your way, you cannot jump a "
                            "piece")
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        self._location = next_location
                        print("piece taken")
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        self._location = next_location
                        print("Move completed")
                        return True

                # if the piece is moving down & right
                if old_x + 2 == new_x and old_y + 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x + 1, old_y + 1) != " ":
                        print(
                            "A piece is in your way, you cannot jump a "
                            "piece")
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        self._location = next_location
                        print("piece taken")
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        self._location = next_location
                        print("Move completed")
                        return True

                # if the piece is moving down & left
                if old_x - 2 == new_x and old_y + 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x - 1, old_y + 1) != " ":
                        print(
                            "A piece is in your way, you cannot jump a "
                            "piece")
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        self._location = next_location
                        print("piece taken")
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        self._location = next_location
                        print("Move completed")
                        return True

                # not a valid diagonal move
                else:
                    print("Not a 2 space diagonal move")
                    return False

            # out of bounds
            else:
                print("Out of bounds for Black Elephants")
                return False


class Horse(GamePieces):
    def __init__(self, color, location):
        self._name = "Horse"
        self._character = "馬"
        super().__init__(color, location)

    def movement(self, board, next_location):
        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        # if the piece is moving forward
        if old_y - 2 == new_y:

            # check the space one above the current location
            if board.check_space(old_x, old_y - 1) != " ":
                print("A piece is in your way")
                return False

            # check to see if the space is occupied, since friendly fire is
            # handled by make_move() we know that if it isn't empty it must be
            # an opponents piece
            if board.check_space(new_x, new_y) != " ":
                print("Piece taken")
                self._location = next_location
                return True

            # if the space is empty then it's just a simple movement.
            else:
                print("Move successful")
                self._location = next_location
                return True
        else:
            print("hello")

""" 
       if old_y - 2 == new_y:
        
        if old_x + 2 == new_x:
            
        if old_x - 2 == new_x: """

#for testing horsies
board1 = XiangqiGame()
board1.display_board()
board1.make_move("B10", "C8") # true, moved forward right
board1.display_board()