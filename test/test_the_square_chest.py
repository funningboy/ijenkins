import unittest
import nose
import gc
from the_square_chest import *

class TestCheckIO(unittest.TestCase):

    def setUp(self):
        pass

    def teardown(self):
        pass

    def test_one_small_square(self):
        """ test one small square """
        expect = 1
        result = checkio([[1,2], [1,5], [2,6], [5,6]])
        self.assertTrue(expect == result)

    def test_its_not_square(self):
        """ test it's not square """

        expect = 0
        result = checkio([[1,2], [1,5], [2,6], [5,9], [6,10], [9,10]])
        self.assertTrue(expect == result)

if __name__ == '__main__':
    # call back by pydb debug when the exception happened
    nose.runmodule(argv=[__file__,'-vvs','-x','--pdb','--pdb-failure'], exit=False)
