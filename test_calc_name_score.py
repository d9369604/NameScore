import unittest
from calc_name_score import calc_name_score


class TestNameScore(unittest.TestCase):

    def test_empty_file_name_score(self):
        self.assertEqual(0, calc_name_score('empty.txt'))

    def test_one_character_name_score(self):
        self.assertEqual(1, calc_name_score('one_character.txt'))

    def test_name_score(self):
        self.assertEqual(150, calc_name_score('contexts.txt'))

    def test_no_such_file(self):
        self.assertRaises(IOError, calc_name_score, 'no_such_file.txt')

    def test_wrong_format_with_number(self):
        self.assertRaises(Exception, calc_name_score, 'wrong_format_with_number.txt')

    def test_wrong_format_with_lower_case(self):
        self.assertRaises(Exception, calc_name_score, 'wrong_format_with_lower_case.txt')

    def test_wrong_format_with_new_line(self):
        self.assertRaises(Exception, calc_name_score, 'wrong_format_with_new_line.txt')

    def test_duplicated_string(self):
        self.assertRaises(Exception, calc_name_score, 'duplicated_string.txt')

if __name__ == '__main__':
    unittest.main()
