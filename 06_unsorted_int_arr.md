# Analysis of the unsorted integer array problem

## The problem

Given an unsorted integer array, look for smallest and largest integer from a list of unsorted integers.

## The solution

The solution is to use a linear scan. The idea is to keep track of the smallest and largest integers seen so far. The algorithm is:

1. Set `smallest` and `largest`.
2. For each integer `x` in the array:
   1. If `x < smallest`, set `smallest = x`.
   2. If `x > largest`, set `largest = x`.

The time complexity is O(n) because the algorithm iterates over the array once. The space complexity is O(1) because the algorithm only uses a constant amount of space.
