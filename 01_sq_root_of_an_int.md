# Analysis of the square root of an integer solution

## The problem

Find a solution to the problem of finding the square root of an integer in O(log n) time.

## The solution

The solution is to use binary search. The idea is to find the integer `x` such that `x * x <= n` and `(x + 1) * (x + 1) > n`. The algorithm is:

1. Set `start = 0` and `end = n`.
2. While `start <= end`:
   1. Set `mid = (start + end) // 2`.
   2. If `mid * mid == n` then return `mid`.
   3. If `mid * mid < n`, set `start = mid + 1`.
   4. If `mid * mid > n`, set `end = mid - 1`.

The time complexity is O(log n) because the number of iterations is `log n` and each iteration takes constant time.
