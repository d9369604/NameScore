import unittest
from calc_name_score import calc_name_score


class TestNameScore(unittest.TestCase):

    def test_no_name(self):
        self.assertEqual(0, calc_name_score(['']))

    def test_one_name(self):
        self.assertEqual(6, calc_name_score(['ABC']))

    def test_normal_case(self):
        self.assertEqual(150, calc_name_score(['CDEF', 'ABC', 'FIJK']))

    def test_one_large_name(self):
        self.assertEqual(351, calc_name_score(['ABCDEFGHIJKLMNOPQRSTUVWXYZ']))

    def test_many_large_names(self):
        self.assertEqual(19305, calc_name_score(['ABCDEFGHIJKLMNOPQRSTUVWXYZ'] * 10))

    def test_many_names(self):
        self.assertEqual(21320, calc_name_score(['Z'] * 40))

if __name__ == '__main__':
    unittest.main()
