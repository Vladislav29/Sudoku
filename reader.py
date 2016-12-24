import puzzle

class PuzzleReader:

    def getPuzzle(self, fileName):
        puzzleFile = open(fileName)
        puzzleRows = puzzleFile.read().split('\n')
        puz = []
        for row in puzzleRows:
            template = []
            puzzleRow = row.split(' ')
            if (len(puzzleRow) != 9):
                break
            for cell in puzzleRow:
                template.append(int(cell))
            puz.append(template)
        return puzzle.Puzzle(puz)
