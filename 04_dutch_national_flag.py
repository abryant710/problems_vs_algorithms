"""
Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

"""


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # initialize pointers for next positions of 0 and 2
    low = 0
    mid = 0
    high = len(input_list) - 1

    while mid <= high:
        if input_list[mid] == 0:
            input_list[mid] = input_list[low]
            input_list[low] = 0
            low += 1
            mid += 1
        elif input_list[mid] == 2:
            input_list[mid] = input_list[high]
            input_list[high] = 2
            high -= 1
        else:
            mid += 1

    return input_list


def test_function(test_case, test_num):
    sorted_array = sort_012(test_case)
    assert sorted_array == sorted(test_case), print("Failed test case {}".format(test_num))


if __name__ == "__main__":
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2], "01")
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1], "02")
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2], "03")
    # Edge cases, empty list and longer list
    test_function([], "04")
    long_arr = [2] * 1000000 + [0] * 1000000 + [1] * 1000000
    test_function(long_arr, "05")
    print("All tests passed for sort_012()")
