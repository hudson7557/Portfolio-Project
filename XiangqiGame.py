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

        # converters contain both the capital and lower case to allow for
        # flexibility. It also allows us to not use .upper() on all comparisons
        # which saves some code
        self._convertAlpha = {"A": 0, "a": 0, "B": 1, "b": 1, "C": 2, "c": 2,
                              "D": 3, "d": 3, "E": 4, "e": 4, "F": 5, "f": 5,
                              "G": 6, "g": 6, "H": 7, "h": 7, "I": 8, "i": 8}

        self._convertNum = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5,
                            "7": 6, "8": 7, "9": 8, "10": 9}

        self._player_turn = "red"

        self._black_check = False

        self._red_check = False

        self._red_piece_list = [piece for list_1 in self._board for piece in
                                list_1 if piece != " " if piece.get_color()
                                == "red"]

        self._black_piece_list = [piece for list_1 in self._board for piece in
                                  list_1 if piece != " " if piece.get_color()
                                  == "black"]

        self._black_general_location = "E1"

        self._red_general_location = "E10"

    def display_board(self):
        """
        Method for displaying the targeted Xiangqi board
        """

        for line in self._board:
            print(line)

    def make_move(self, target_coordinates, move_to_coordinates):
        """
        This method handles general movement validation for a piece. If checks
        all the precondition to make sure the move is potentially valid, then
        calls a pieces specific movement to see if the move is valid for that
        piece. If the move is valid _complete_move is called.
        :param target_coordinates: string of coordinates
        :param move_to_coordinates: string of coordinates
        :return: True of False
        """

        # check to make sure the game is still active, that is no one has won
        if self._game_state != "UNFINISHED":
            return False

        # make sure the move is targeting a piece on the board using the
        # dictionaries to check if the string is valid or not.
        if target_coordinates[0] not in self._convertAlpha or \
                target_coordinates[1:] not in self._convertNum:
            return False

        # if the move targets the same space the move is considered invalid
        if target_coordinates == move_to_coordinates:
            return False

        # make sure the coordinates being targeted actually contain a piece
        if self._board[self._convertNum[target_coordinates[1:]]][
            self._convertAlpha[target_coordinates[0]]] == " ":
            return False

        # make sure the coordinates being moved to are on the board using the
        # dictionaries to check if the string is valid or not.
        if move_to_coordinates[0] not in self._convertAlpha or \
                move_to_coordinates[1:] not in self._convertNum:
            return False

        # make sure the move_to_coordinates are on the board.
        # get the target pieces object
        current_piece = self._board[self._convertNum[target_coordinates[1:]]][
            self._convertAlpha[target_coordinates[0]]]

        # make sure turn order is being followed
        if current_piece.get_color().upper() != self._player_turn.upper():
            return False

        # we set a place holder for the targeted piece
        targeted_space = self._board[self._convertNum[
            move_to_coordinates[1:]]][self._convertAlpha[
            move_to_coordinates[0]]]

        # see if the move_to space is occupied
        if targeted_space != " ":

            # if the space is occupied we check to make sure it is not a
            # friendly piece in the space
            if current_piece.get_color() == targeted_space.get_color():
                return False

        # call the target pieces movement ability with the new coordinates
        # each piece contains it's own control flow to check if a move is valid
        # if the move is valid the pieces movement returns true and the piece is
        # moved on the list. The names of the pieces determine how they are
        # called. Some get the board passed to them so they can use check space.
        # Others don't need it.
        if current_piece.get_name() in ["Soldier", "Advisor"]:

            # the movement for these three is only passed the
            # move_to_coordinates
            if current_piece.movement(move_to_coordinates) == True:

                # test in check returns whether or not the move clears the
                # check. If it does execution continues, else return false.
                if current_piece.get_color() == "red" and \
                        self._red_check == True:
                    if not self.test_in_check_move(target_coordinates,
                                                   move_to_coordinates,
                                                   current_piece,
                                                   targeted_space):
                        return False

                if current_piece.get_color() == "black" and \
                        self._black_check == True:

                    # test in check returns whether or not the move clears the
                    # check. If it does execution continues, else return false.
                    if not self.test_in_check_move(target_coordinates,
                                                   move_to_coordinates,
                                                   current_piece,
                                                   targeted_space):
                        return False

                # check to see if the space being moved to is empty
                if targeted_space == " ":
                    # if the movement is valid for the piece _move_completion is
                    # called which handles the actual movement of the piece
                    # within the board.
                    self._move_completion(target_coordinates,
                                          move_to_coordinates,
                                          current_piece)

                    # the check finder is called to see if the move resulted in
                    # a check.
                    self.check_finder(current_piece.get_color())

                    return True

                # check to see if the piece being attacked is a not a general
                if targeted_space.get_name() != "General":

                    # move completion is called to move the piece in the list
                    self._move_completion(target_coordinates,
                                          move_to_coordinates,
                                          current_piece)

                    # the check finder is called to see if the move resulted in
                    # a check.
                    self.check_finder(current_piece.get_color())

                    return True

                # if control has made it past the empty check and past the check
                # to see if it is not general we know the targeted piece is a
                # general.
                else:

                    # the game state is changed to reflect which ever color took
                    # a general has won
                    self._game_state = current_piece.get_color().upper() + \
                                       "_WON"

                    # call the final movement method
                    self._move_completion(target_coordinates,
                                          move_to_coordinates,
                                          current_piece)

                    # we don't update the list because someone has won and the
                    # game is complete meaning that check doesn't matter any
                    # more.

                    # the check finder is called to see if the move resulted in
                    # a check.
                    self.check_finder(current_piece.get_color())

                    return True

            # if the move cannot be completed by the piece make_move() returns
            # false.
            else:
                return False
        # same as above, pieces with the names in the list have the board passed
        # to them in order to make specific checks or moves.
        if current_piece.get_name() in ["General", "Chariot", "Cannon",
                                        "Elephant", "Horse"]:

            # if the movement is possible
            if current_piece.movement(self, move_to_coordinates) == True:

                if current_piece.get_color() == "red" and \
                        self._red_check == True:
                    if not self.test_in_check_move(target_coordinates,
                                                   move_to_coordinates,
                                                   current_piece,
                                                   targeted_space):
                        return False

                if current_piece.get_color() == "black" and \
                        self._black_check == True:

                    # test in check returns whether or not the move clears the
                    # check. If it does execution continues, else return false.
                    if not self.test_in_check_move(target_coordinates,
                                                   move_to_coordinates,
                                                   current_piece,
                                                   targeted_space):
                        return False

                # check to see if the space being moved to is empty
                if targeted_space == " ":
                    # if the movement is valid for the piece _move_completion is
                    # called which handles the actual movement of the piece
                    # within the board.
                    self._move_completion(target_coordinates,
                                          move_to_coordinates,
                                          current_piece)

                    # the check finder is called to see if the move resulted in
                    # a check.
                    self.check_finder(current_piece.get_color())

                    return True

                # check to see if the being move to contains a general
                if targeted_space.get_name() != "General":

                    self._move_completion(target_coordinates,
                                          move_to_coordinates,
                                          current_piece)

                    # the check finder is called to see if the move resulted in
                    # a check.
                    self.check_finder(current_piece.get_color())

                    return True

                # if control has made it past the empty check and past the check
                # to see if it is not general we know the targeted piece is a
                # general.
                else:

                    # the game state is changed to reflect which ever color took
                    # a general has won
                    self._game_state = current_piece.get_color().upper() + \
                                       "_WON"

                    # call the final movement method
                    self._move_completion(target_coordinates,
                                          move_to_coordinates,
                                          current_piece)

                    # we don't update the list because someone has won and the
                    # game is complete meaning that check doesn't matter any
                    # more.

                    return True

    def display_character(self, target_coordinates):
        """
        DELETE - ACCESSES DATA MEMBERS IT SHOULDN'T
        Method to display a piece on the board. Used primarily for checking to
        see if a piece was created accurately.
        :param target_coordinates: coordinates of the target piece
        """
        current_piece = self._board[self._convertNum[target_coordinates[1:]]][
            self._convertAlpha[target_coordinates[0]]]

        # if the space is empty it will print a statement letting us know
        if current_piece == " ":
            print("Space is empty.")
        # if the space is not empty it prints some of the pieces data
        else:
            print(current_piece._color, current_piece._name,
                  current_piece._location, current_piece._character)

    def get_game_state(self):
        """
        Method allowing users to check the current state of the game.
        """
        return self._game_state

    def check_space(self, x_coord, y_coord):
        """
        Method which allows the program, to check the contents of a space.
        Coordinates must be converted by convertNum and convertAlpha.
        """

        return self._board[y_coord][x_coord]

    def display_player_turn(self):
        """
        Method used to check who's turn it is.
        """

        print(self._player_turn)

    def _move_completion(self, target_coordinates, move_to_coordinates,
                         current_piece):
        """
        Method to move the piece within the list in memory. This should never be
        called directly by the player as it would bypass validation. It will be
        called by make_move() when necessary. So no touchy.
        """

        targeted_space = self._board[self._convertNum[
            move_to_coordinates[1:]]][self._convertAlpha[
            move_to_coordinates[0]]]

        # since a list of all the piece objects, sorted by their
        # color, is generated at the start of a new game. We have
        # to update that list in order to have check_finder work.
        # So when a piece is taken we remove it from it's respective
        # list.

        if targeted_space != " ":
            if targeted_space.get_color() == 'red':
                self._red_piece_list.remove(targeted_space)

            if targeted_space.get_color() == 'black':
                self._black_piece_list.remove(targeted_space)

        # moves the piece
        self._board[self._convertNum[move_to_coordinates[1:]]][
            self._convertAlpha[move_to_coordinates[0]]] = current_piece

        # the object has been moved in the list and we can change it's old
        # position to an empty space.
        self._board[self._convertNum[target_coordinates[1:]]][
            self._convertAlpha[target_coordinates[0]]] = " "

        # update the pieces current location
        current_piece.location_setter(move_to_coordinates)
        # change who's turn it is
        if current_piece.get_color().lower() == 'red':
            self._player_turn = 'black'

        if current_piece.get_color().lower() == 'black':
            self._player_turn = 'red'

        return True

    def is_in_check(self, color):
        """
        A method used to check whether a color is in check.
        :param color: "red" or "black"
        :return: a True or False value for black or red being in check
        """

        # if the user types in black
        if color.lower() == "black":
            if self._black_check == True:
                return True
            else:
                return False

        # if the user types in red
        if color.lower() == "red":
            if self._red_check == True:
                return True
            else:
                return False

        # if the color was not red or black
        else:
            return "Color must be red or black."

    def show_list(self, color):

        if color.lower() == "black":
            num = 1
            for piece in self._black_piece_list:
                print(num, piece.get_name(), piece.get_color(),
                      piece.get_location())
                num += 1

        if color.lower() == "red":
            num = 1
            for piece in self._red_piece_list:
                print(num, piece.get_name(), piece.get_color(),
                      piece.get_location())
                num += 1

    def check_finder(self, color):
        """
        Method for checking whether a certain color is in check. Since each
        piece stores it's own movement validations and doesn't actually move the
        piece, we can call the pieces movement to see if the general is in
        check.
        :param color: the color of the team you want to know is in check
        :return: True or False
        """

        # if red was the last piece to go we check if black is now in check
        if color == 'red':

            # our list of pieces contains all the piece objects
            for piece in self._red_piece_list:

                # we sort which call is made to their movement based on their
                # name.
                if piece.get_name() in ["Soldier", "Advisor"]:

                    # if a pieces movement returns True we set the check status
                    if piece.movement(self._black_general_location) == True:
                        # we would then set the check status to reflect this.
                        self._black_check = True
                        return True

                # the names in this list get the board object passed to them.
                if piece.get_name() in ["General", "Chariot", "Cannon",
                                        "Elephant", "Horse"]:

                    # if a pieces movement returns True we set the check status
                    if piece.movement(self,
                                      self._black_general_location) == True:
                        self._black_check = True
                        return True

            # if the general is safe nothing happens.
            return False

        # if black was last to go we check if red is now in check
        if color == 'black':
            for piece in self._black_piece_list:

                # we sort which call is made to their movement based on their
                # name.
                if piece.get_name() in ["Soldier", "Advisor"]:

                    # if a pieces movement returns True we set the check status
                    if piece.movement(self._red_general_location) == True:
                        # we would then set the check status to reflect this.
                        self._red_check = True
                        return True

                # the names in this list get the board object passed to them.
                if piece.get_name() in ["General", "Chariot", "Cannon",
                                        "Elephant", "Horse"]:

                    # if a pieces movement returns True we set the check status
                    if piece.movement(self,
                                      self._black_general_location) == True:
                        self._red_check = True
                        return True

            # if the general is safe nothing happens.
            return False

    def general_location(self, color, new_location):
        """
        Setter method to update the generals location data member
        :return: Nothing
        """
        if color == 'red':
            self._red_general_location = new_location

        if color == 'black':
            self._black_general_location = new_location

    def display_general(self):
        print("black", self._black_general_location)
        print("red", self._red_general_location)

    def test_in_check_move(self, target_coordinates, move_to_coordinates,
                           current_piece, targeted_piece):
        # make move in the actual board
        self._move_completion(target_coordinates, move_to_coordinates,
                              current_piece)

        if current_piece.get_color() == 'red':

            # check for check
            if self.check_finder('black') == False:
                # reverse the move
                self._move_completion(move_to_coordinates,
                                      target_coordinates, current_piece)
                self._board[self._convertNum[move_to_coordinates[1:]]][
                    self._convertAlpha[move_to_coordinates[0]]] = targeted_piece

                self._black_piece_list.append(targeted_piece)

                if current_piece.get_color() == "red":
                    self._red_check = False
                if current_piece.get_color() == "black":
                    self._black_check = False
                return True

            else:
                # still reverse the move
                self._move_completion(move_to_coordinates,
                                      target_coordinates, current_piece)
                self._board[self._convertNum[move_to_coordinates[1:]]][
                    self._convertAlpha[move_to_coordinates[0]]] = targeted_piece
                self._black_piece_list.append(targeted_piece)
                return False


class GamePieces:
    """
    A super class for all the other game pieces that gets used to streamline
    initializing different pieces.
    """

    def __init__(self, color, location):
        """
        A method used as a super() to initialize pieces. Every piece has it's
        own convertAlpha, convertNum, color, and location data members.
        :param color:
        :param location:
        """

        self._color = color

        self._location = location

        # convert alpha contains both the lower and upper case because using
        # .upper() on all comparisons would've added more code
        self._convertAlpha = {"A": 0, "a": 0, "B": 1, "b": 1, "C": 2, "c": 2,
                              "D": 3, "d": 3, "E": 4, "e": 4, "F": 5, "f": 5,
                              "G": 6, "g": 6, "H": 7, "h": 7, "I": 8, "i": 8}

        # converts the string number to the correct integer.
        self._convertNum = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5,
                            "7": 6, "8": 7, "9": 8, "10": 9}

    def location_setter(self, new_location):
        self._location = new_location

    def get_color(self):
        """
        Method used to return a pieces color
        :return:
        """
        return self._color

    def get_location(self):
        return self._location


class General(GamePieces):
    """
    This class creates a General object, it inherits from game_pieces and adds
    additional data members specific to the General.
    """

    def __init__(self, color, location):
        self._name = "General"
        self._character = "師"
        super().__init__(color, location)

    def get_name(self):
        return self._name

    def movement(self, board, next_location):
        """
        This is the General's specific movement method. It will check to make
        sure that the input movement is allowed for the General.
        :param board: the current board object
        :param next_location: the spot the General is moving to.
        :return: True or False
        """

        # gets the index numbers for an objects location
        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        if self._color == "red":

            # see if the x axis is changing
            if old_x != new_x:
                if new_x == old_x + 1 or new_x == old_x - 1:
                    # if the x axis is changing we make sure it's only one
                    # space being moved
                    if 3 <= new_x <= 5:
                        # if the move is in the palace the pieces location is
                        # updated and True is returned.
                        self._location = next_location
                        board.general_location("red", next_location)
                        return True
                    else:
                        return False
                else:
                    return False

            # first we check to see if the y axis is changing
            if old_y != new_y:
                # if y axis is changing we make sure it's only one space moved
                if new_y == old_y + 1 or new_y == old_y - 1:
                    # then we make sure the move is in the palace
                    if 7 <= new_y <= 9:
                        # if the move is in the palace the pieces location is
                        # updated and True is returned.
                        board.general_location("red", next_location)
                        return True
                    else:
                        return False

                # the red Generals flying general move
                # if we are targeting the general on the other side.
                if board.check_space(new_x, new_y).get_name() == "General":

                    space = old_y
                    # we iterate through the board on the y_axis to check for
                    # whether the generals can actually see each other. Since we
                    # already know new_y would be the target generals y_coord we
                    # check just up to the general.
                    while space != new_y + 1:
                        space -= 1

                        # if something is in the way we return false.
                        if board.check_space(old_x, space) != " ":
                            return False

                    # if nothing is in the way the move goes through.
                    else:
                        board.general_location("red", next_location)
                        self._location = next_location
                        return True

                else:
                    return False

            else:
                return False

        if self._color == "black":

            # see if the x axis is changing
            if old_x != new_x:
                if new_x == old_x + 1 or new_x == old_x - 1:
                    # if the x axis is changing we make sure it's only one
                    # space being moved
                    if 3 <= new_x <= 5:
                        # if the move is in the palace the pieces location is
                        # updated and True is returned.
                        board.general_location("black", next_location)
                        return True
                    else:
                        return False
                else:
                    return False

            # first we check to see if the y axis is changing
            if old_y != new_y:

                # if y axis is changing we make sure it's only one space moved
                if new_y == old_y + 1 or new_y == old_y - 1:

                    # then we make sure the move is in the palace
                    if 0 <= new_y <= 2:

                        # if the move is in the palace the pieces location is
                        # updated both in the piece and in the board data member
                        # and True is returned.
                        board.general_location("black", next_location)
                        return True
                    else:
                        return False

                # the black Generals flying general move
                # if we are targeting the general on the other side.
                if board.check_space(new_x, new_y).get_name() == "General":

                    space = old_y

                    # we iterate through the board on the y_axis to check for
                    # whether the generals can actually see each other. Since we
                    # already know new_y would be the target generals y_coord we
                    # check just up to the general.
                    while space != new_y - 1:

                        space += 1

                        # if something is in the way we return false.
                        if board.check_space(old_x, space) != " ":
                            return False

                    # if nothing is in the way the move goes through.
                    else:
                        board.general_location("black", next_location)
                        return True

                else:
                    return False

            else:
                return False


class Soldier(GamePieces):

    def __init__(self, color, location):
        self._name = "Soldier"
        self._character = "兵"
        super().__init__(color, location)

    def get_name(self):
        return self._name

    def movement(self, next_location):

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
                    return True

                else:
                    return False
            # if the soldier has crossed the river yet.
            if old_y <= 4:

                if old_y - 1 == new_y and old_x == new_x:
                    return True

                if (old_x - 1 == new_x or old_x + 1 == new_x) and \
                        old_y == new_y:
                    return True
                else:
                    return False

        if self._color == "black":

            # check to see if the red soldier has crossed the river or not.
            if old_y <= 4:

                # we subtract 1 from the old_y axis to make sure the move is
                # only one space and that the piece has moved forward. At this
                # point the soldier can't move left or right which is why there
                # is a check to make sure it maintains it's x value.
                if old_y + 1 == new_y and old_x == new_x:
                    return True

                else:
                    return False
            # if the soldier has crossed the river yet.
            if old_y >= 5:

                if old_y + 1 == new_y and old_x == new_x:
                    return True

                if (old_x - 1 == new_x or old_x + 1 == new_x) and \
                        old_y == new_y:
                    return True
                else:
                    return False


class Chariot(GamePieces):

    def __init__(self, color, location):
        self._name = "Chariot"
        self._character = "車"
        super().__init__(color, location)

    def get_name(self):
        return self._name

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
                            return True
                        if space != new_x:
                            return False
                    else:
                        return False
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
                            return True
                        if space != new_x:
                            return False
                    else:
                        return False
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
                            return True
                        if space != new_y:
                            return False
                    else:
                        return False

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
                            return True
                        if space != new_y:
                            return False
                    else:
                        return False
            return True

        else:
            return False


class Cannon(GamePieces):

    def __init__(self, color, location):
        self._name = "Cannon"
        self._character = "炮"
        super().__init__(color, location)

    def get_name(self):
        return self._name

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
                        return False
                # if all the spaces are empty the false statement never triggers
                # and we return true.
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
                        # the number of pieces in between are tracked by
                        # incrementing the piece_counter
                        if board.check_space(old_x, space) != " ":
                            piece_counter += 1
                    # once the while loop is complete we check if there is only
                    # one piece, if there is only 1 the move goes through
                    if piece_counter == 1:
                        return True
                    # if there is more than one piece to jump we return false.
                    else:
                        return False

                else:
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
                        return False
                # if all the spaces are empty the false statement never triggers
                # and we return true.
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
                        # the number of pieces in between are tracked by
                        # incrementing the piece_counter
                        if board.check_space(old_x, space) != " ":
                            piece_counter += 1
                    # once the while loop is complete we check if there is only
                    # one piece, if there is only 1 the move goes through
                    if piece_counter == 1:
                        return True
                    # if there is more than one piece to jump we return false.
                    else:
                        return False

                else:
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
                        return False
                # if all the spaces are empty the false statement never triggers
                # and we return true.
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
                        # the number of pieces in between are tracked by
                        # incrementing the piece_counter
                        if board.check_space(space, old_x) != " ":
                            piece_counter += 1
                    # once the while loop is complete we check if there is only
                    # one piece, if there is only 1 the move goes through
                    if piece_counter == 1:
                        return True
                    # if there is more than one piece to jump we return false.
                    else:
                        return False

                else:
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
                        return False
                # if all the spaces are empty the false statement never triggers
                # and we return true.
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
                        # the number of pieces in between are tracked by
                        # incrementing the piece_counter
                        if board.check_space(space, old_y) != " ":
                            piece_counter += 1
                    # once the while loop is complete we check if there is only
                    # one piece, if there is only 1 the move goes through
                    if piece_counter == 1:
                        return True
                    # if there is more than one piece to jump we return false.
                    else:
                        return False

                else:
                    return False
        else:
            return False


class Advisor(GamePieces):

    def __init__(self, color, location):
        self._name = "Advisor"
        self._character = "仕"
        super().__init__(color, location)

    def get_name(self):
        return self._name

    def movement(self, next_location):
        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        if self._color == "red":
            # check to make sure the move to space is within the palace
            if 7 <= new_y <= 9 and 3 <= new_x <= 5:
                # if the piece is moving up & right
                if old_x + 1 == new_x and old_y - 1 == new_y:
                    return True

                # if the piece is moving down & right
                if old_x + 1 == new_x and old_y + 1 == new_y:
                    return True
                # if the piece is moving down & left
                if old_x - 1 == new_x and old_y + 1 == new_y:
                    return True
                # if the piece is moving up & left
                if old_x - 1 == new_x and old_y - 1 == new_y:
                    return True
                else:
                    return False
            else:
                return False

        if self._color == "black":
            # check to make sure the move to space is within the palace
            if 0 <= new_y <= 2 and 3 <= new_x <= 5:
                # if the piece is moving up & right
                if old_x + 1 == new_x and old_y - 1 == new_y:
                    return True

                # if the piece is moving down & right
                if old_x + 1 == new_x and old_y + 1 == new_y:
                    return True
                # if the piece is moving down & left
                if old_x - 1 == new_x and old_y + 1 == new_y:
                    return True
                # if the piece is moving up & left
                if old_x - 1 == new_x and old_y - 1 == new_y:
                    return True
                else:
                    return False
            else:
                return False


class Elephant(GamePieces):

    def __init__(self, color, location):
        self._name = "Elephant"
        self._character = "相"
        super().__init__(color, location)

    def get_name(self):
        return self._name

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
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        return True

                # if the piece is moving up & left
                if old_x - 2 == new_x and old_y - 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x - 1, old_y - 1) != " ":
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        return True

                # if the piece is moving down & right
                if old_x + 2 == new_x and old_y + 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x + 1, old_y + 1) != " ":
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        return True

                # if the piece is moving down & left
                if old_x - 2 == new_x and old_y + 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x - 1, old_y + 1) != " ":
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        return True

                # not a valid diagonal move
                else:
                    return False

            # out of bounds
            else:
                return False

        if self._color == "black":

            # check to make sure the move to space is on the red side
            if 0 <= new_y <= 4:

                # if the piece is moving up & right
                if old_x + 2 == new_x and old_y - 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x + 1, old_y - 1) != " ":
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        return True

                # if the piece is moving up & left
                if old_x - 2 == new_x and old_y - 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x - 1, old_y - 1) != " ":
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        return True

                # if the piece is moving down & right
                if old_x + 2 == new_x and old_y + 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x + 1, old_y + 1) != " ":
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        return True

                # if the piece is moving down & left
                if old_x - 2 == new_x and old_y + 2 == new_y:

                    # if the space is occupied the move cannot be completed
                    if board.check_space(old_x - 1, old_y + 1) != " ":
                        return False

                    # if the space being moved into is occupied we track that
                    # a piece was taken
                    if board.check_space(new_x, new_y) != " ":
                        return True

                    # if the space is not occupied it's just a movement
                    else:
                        return True

                # not a valid diagonal move
                else:
                    return False

            # out of bounds
            else:
                return False


class Horse(GamePieces):
    def __init__(self, color, location):
        self._name = "Horse"
        self._character = "馬"
        super().__init__(color, location)

    def get_name(self):
        return self._name

    def movement(self, board, next_location):
        old_x = self._convertAlpha[self._location[0]]
        old_y = self._convertNum[self._location[1:]]
        new_x = self._convertAlpha[next_location[0]]
        new_y = self._convertNum[next_location[1:]]

        # if the piece is moving forward
        if old_y - 2 == new_y:

            # check the space one above the current location
            if board.check_space(old_x, old_y - 1) != " ":
                return False

            # if the piece is moving back two on the y-axis, it can only move
            # 1 left or right on the x_axis
            if old_x - 1 == new_x or old_x + 1 == new_x:

                # check to see if the space is occupied, since friendly fire is
                # handled by make_move() we know that if it isn't empty it must
                # be an opponents piece
                if board.check_space(new_x, new_y) != " ":
                    return True

                # if the space is empty then it's just a simple movement.
                else:
                    return True
            else:
                return False

        # if the piece is moving backwards
        if old_y + 2 == new_y:

            # check the space one above the current location
            if board.check_space(old_x, old_y + 1) != " ":
                return False

            # if the piece is moving back two on the y-axis, it can only move
            # 1 left or right on the x_axis
            if old_x - 1 == new_x or old_x + 1 == new_x:

                # check to see if the space is occupied, since friendly fire is
                # handled by make_move() we know that if it isn't empty it must
                # be an opponents piece
                if board.check_space(new_x, new_y) != " ":
                    return True

                # if the space is empty then it's just a simple movement.
                else:
                    return True
            else:
                return False

        # if the piece is moving right
        if old_x + 2 == new_x:

            # check the space one above the current location
            if board.check_space(old_x + 1, old_y) != " ":
                return False

            # if the piece is moving back two on the y-axis, it can only move
            # 1 left or right on the x_axis
            if old_y - 1 == new_y or old_y + 1 == new_y:

                # check to see if the space is occupied, since friendly fire is
                # handled by make_move() we know that if it isn't empty it must
                # be an opponents piece
                if board.check_space(new_x, new_y) != " ":
                    return True

                # if the space is empty then it's just a simple movement.
                else:
                    return True
            else:
                return False

        if old_x - 2 == new_x:

            # check the space one above the current location
            if board.check_space(old_x - 1, old_y) != " ":
                return False

            # if the piece is moving back two on the y-axis, it can only move
            # 1 left or right on the x_axis
            if old_y - 1 == new_y or old_y + 1 == new_y:

                # check to see if the space is occupied, since friendly fire is
                # handled by make_move() we know that if it isn't empty it must
                # be an opponents piece
                if board.check_space(new_x, new_y) != " ":
                    return True

                # if the space is empty then it's just a simple movement.
                else:
                    return True
            else:
                return False

game = XiangqiGame()
move_result = game.make_move('c1', 'e3')
print(move_result)
game.display_board()
black_in_check = game.is_in_check('black')
print(black_in_check)
print(game.make_move('e7', 'e6'))

state = game.get_game_state()
print(state)

