from board import Board
from sudoku_reader import Sudoku_reader
from square import Square
from element import Element
import numpy as np
import time

start = time.time()

class SudokuBoard(Board):

    def __init__(self, nums):
        super().__init__(nums)

        #Storing the rows, colums and boxes:
        self.rows = []
        self.cols = []
        self.boxes = []

        #Initialize the board and set up the elements
        self.board = self._set_up_nums()
        self._set_up_elems()

        

    
    def _set_up_nums(self):
        #Set up the board using square objects 
        return np.asarray([[Square(value) for value in row] for row in self.nums])
       


    def _box(self):
        #Generator method that returns one box at a time
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = [self.board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                yield box


    def _set_up_elems(self):
        #Set up the elements of the board
        #Storing these elements in self.rows, self.cols and self.boxes

        #Set up rows
        for id, row in enumerate(self.board):
            self.rows.append(Element(row, "row", id))

        #Set up columns
        for id, col in enumerate(np.transpose(self.board)):
            self.cols.append(Element(col, "col", id))

        #Set up boxes
        for id, box in enumerate(self._box()):
            self.boxes.append(Element(box, "box", id))



    def find_empty(self, board):
        #Finds the empty squares on the board
        #Returns the coordinates or None if all values != 0
        for row in range(9):
            for col in range(9):
                if board[row][col].value == 0:
                    return (row, col)
        return None


    def solve(self):
        #Find the empty squares
        empty = self.find_empty(self.board)
        #If no empty squares, then the sudoku is solved
        if not empty:
            return True
        #Using the coordinates for the empty square to test value and set value
        row, col = empty
        for number in range(1, 10):
            if self.board[row][col].is_legal(number, self.rows, self.cols, self.boxes):
                self.board[row][col].set_value(number)
                #Update the elements when the new value has been set
                self._set_up_elems()
                #Recursion
                if self.solve():
                    return True
                else:
                    #Backtracking
                    self.board[row][col].set_value(0)
        return False


    def print_board(self, spaceing):
        #Method for printing the solved board 
        print()
        for row in range(9):
            if row != 0 and row % 3 == 0:
                if spaceing == "":
                    print("- - - - - - - - - - -")
                if spaceing == " ":
                    print("- - - - - - - - - - - - - - -") 
                if spaceing == "  ":
                    print("- - - - - - - - - - - - - - - - - - -")
            for col in range(9):
                if col != 0 and col % 3 == 0:
                    print("|", end=" ")

                if col == 8:
                    print(self.board[row][col].value)
                else:
                    print(str(self.board[row][col].value)+ spaceing, end=" ")
        print()


def solve_boards(filename, num_of_boards):
    reader = Sudoku_reader(filename)
    for i in range(num_of_boards):
        print(f"Solution for board: {i + 1}")
        board = SudokuBoard(reader.next_board())
        board.solve()
        board.print_board(spaceing=" ")
    end = time.time()
    print(f"Execution Time:%.2fs"%(end-start))

if __name__ == "__main__":
    solve_boards("sudoku_10.csv", 10)









