# Analysis of the rearrange array digits problem

## The problem

Rearrange Array Elements so as to form two numbers such that their sum is maximum. Return these two numbers.

## The solution

The solution is to use merge sort to help sort the array. The idea is to split the array into two halves, sort each half, and then merge the two halves. The algorithm is:

1. Handle the base case: if the array has 0 or 1 elements, return the array.
2. Use merge sort to sort the array:
   1. Split the array into two halves.
   2. Sort each half.
   3. Merge the two halves.
3. Iterate through the array and add the elements to two numbers:
   1. If the index is even, add the element to the first list.
   2. If the index is odd, add the element to the second list.
4. Return the two numbers as a list of 2.

The time complexity is O(n log n) because the number of iterations is `log n` and each iteration takes O(n) time. The space complexity is O(n) because the algorithm uses O(n) space.
