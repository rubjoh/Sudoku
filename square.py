

class Square:

    def __init__(self, value):
        self.row = None
        self.col = None
        self.box = None
        self.value = value 


    def set_value(self, new_value):
        self.value = new_value
 

    def is_legal(self, value, rows, cols, boxes):
        """
        Method that checks if a given value of a square is in the
        same row, column or box.
        Args: Value: The value you want to check 
              rows: list of all the rows on the board
              cols: list of all the columns on the board
              boxes: list of all the boxes on the board
        Output: True if value is legal and false if it's not
        """
        # Checking the row
        if self.row and rows[self.row].has_value(value) == True:
            return False
    
        # Checking the column
        if self.col and cols[self.col].has_value(value) == True:
            return False
    
        # Checking the box
        if self.box and boxes[self.box].has_value(value) == True:
            return False
    
        # If all checks out: value is legal
        return True


