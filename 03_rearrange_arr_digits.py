"""
Rearrange Array Elements

Rearrange Array Elements so as to form two numbers such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

"""


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Handle edge cases
    if len(input_list) == 0:
        return []
    if len(input_list) == 1:
        return input_list
    if len(input_list) == 2:
        return [input_list[0], input_list[1]]

    sorted_list = merge_sort(input_list)
    num1 = []
    num2 = []
    for i in range(len(sorted_list)):
        if i % 2 == 0:
            num1.insert(0, sorted_list[i])
        else:
            num2.insert(0, sorted_list[i])

    return [int("".join(map(str, num1))), int("".join(map(str, num2)))]


def test_function(test_case, test_num):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    assert sum(output) == sum(solution), print("Test {}: Failed".format(test_num))


if __name__ == "__main__":
    test_function([[1, 2, 3, 4, 5], [542, 31]], "01")
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]], "02")
    test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [97531, 86420]], "03")
    # Edge cases, empty list and longer list
    test_function([[], []], "04")
    test_function(
        [
            [i for i in range(100)],
            [
                98969492908886848280787674727068666462605856545250484644424038363432302826242220181614121086420,
                99979593918987858381797775737169676563615957555351494745434139373533312927252321191715131197531,
            ],
        ],
        "05",
    )
    print("All tests passed for rearrange_digits()")
