
class Square:

    def __init__(self, value):
        self.row = None
        self.col = None
        self.box = None
        self.value = value 


    def set_value(self, new_value):
        self.value = new_value


    def is_legal(self, value):
        # Checking the row
        if self.row and self.row.has_value(value) == True:
            return False

        # Checking the column
        if self.col and self.col.has_value(value) == True:
            return False

        # Checking the box
        if self.box and self.box.has_value(value) == True:
            return False

        # If all checks out: value is legal
        return True

    def __str__(self):
        return str(self.value)



