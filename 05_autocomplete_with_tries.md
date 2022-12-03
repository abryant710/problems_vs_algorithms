# Analysis of the autocomplete with tries problem

## The problem

Given a list of words and a prefix, return all words that start with the prefix. The solution should run in O(p + n) time, where `p` is the length of the prefix and `n` is the number of words in the list.

## The solution

The solution is to use a trie. The idea is to store the words in a trie and then search for the prefix in the trie. The algorithm is:

1. Create a trie from the list of words.
2. Search for the prefix in the trie.
3. If the prefix is not found, return an empty list.
4. If the prefix is found, return all words in the trie that start with the prefix.

## Algorithm complexity breakdown

### Definition of terms

`w` is the length of the word inserted into the dictionary of children
`n` is the number of words in the dictionary of children
`p` is the length of the prefix when searching for a word

### Summary

For a trie, the time complexity depends on `w` and `n`. The time complexity for creating the trie is `O(n * w)`. The time complexity for searching for the prefix is `O(p)`. The overall space complexity is `O(n * w)`.

### Trie Class

init method: O(1) time and O(1) space
insert method: O(w) time, since the word is inserted, and O(w) space
find method: O(p) time, which is the length of the prefix, and O(1) space

### TrieNode Class

init method: O(1) time and O(1) space
insert method: O(w) time, since there is an iteration over each char in the word, and O(w) space
suffixes method: O(n) time, since all words in the trie are iterated, and O(n) space
