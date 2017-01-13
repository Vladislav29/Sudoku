import unittest
import subprocess

class SudokuTestCase(unittest.TestCase):
    def test_main(self):
        subprocess.call(['python', 'main.py', 'puzzleOne.txt', 'output.txt'])
        with open('output.txt', 'r') as f:
            output = f.read()
        with open('expected_output.txt', 'r') as f:
            expected_output = f.read()
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
