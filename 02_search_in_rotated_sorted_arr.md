# Analysis of the search in rotated sorted array problem

## The problem

Given a sorted array of integers `nums` that has been rotated an unknown number of times, write a function to search `target` in `nums`. If `target` exists in `nums`, then return its index, otherwise return `-1`.

## The solution

The solution is to use binary search. The idea is to find the index `i` such that `nums[i] <= target <= nums[i + 1]`. The algorithm is:

1. Set `start = 0` and `end = len(nums) - 1`.
2. While `start <= end`:
   1. Set `mid = (start + end) // 2`.
   2. If `nums[mid] == target` then return `mid`.
   3. If `nums[start] <= nums[mid]`:
      1. If `nums[start] <= target < nums[mid]`, set `end = mid - 1`.
      2. Otherwise, set `start = mid + 1`.
   4. If `nums[mid] <= nums[end]`:
      1. If `nums[mid] < target <= nums[end]`, set `start = mid + 1`.
      2. Otherwise, set `end = mid - 1`.
3. Return `-1` if `target` is not found.

The time complexity is O(log n) because the number of iterations is `log n` and each iteration takes constant time. The space complexity is O(1) because the algorithm uses constant space.
