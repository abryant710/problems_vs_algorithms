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

The time complexity of the overall algorithm is O(p), where `p` is the length of the path after splitting it into a list of strings. The space complexity is also O(p).

RouteTrie class:

init method: O(1) time and O(1) space
insert method: O(p) time, since it iterates over each string in the path, and O(p) space since each string is stored in a node
find method: O(p) time, since it iterates over each string in the path, and O(1) space since it simply returns the handler for the path or None

RouteTrieNode class:

init method: O(1) time and O(1) space
insert method: O(1) time, since it simply inserts a node into the children dictionary, and O(1) space

Router class:

init method: O(1) time and O(1) space
add_handler method: O(p) time, as it calls the insert method on the trie, and O(p) space
lookup method: O(p) time, as it calls the find method on the trie, and O(1) space
split_path method: O(n) time where n is the length of the input string, as it uses the split method on the path which iterates over each char. O(p) space since it creates a list of strings based on the "/" delimiter
