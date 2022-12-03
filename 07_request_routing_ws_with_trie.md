# Analysis of the request routing for a web server with trie problem

## The problem

Implement an HTTPRouter like you would find in a typical web server using the Trie data structure.

## The solution

The solution is to use a trie. The idea is to store the path in the trie. The algorithm is:

1. Create a trie.
2. For each path in the list of paths:
   1. Split the path into a list of strings.
   2. Insert the list of strings into the trie using nodes.
3. For each path in the list of paths:
   1. Split the path into a list of strings.
   2. Search the trie for the list of strings.
   3. If the list of strings is found, return the path.
   4. If the list of strings is not found, return a "Not found" handler.

The time complexity is O(n), where n is the path after it has been split. The space complexity is O(n) because the storage of the paths in the trie is O(n).
