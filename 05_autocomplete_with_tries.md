# Analysis of the autocomplete with tries problem

## The problem

Given a list of words and a prefix, return all words that start with the prefix. The solution should run in O(p + n) time, where `p` is the length of the prefix and `n` is the number of words in the list.

## The solution

The solution is to use a trie. The idea is to store the words in a trie and then search for the prefix in the trie. The algorithm is:

1. Create a trie from the list of words.
2. Search for the prefix in the trie.
3. If the prefix is not found, return an empty list.
4. If the prefix is found, return all words in the trie that start with the prefix.

The time complexity is O(p + n) because the time to create the trie is O(n) and the time to search for the prefix is O(p).
