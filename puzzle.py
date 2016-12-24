import sys

class Puzzle:

    def __init__(self, puzzle):
        self.puzzle = puzzle

    def getWidth(self):
        return len(self.puzzle[0])

    def getHeight(self):
        return len(self.puzzle)

    def getRow(self, rowIndex):
        return self.puzzle[rowIndex]

    def getCol(self, colIndex):
        return [self.puzzle[i][colIndex] for i in range(len(self.puzzle))]

    def getSquare(self, rowIndex, colIndex):
        x = (colIndex // 3) * 3
        y = (rowIndex // 3) * 3
        rows = self.puzzle[y:y+3]
        cols = [rows[i][x:x+3] for i in range(len(rows))]
        return sum(cols, [])

    def setValue(self, row, col, value):
        self.puzzle[row][col] = value

    def hasNotValue(self, li, setValue):
        return set(li) & setValue == set([])

    def checkValue(self, value, row, col):
        val = set([value])
        return (self.hasNotValue(self.getRow(row), val) and
                self.hasNotValue(self.getCol(col), val) and
                self.hasNotValue(self.getSquare(row, col), val))

    def getFirstEmptyValue(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if (self.puzzle[i][j] == 0):
                    return [i, j]
        return False

    def toString(self):
        stringRepresentation = ''
        for row in self.puzzle:
            for cell in row:
                stringRepresentation += str(cell) + ' '
            stringRepresentation += '\n'
        return stringRepresentation
