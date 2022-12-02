"""
Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Time complexity: O(log(n))
    since the loop will never run more than log(n) times
    Space complexity: O(1)
    since we are not storing any data

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Take care of edge cases
    if number < 0:
        return None
    if number == 0 or number == 1:
        return number

    test_numbers = range(1, number)
    for test_number in test_numbers:
        # Should always return well before looping through all values
        if test_number * test_number > number:
            return test_number - 1
        elif test_number * test_number == number:
            return test_number


def test():
    assert 3 == sqrt(9), print("Failed test 01")
    print("Passed test 01")
    assert 0 == sqrt(0), print("Failed test 02")
    print("Passed test 02")
    assert 4 == sqrt(16), print("Failed test 03")
    print("Passed test 03")
    assert 1 == sqrt(1), print("Failed test 04")
    print("Passed test 04")
    assert 5 == sqrt(27), print("Failed test 05")
    print("Passed test 05")


if __name__ == "__main__":
    test()
