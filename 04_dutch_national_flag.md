# Analysis of the dutch national flag problem

## The problem

Given an array of 0s, 1s, and 2s, sort the array in place. The algorithm should run in O(n) time and use constant space.

## The solution

The solution is to use a 3-way partitioning algorithm. The idea is to use 3 pointers: `low`, `mid`, and `high`. The algorithm is:

1. Set `low = 0`, `mid = 0`, and `high = len(arr) - 1`.
2. While `mid <= high`:
   1. If `arr[mid] == 0`, swap `arr[low]` and `arr[mid]`, and increment `low` and `mid`.
   2. If `arr[mid] == 1`, increment `mid`.
   3. If `arr[mid] == 2`, swap `arr[mid]` and `arr[high]`, and decrement `high`.

The time complexity is O(n) because the algorithm iterates through the array once. The space complexity is O(1) because the algorithm uses constant space.
