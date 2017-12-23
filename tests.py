#! /usr/bin/python3.6
"""
Unit tests for Twig coding challenge.
"""

import unittest
from coding_challenge import split_list

class TestCase(unittest.TestCase):
    """
    Unit tests class for coding challenge function.
    """
    def setUp(self):
        self.equally_divisible_list = [1, 5, 7, 3, 8, 9, 11, 14, 18]
        self.unequally_divisible_list = [1, 5, 7, 3, 8, 9, 11, 14, 18, 23, 30]
        self.empty_list = []
        self.positive_int = 3
        self.negative_int = -1

    def test_equally_divisible_list_and_positive_int(self):
        """
        Test that a list that divides equally and a positive number of lists
        to divide in to returns 3 lists all with 3 elements.
        """
        result = split_list(self.equally_divisible_list, self.positive_int)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result[0]), 3)
        self.assertEqual(len(result[1]), 3)
        self.assertEqual(len(result[2]), 3)

    def test_equally_divisible_list_and_negative_int(self):
        """
        Test that a list that divides equally and a negative number of lists
        to divide in to returns an empty list.
        """
        result = split_list(self.equally_divisible_list, self.negative_int)
        self.assertEqual(len(result), 0)

    def test_equally_divisible_list_and_1(self):
        """
        Test that a list that divides equally and number of lists to divide
        in to set as 1 returns 1 list with the same elements
        as the original list.
        """
        result = split_list(self.equally_divisible_list, 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.equally_divisible_list)

    def test_equally_divisible_list_and_zero(self):
        """
        Test that a list that divides equally and number of lists
        to divide in to set as 0 returns an empty list.
        """
        result = split_list(self.equally_divisible_list, 0)
        self.assertEqual(len(result), 0)

    def test_unequally_divisible_list_and_positive_int(self):
        """
        Test that a list that does not divide equally and a positive number
        of lists to divide in to returns 3 lists: two with 4 elements and
        one with 3 elements.
        """
        result = split_list(self.unequally_divisible_list, self.positive_int)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result[0]), 4)
        self.assertEqual(len(result[1]), 4)
        self.assertEqual(len(result[2]), 3)

    def test_unequally_divisible_list_and_negative_int(self):
        """
        Test that a list that does not divide equally and a negative number
        of lists to divide in to returns an empty list.
        """
        result = split_list(self.unequally_divisible_list, self.negative_int)
        self.assertEqual(len(result), 0)

    def test_unequally_divisible_list_and_1(self):
        """
        Test that a list that does not divide equally and number of lists
        to divide in to set as 1 returns 1 list with the same elements
        as the original list.
        """
        result = split_list(self.unequally_divisible_list, 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.unequally_divisible_list)

    def test_unequally_divisible_list_and_zero(self):
        """
        Test that a list that does not divide equally and number of lists
        to divide in to set as 0 returns an empty list.
        """
        result = split_list(self.unequally_divisible_list, 0)
        self.assertEqual(len(result), 0)

    def test_empty_list_and_positive_int(self):
        """
        Test that an empty list and a positive number of lists to divide in to
        returns an empty list.
        """
        result = split_list(self.empty_list, self.positive_int)
        self.assertEqual(len(result), 0)

    def test_empty_list_and_negative_int(self):
        """
        Test that an empty list and a negative number of lists to divide in to
        returns an empty list.
        """
        result = split_list(self.empty_list, self.negative_int)
        self.assertEqual(len(result), 0)

    def test_example(self):
        """
        Test that the example returns 3 lists: two with 2 elements and one
        with one element.
        """
        result = split_list([1, 2, 3, 4, 5], 3)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result[0]), 2)
        self.assertEqual(len(result[1]), 2)
        self.assertEqual(len(result[2]), 1)

if __name__ == "__main__":
    unittest.main()
