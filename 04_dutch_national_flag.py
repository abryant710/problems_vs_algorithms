"""
Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

"""


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Time complexity: O(n)
    since we traverse the input array once
    Space complexity: O(n)
    since we create a dictionary to store the counts of each number, which scales linearly with the size of the input array

    Args:
       input_list(list): List to be sorted
    """
    tallies = {0: 0, 1: 0, 2: 0}
    for num in input_list:
        if num == 0:
            tallies[0] += 1
        elif num == 1:
            tallies[1] += 1
        else:
            tallies[2] += 1
    return [0] * tallies[0] + [1] * tallies[1] + [2] * tallies[2]


def test_function(test_case, test_num):
    sorted_array = sort_012(test_case)
    assert sorted_array == sorted(test_case), print("Failed test case {}".format(test_num))
    print("Passed test {}".format(test_num))


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2], "01")
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1], "02")
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2], "03")
