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

Algorithm complexity breakdown:

`p` is the length of the path after splitting it into a list of strings.

RouteTrie class:

The time complexity of inserting a path into the trie is O(p).
The time complexity of finding a path in the trie is O(p).

Router class:

Since the add_handler method calls the RouteTrie insert method, the time complexity is O(p).
Since the lookup method calls the RouteTrie find method, the time complexity is O(p).

The time complexity of the overall algorithm is O(p).

The space complexity of the algorithm is O(n), where `n` is the number of paths in the list, due to the self.children dictionary attribute in the RouteTrieNode class.
