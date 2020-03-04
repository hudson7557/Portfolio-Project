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



general = general("black", "D9")
general.display_character()
general.movement("E9")
