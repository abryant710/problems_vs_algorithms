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

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Take care of edge cases
    if number == None:
        return None
    if number < 0:
        return None
    if number == 0 or number == 1:
        return number

    # Binary search
    start = 1
    end = number
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == number:
            return mid
        if mid * mid < number:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans


def test():
    assert 3 == sqrt(9), print("Failed test 01")
    assert 0 == sqrt(0), print("Failed test 02")
    assert 4 == sqrt(16), print("Failed test 03")
    assert 1 == sqrt(1), print("Failed test 04")
    assert 5 == sqrt(27), print("Failed test 05")
    # Edge cases, None and large number
    assert None == sqrt(None), print("Failed test 06")
    assert 5000 == sqrt(25000000), print("Failed test 07")
    print("All tests passed for sqrt()")


if __name__ == "__main__":
    test()
