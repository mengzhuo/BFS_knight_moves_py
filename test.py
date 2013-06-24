import unittest
from knight import knight_move, Point

class TestKnight(unittest.TestCase):
    """Test case for knigth move"""

    def test_point_creation(self):
        self.assertEqual(Point(0, 0).step, 0)

    def test_knight_move(self):
        self.assertEqual(knight_move(8, Point(0,0), Point(7,7)).step, 6) 

    def test_knight_move_path(self):
        """
        0,0 -> 0,1 takes 3 steps
        0,0 -> 1,2 -> 2,0 -> 0,1
        """
        path = [(p.x,p.y) for p in knight_move(3, Point(0,0), Point(0,1)).path]
        self.assertEqual(path,[(1,2), (2,0), (0,1)])

    def test_knight_covert_move(self):
        """
        Knight should be able to move any place on a board which
        great than 6x6
        """
        for x in xrange(6):
            for y in xrange(6):
                self.assertIsNotNone(knight_move(6, Point(x,y), Point(5, 5)))

unittest.main()
