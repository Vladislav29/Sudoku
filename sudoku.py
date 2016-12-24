import puzzle

class Sudoku:

    def __init__(self, puzzle):
        self.puzzle = puzzle;

    def check(self):
        squares = [self.puzzle.getSquare(3 * i, 3 * j) for i in range(3) for j in range(3)]

        for row in range(self.puzzle.getHeight()):
            if (len(self.puzzle.etalon & set(self.puzzle.getValues(self.puzzle.getRow(row)))) != 9):
                return False

        for col in range(self.puzzle.getWidth()):
            if (len(self.puzzle.etalon & set(self.puzzle.getValues(self.puzzle.getCol(col)))) != 9):
                return False

        for square in squares:
            if (len(self.puzzle.etalon & set(self.puzzle.getValues(square))) != 9):
                return False

        return True

    def solve(self):
        coordinates = self.puzzle.getFirstEmptyValue()
        if (not coordinates):
            return True
        for i in range(1,10):
            if (self.puzzle.checkValue(i, coordinates[0], coordinates[1]) == True):
                self.puzzle.setValue(coordinates[0], coordinates[1], i)
                if (self.solve() == True):
                    return True
                self.puzzle.setValue(coordinates[0], coordinates[1], 0)
        return False
