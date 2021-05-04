# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?
def two_numbers_add_up_brute_force(number_list: list, k: int) -> bool:
    for idx, number in enumerate(number_list):
        for item in number_list[idx+1:]:
            if k - item == number:
                return True
    return False


def two_numbers_add_up_set_approach(number_list: list, k: int) -> bool:
    temp_set = set()
    for number in number_list:
        if number in temp_set:
            return True
        temp_set.add(k-number)
    return False
