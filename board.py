



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


list_1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

list_2 = [num for sublist in list_1 for num in sublist if num % 2 == 0]

print(list_2)

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



