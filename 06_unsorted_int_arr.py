"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?

"""
import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Time complexity: O(n)
    since we are iterating through the list only once
    Space complexity: O(1)
    since we are not using any additional data structures

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = ints[0]
    max = ints[0]
    for i in ints:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)


def test(test_case):
    l = [i for i in test_case]  # a list containing 0 - 9
    random.shuffle(l)

    return get_min_max(l)


if __name__ == "__main__":
    assert (0, 9) == test([i for i in range(10)]), print("Failed test 01")
    assert (0, 19) == test([i for i in range(20)]), print("Failed test 02")
    assert (0, 29) == test([i for i in range(30)]), print("Failed test 03")
    print("All tests passed")
