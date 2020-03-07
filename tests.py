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

"""
for testing make_move on the black General
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
board1.display_board()
"""

"""
For testing make_move on the red soldier
board1 = XiangqiGame()
board1.display_board()
board1.make_move("E1", "E2")
print("break")
board1.display_board()
board1.make_move("C7", "C6") # dope
board1.make_move("C6", "C5") # crossing the river
board1.make_move("C5", "D5")
board1.make_move("D5", "D6") # false, backwards
board1.make_move("D5", "D3") # false, more than one space moved.
board1.make_move("D5", "A1") # false, impossible move
board1.make_move("D5", "C5") # true, moved left
board1.make_move("C5", "D5") # true, moved right
board1.make_move("D5", "C4") # false, diagonal move
board1.make_move("D5", "D2") # false, more than one space moved left
board1.make_move("D5", "D10") # false, more than one space moved right
board1.display_board()
"""

"""
For testing make_move on black soldier class
board1 = XiangqiGame()
board1.display_board()
board1.make_move("E1", "E2")
print("break")
board1.display_board()
board1.make_move("A4", "A5") # dope
board1.make_move("A5", "B5") # false, moving right before crossing river
board1.make_move("C4", "B4") # false, moving left before crossing river
board1.make_move("C4", "C3") # false, backwards move
board1.make_move("A5", "A6") # crossing the river
board1.make_move("A6", "B6") # True, moved one to the right
board1.make_move("B6", "B5") # false, backwards
board1.make_move("B6", "B3") # false, more than one space moved.
board1.make_move("B6", "A1") # false, impossible move
board1.make_move("B6", "A6") # true, moved left
board1.make_move("A6", "B6") # true, moved right
board1.make_move("B6", "A7") # false, diagonal move
board1.make_move("B6", "C6") # true, more than one space moved right
board1.make_move("C6", "A6") # false, more than one space moved right
board1.display_board()
"""