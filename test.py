from counter import *
import unittest


class TestIncrement(unittest.TestCase):

    def test_increment(self):
        bits = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(255):
            idec = int(bits2bin(bits), 2)
            self.assertEqual(i, idec)
            increment(bits)
    
    def test_decrement(self):
        bits = [1, 1, 1, 1, 1, 1, 1, 1]
        for i in range(255, 0, -1):
            idec = int(bits2bin(bits), 2)
            self.assertEqual(i, idec)
            decrement(bits)

if __name__ == '__main__':
    unittest.main()