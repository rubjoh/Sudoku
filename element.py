from square import Square

class Element:

    def __init__(self, squares, type, id):
        self.squares = squares
        self.id = id


        for square in self.squares:
            if type == "row":
                square.row = self.id
            if type == "col":
                square.col = self.id
            if type == "box": 
                square.box = self.id

    def has_value(self, value):
        """
        Method to check if a given number is a part of the element.
        Args: self and the value you want to check
        Output: True if value is in element and false if not. 
        """
            
        for square in self.squares:
            if square.value == value:
                return True

        return False 