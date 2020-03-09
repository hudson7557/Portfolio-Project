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

"""# For testing make_move on the red soldier
board1 = XiangqiGame()
board1.display_board()
print("break")
board1.display_board()
board1.make_move("C7", "C6") # dope
board1.make_move("C6", "C7") # false backwards
board1.make_move("C6", "B5") # false diagonal
board1.make_move("C6", "B6") # false, sideways
board1.make_move("C6", "D6") # false, sideways
board1.make_move("C6", "C5") # crossing the river
board1.make_move("C5", "D5") # true, moved right
board1.make_move("D5", "D6") # false, backwards
board1.make_move("D5", "D3") # false, more than one space moved.
board1.make_move("D5", "A1") # false, impossible move
board1.make_move("D5", "C5") # true, moved left
board1.make_move("C5", "D5") # true, moved right
board1.make_move("D5", "C4") # false, diagonal move
board1.make_move("D5", "D2") # false, more than one space moved left
board1.make_move("D5", "D10") # false, more than one space moved right
board1.display_board()"""

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

"""
# For testing make_move not allowing people to take their own pieces 
board1 = XiangqiGame()
board1.display_board()
print("break")
board1.display_board()
board1.make_move("C7", "C6") # dope
board1.make_move("C6", "C5") # crossing the river
board1.make_move("C5", "D5") # true, moved right
board1.make_move("E7", "E6") # true, move forward
board1.make_move("E6", "E5") # crossing the river
board1.make_move("E5", "D5") # false, same team
board1.display_board()"""

"""
# For testing make_move taking a piece
board1 = XiangqiGame()
board1.display_board()
print("break")
board1.display_board()
board1.make_move("C7", "C6") # dope
board1.make_move("C6", "C5") # crossing the river
board1.make_move("C5", "D5") # true, moved right
board1.make_move("E7", "E6") # true, move forward
board1.make_move("E6", "E5") # crossing the river
board1.make_move("E5", "D5") # false, same team
board1.make_move("D5", "E5") # false, same team
board1.make_move("D5", "C5") # true, left movement
board1.make_move("C4", "C5") # true, forward, takes piece
board1.display_character("C5")
board1.display_board()"""

"""# For testing make_move on Chariots
board1 = XiangqiGame()
board1.display_board()
board1.make_move("I10", "H10")
board1.make_move("H10", "I10")  # testing moving left and right.
board1.make_move("I10", "F10")
board1.make_move("F10", "G10")
board1.make_move("G10", "G8")
board1.make_move("G8", "G10")
board1.make_move("G10", "G8")
board1.make_move("G8", "F8")
board1.make_move("F8", "F1")
board1.make_move("F1", 'E1')
board1.make_move("E1", "I1")
board1.make_move("I1", "A1")
board1.make_move("A1", "A3")
board1.make_move("A3", "B2")
board1.display_board()"""

"""
# For testing make_move on the cannons 
board1 = XiangqiGame()
board1.display_board()
board1.make_move("B8", "B6") # true, forwards
board1.make_move("B6", "B7") # true, backwards
board1.make_move("B7", "B8") # true, backwards
board1.make_move("B8", "D8") # true, right move
board1.make_move("D8", "E8") # true, right move
board1.make_move("E8", "E7") # false, moving into it's own piece
board1.make_move("E8", "E6") # false, jumping a piece on a non-cap move
board1.make_move("E8", "E4") # true, capturing a piece
board1.make_move("E4", "E5") # True
board1.make_move("E5", "A5") # True
board1.make_move("A5", "A1") # true, capturing the enemy
board1.make_move("A1", "A8") # false, jumping two
board1.display_board()
"""

"""board1 = XiangqiGame()
# for testing the red Advisors
board1.make_move("D10", "E9") # moving up the board and to the right
board1.make_move("E9", "F8")
board1.make_move("F8", "E9") # moving down the board and to the left
board1.make_move("E9", "D10")
board1.make_move("F10", "E9") # moving up the board and to the left
board1.make_move("E9", "D8")
board1.make_move("D8", "C9") # false, out of the palace
board1.make_move("D8", "D7") # false, not a diagonal move also OB
board1.make_move("D8", "E8") # false, not a diagonal move
board1.make_move("D8", "D9") # false, not a diagonal move
board1.make_move("D8", "F10") # false, moving two spaces
board1.make_move("D10", "E9")
board1.make_move("E9", "D8")
board1.make_move("E10", "E9")
# for testing black advisors 
board1.make_move("D1", "E2") # true, moving forward and to the right
board1.make_move("E2", "F3") # true, moving forward and to the right
board1.make_move("G4", "G5") # moving the soldier out of the way
board1.make_move("F3", "G4") # false, ob
board1.make_move("F3", "E2") # true, moving backwards and to the left
board1.make_move("E2", "D1") # true, moving backwards and to the left
board1.make_move("F1", "E2") # true, moving forwards and to the right
board1.make_move("E2", "D3") # true, moving forwards and to the left
board1.make_move("D3", "D4") # false, not diagonal
board1.make_move("D3", "E2") # true, moving backwards and to the right
board1.make_move("E2", "F1")  # true, moving backwards and to the right
board1.make_move("F1", "G2") # false, ob
board1.make_move("D1", "C2") # false, ob
"""

"""#for testing elephants 
board1 = XiangqiGame()
board1.display_board()
# For testing red elephants
board1.make_move("C10", "E8") # true, moved forward right
board1.make_move("E8", "C6") # true, moved forward left
board1.make_move("G10", "I12") # false, ob
board1.make_move("G10", "E8") # true, moved forward left
board1.make_move("E8", "G6") # true, moved forward right
board1.make_move("G6", "C4") # false, crossing the river
board1.make_move("G6", "I8") # true, moved back right
board1.make_move("C6", "A8") # true, move back left
board1.make_move("A8", "C10") # true, moved back right
board1.make_move("I8", "G10") # true, moved back left
# For testing black elephants
print("BREAK TO BLACK PIECE TESTING")
board1.make_move("C1", "E3") # true, moved backwards right
board1.make_move("E3", "G5") # true, moved forward right
board1.display_character("G5")
board1.make_move("G5", "I7") # false, OB
board1.make_move("G5", "I3") # true, moved forwards right
board1.make_move("I3", "I2") # false, horizontal move
board1.make_move("I3", "H2") # false, one space diagonal move
board1.make_move("G1", "E3") # true, moved backward left
board1.make_move("I3", "G1") # true, moved forward, left
board1.make_move("E3", "C1") # true, moved forward, left
board1.display_board()"""

"""#for testing horsies
board1 = XiangqiGame()
board1.display_board()
board1.make_move("B10", "C8") # true, moved forward right
board1.make_move("C8", "B10") # true, moved backwards left
board1.make_move("B10", "A8") # true, moved forward left
board1.make_move("A8", "B10") # true, moved backwards right
board1.make_move("B10", "A8") # true, moved forwards left
board1.make_move("A8", "B6") # false, soldier in the way
board1.make_move("A8", "C8") # false, cannon in the way
board1.make_move("H10", "F9") # false, elephant in the way
board1.make_move("H10", "G8") # true, moved forward left
board1.make_move("G8", "E9") # true, moved left and back
board1.display_character("E9")
board1.make_move("E9", "G8") # true, moved right and back
board1.make_move("A8", "B10") # true, moved back and right
board1.make_move("B10", "D9") # false, runs into elephant
board1.make_move("B10", "C8") # true, move up right
board1.make_move("C8", "E9") # true, moved right down
board1.make_move("E9", "C8") # true, moved left and up
board1.make_move("C8", "E7") # false, friendly fire
board1.make_move("C8", "E8") # horizontal move
board1.make_move("C8", "B10") # true, reset
board1.make_move("B10", "D8") # false, invalid move
board1.make_move("B10", "B9")
board1.make_move("B1", "C3")
board1.make_move("C3", "B1")
board1.display_board()"""