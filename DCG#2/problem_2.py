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
def list_product(number_list: list) -> int or float:
    result = 1
    for number in number_list:
        result *= number
    return result


def product_array_division(input_list: list) -> list:
    total = list_product(input_list)
    output_list = []
    for item in input_list:
        output_list.append(total / item)
    return output_list


def product_array_pop(input_list: list) -> list:
    output_list = []
    for idx, item in enumerate(input_list):
        temp_list = input_list.copy()
        temp_list.pop(idx)
        output_list.append(list_product(temp_list))
    return output_list
