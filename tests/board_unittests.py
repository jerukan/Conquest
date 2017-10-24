import sys
import unittest

from util.board_util.board import Board

print(sys.path)

class BoardUnitTest(unittest.TestCase):

    def test_fill(self):
        board = Board()
        board.getUnitMoves([3,3], 3)

if __name__ == '__main__':
    unittest.main()
