# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?
import unittest
from problem_1 import two_numbers_add_up


class Problem1TestCase(unittest.TestCase):
    def test_numbers_add_up(self):
        self.assertEqual(two_numbers_add_up([10, 15, 3, 7], 17), True)
        self.assertEqual(two_numbers_add_up([6, 7, 18, 9, 4], 21), False)
        self.assertEqual(two_numbers_add_up([6, 7, 18, 9, 4], 22), True)
        self.assertEqual(two_numbers_add_up([1, 1, 2, 5, 7, 11, 13], 3), True)


if __name__ == '__main__':
    unittest.main()
