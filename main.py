# -*- coding: utf-8 -*-
import sudoku
import puzzle
import reader
import sys

if len(sys.argv) == 3:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    reader = reader.PuzzleReader()
    s = sudoku.Sudoku(
    reader.getPuzzle(input_file)

    )

    s.solve()
    f = open(output_file, 'w')
    f.write(s.puzzle.toString())
    print(s.puzzle.toString())
else:
    print("Неверное количество аргументов командной строки.")
