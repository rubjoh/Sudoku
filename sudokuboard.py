from board import Board
from sudoku_reader import Sudoku_reader
from square import Square
from element import Element
import numpy as np

class SudokuBoard(Board):

    def __init__(self, nums):
        super().__init__(nums)

        #Initialize the board and set up ref
        self.board = self._set_up_nums()
        self._set_up_elems()

        #Storing the rows, colums and boxes:
        self.rows = []
        self.cols = []
        self.boxes = []
        

    
    def _set_up_nums(self):
        #Set up the board using square objects 
        board = np.asarray([[Square(value) for value in row] for row in self.nums])
        return board

    def _set_up_elems(self):
        #Set up links between squares and elements
        #board = self._set_up_nums()

        #Rows:
        for row in range(9):
            row_elements = Element(self.board[row], type="row")
            self.rows.append(row_elements)
        
        #Column:
        for col in range(9):
            col_elements = Element(self.board[:,col], type="col")
            self.cols.append(col_elements)

        #Box:
        for i in range(3):
            for j in range(3):
                for row in range(i*3, i*3+3):
                    for col in range(j*3, j*3+3):
                        box_squares = [self.board[i][j] for i in range(row-row//3, row-row//3+3) for j in range(col-col//3, col-col//3+3)]
                        box_elements = Element(box_squares, type="box")
                        self.boxes.append(box_elements)
        
            


    def find_empty(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col].value == 0:
                    return (row, col)
        return None


    def solve(self):

        empty = self.find_empty(self.board)
        if not empty:
            for row in range(9):
                for col in range(9):
                    print(self.board[row][col].value)
            #print(self.board)
            self._set_up_elems()
            return True

        row, col = empty
        for number in range(1, 10):
            if self.board[row][col].is_legal(number, self.board):
                self.board[row][col].set_value(number, row, col)
                self._set_up_elems()
                if self.solve():
                    return True
                else:
                    self.board[row][col].set_value(0, row, col)
        return False



if __name__ == "__main__":
    reader = Sudoku_reader("sudoku_10.csv")
    b = SudokuBoard(reader.next_board())
    solved_board = b.solve()
    print(solved_board)

 








