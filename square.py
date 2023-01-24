

class Square:

    def __init__(self, value):
        self.row = None
        self.col = None
        self.box = None
        self.value = value 


    def set_value(self, new_value, new_row, new_col):
        self.value = new_value
        self.row = new_row
        self.col = new_col


    def is_legal(self, value, sudokuboard):
        # Checking the row
        if self.row and self.sudokuboard.rows[self.row].has_value(value) == True:
            return False
    
        # Checking the column
        if self.col and self.sudokuboard.cols[self.col].has_value(value) == True:
            return False
    
        # Checking the box
        if self.box and self.sudokuboard.boxes[self.box].has_value(value) == True:
            return False
    
        # If all checks out: value is legal
        return True



from square import Square

class Element:

    def __init__(self, squares, type):
        self.squares = squares


        for square in self.squares:
            if type == "row":
                square.row = self
            if type == "col":
                square.col = self
            if type == "box": 
                square.box = self

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