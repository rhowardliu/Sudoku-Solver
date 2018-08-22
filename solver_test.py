import unittest
from solver import sudoku_solve
from reverse_solver import sudoku_solve_reverse
class SudokuTest(unittest.TestCase):
    puzzle_unsolved = [[0,0,0,0,4,0,0,0,6],
                       [6,2,3,5,0,0,8,0,4],
                       [8,0,0,2,0,0,0,0,0],
                       [0,0,0,8,0,0,0,0,0],
                       [3,0,1,0,5,0,0,0,0],
                       [0,5,0,3,0,7,0,0,0],
                       [4,0,0,7,0,3,6,0,8],
                       [0,0,0,0,0,0,0,0,0],
                       [5,0,8,0,2,0,3,0,7]]

    puzzle_solved = sudoku_solve(puzzle_unsolved)


    def test_horizontal(self):
        '''Testing if sudoku solution has horizontal clashes'''
        for i in range(9):
            for j in range(9):
                for k in range(j+1,9):
                    self.assertNotEqual(self.puzzle_solved[i][j],self.puzzle_solved[i][k])

    def test_vertical (self):
        '''Testing if sudoku solution has vertical clashes'''
        for j in range(9):
            for i in range(9):
                for k in range(i+1,9):
                    self.assertNotEqual(self.puzzle_solved[i][j],self.puzzle_solved[k][j])

    def test_box(self):
        for box in range (9):
            temp = set()
            for i in range (int (box/3) * 3, int (box/3) * 3 + 2):
                for j in range (box % 3 * 3, box % 3 *3 + 2):
                    self.assertNotIn(self.puzzle_solved[i][j], temp)
                    temp.add( self.puzzle_solved[i][j])


if __name__ == '__main__':
    unittest.main()