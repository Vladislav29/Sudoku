# -*- coding: utf-8 -*-
import sudoku
import puzzle
import reader
import sys

reader = reader.PuzzleReader()

f = input()
s = sudoku.Sudoku(
reader.getPuzzle('f')

)

s.solve()
f = open('output', 'w')
f.write(s.puzzle.toString())
print(s.puzzle.toString())

#
