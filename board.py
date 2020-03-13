



class XiangqiGame:

      def __init__(self):
            """
            Starts a game of Xiangqi as a list object. The board has a
            coordinate grid with A-I on top and
            1-10 on the left side. Open spaces denoted by a single space " ".
            """

            self._game_state = "UNFINISHED"
            self._board = [
                  ["  ", "A ", "  ", "B ", "  ", "C ", "  ",
                   "D", "  ",
                   " E", "  ", " F", "  ", " G", "  ", " H",
                   "  ", " I"],
                  ["1 ", " ", " - ", " ", " - ", " ", " - ",
                   " ", " - ",
                   " ", " - ", " ", " - ", " ", " - ", " ",
                   " - ", " "],
                  ["  ", "| ", "  ", "| ", "  ", "| ", "  ",
                   "|", " \ ",
                   "|", " / ", "|", "  ", " |", "  ", " |",
                   "  ", " |",
                   "  "],
                  ["2 ", " ", " - ", " ", " - ", " ", " - ",
                   " ", " - ",
                   " ", " - ", " ", " - ", " ", " - ", " ",
                   " - ", " "],
                  ["  ", "| ", "  ", "| ", "  ", "| ", "  ",
                   "|", " / ",
                   "|", " \ ", "|", "  ", " |", "  ", " |",
                   "  ", " |",
                   "  "],
                  ["3 ", " ", " - ", " ", " - ", " ", " - ",
                   " ", " - ",
                   " ", " - ", " ", " - ", " ", " - ", " ",
                   " - ", " "],
                  ["  ", "| ", "  ", "| ", "  ", "|", "   ",
                   "|", "   ",
                   "|", "   ", "|", "  ", " |", "  ", " |",
                   "  ", " |",
                   "  "],
                  ["4 ", " ", " - ", " ", " - ", " ", " - ",
                   " ", " - ",
                   " ", " - ", " ", " - ", " ", " - ", " ",
                   " - ", " "],
                  ["  ", " ", "   ", " ", "   ", " ", "   ",
                   " ", "   ",
                   " ", "   ", " ", "   ", " ", "   ", " ",
                   "   ", " "],
                  ["5 ", "|", "   ", " ", "   ", " ", "   ",
                   " ", "   ",
                   " ", "   ", " ", "   ", " ", "   ", " ",
                   "   ", "|"],
                  ["  ", " ", "   ", " ", "   ", " ", "   ",
                   " ", "   ",
                   " ", "   ", " ", "   ", " ", "   ", " ",
                   "   ", " "],
                  ["6 ", " ", " - ", " ", " - ", " ", " - ",
                   " ", " - ",
                   " ", " - ", " ", " - ", " ", " - ", " ",
                   " - ", " "],
                  ["  ", "| ", "  ", "| ", "  ", "|", "   ",
                   "|", "   ",
                   "|", "   ", "|", "  ", " |", "  ", " |",
                   "  ", " |",
                   "  "],
                  ["7 ", " ", " - ", " ", " - ", " ", " - ",
                   " ", " - ",
                   " ", " - ", " ", " - ", " ", " - ", " ",
                   " - ", " "],
                  ["  ", "| ", "  ", "| ", "  ", "|", "   ",
                   "|", "   ",
                   "|", "   ", "|", "  ", " |", "  ", " |",
                   "  ", " |",
                   "  "],
                  ["8 ", " ", " - ", " ", " - ", " ", " - ",
                   " ", " - ",
                   " ", " - ", " ", " - ", " ", " - ", " ",
                   " - ", " "],
                  ["  ", "| ", "  ", "| ", "  ", "| ", "  ",
                   "|", " \ ",
                   "|", " / ", "|", "  ", " |", "  ", " |",
                   "  ", " |",
                   "  "],
                  ["9 ", " ", " - ", " ", " - ", " ", " - ",
                   " ", " - ",
                   " ", " - ", " ", " - ", " ", " - ", " ",
                   " - ", " "],
                  ["  ", "| ", "  ", "| ", "  ", "| ", "  ",
                   "|", " / ",
                   "|", " \ ", "|", "  ", " |", "  ", " |",
                   "  ", " |",
                   "  "],
                  ["10 ", " ", "- ", " ", " - ", " ", " - ",
                   " ", " - ",
                   " ", " - ", " ", " - ", " ", " - ", " ",
                   " - ", " "]]


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_1.remove(2)
print(list_1)

# def test_in_check_move(target_coordinates, move_to_coordinates,
# current, targeted_piece):
# if color moving is in check:
    # make move
    # move_completion((target_coordinates, move_to_coordinates,
        # current_piece)
    # check for check
    # if self.check_finder(current_piece.get_color()) == True:
        # move_completion(move_to_coordinates, target_coordinates, current_piece)
        # self._board[self._convertNum[move_to_coordinates[1:]]][self._convertAlpha[move_to_coordinates[0]]] = target_piece
        # return False
    # if the check finder does not find a check we remove check and reverse the move
    # else:
        # if current_piece.get_color() == "red":
            # self._red_check = False
        # if current_piece.get_color() == "black":
            # self._black_check = False
        # move_completion(move_to_coordinates, target_coordinates, current_piece)
        # self._board[self._convertNum[move_to_coordinates[1:]]][self._convertAlpha[move_to_coordinates[0]]] = target_piece
        # return True



""" # for cannons, removed the friendly fire check
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
                    return False"""
