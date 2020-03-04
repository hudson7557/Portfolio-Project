"""for testing make_move on the red General
board1 = XiangqiGame()
board1.display_board()
board1.make_move("E10", "F10")
board1.make_move("F10", "G10")
board1.make_move("F10", "E10")
board1.make_move("E10", "D10")
board1.make_move("D10", "C10")
board1.make_move("D10", "D9")
board1.make_move("D9", "D8")
board1.make_move("D8", "D7")
board1.make_move("D8", "E8")
board1.make_move("E8", "F8")
board1.make_move("F8", "G8")
board1.make_move("F8", "G7")
print("break")
board1.display_board()"""

"""for testing make_move on the black General
board1 = XiangqiGame()
board1.display_board()
board1.make_move("E1", "E11")
board1.make_move("E1", "F1") # valid
board1.make_move("F1", "G1") # out of palace right bounds
board1.make_move("F1", "E1") # valid
board1.make_move("E1", "D1") # valid
board1.make_move("D1", "C1") # out of palace left bounds
board1.make_move("D1", "D2") # valid
board1.make_move("D2", "D3") # valid
board1.make_move("D3", "D4") # out of palace bounds moving forward
board1.make_move("D3", "E2") # wrong because it's a diagonal move
print("break")
board1.display_board()"""