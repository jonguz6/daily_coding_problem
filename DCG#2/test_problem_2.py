# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?
import unittest
from problem_2 import product_array


class MyTestCase(unittest.TestCase):
    def test_list_product(self):
        self.assertEqual(list_product([1, 2, 3]), 6)
        self.assertEqual(list_product([10, 20, 3]), 600)
        self.assertEqual(list_product([5, 5, 5, 5, 5]), 3125)
        self.assertEqual(list_product([1, 1, 1, 1, 1]), 1)
        self.assertEqual(list_product([5, 2.5, 7.3]), 91.25)

    def test_product_array(self):
        self.assertEqual(product_array([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(product_array([3, 2, 1]), [2, 3, 6])


if __name__ == '__main__':
    unittest.main()
