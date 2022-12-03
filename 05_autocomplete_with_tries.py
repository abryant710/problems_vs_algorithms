"""
Building a Trie in Python

Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

- A Trie class that contains the root node (empty string)
- A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

Finding Suffixes

Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature. To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

Using the code you wrote for the TrieNode above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)


"""

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False

    def insert(self, word):
        ## Add a child node in this Trie
        current_node = self
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def suffixes(self, suffix=""):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffixes = []
        for key, value in self.children.items():
            if value.is_word:
                suffixes.append(suffix + key)
            suffixes.extend(value.suffixes(suffix + key))
        return suffixes


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        self.root.insert(word)

    def find(self, prefix):
        """
        Time Complexity: O(n)
        since we are iterating through each character in the prefix
        Space Complexity: O(1)
        since we are not creating any new data structure
        """
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node


my_trie = Trie()
wordList = [
    "ant",
    "anthology",
    "antagonist",
    "antonym",
    "fun",
    "function",
    "factory",
    "trie",
    "trigger",
    "trigonometry",
    "tripod",
]
for word in wordList:
    my_trie.insert(word)


def test(prefix):
    if not prefix:
        return None
    prefix_node = my_trie.find(prefix)
    if prefix_node:
        return prefix_node.suffixes()
    else:
        return prefix + " not found"


if __name__ == "__main__":
    assert test("ant") == ["hology", "agonist", "onym"], print("Test 01 failed")
    assert test("f") == ["un", "unction", "actory"], print("Test 02 failed")
    assert test("fu") == ["n", "nction"], print("Test 03 failed")
    assert test("tri") == ["e", "gger", "gonometry", "pod"], print("Test 04 failed")
    # Edge cases, None, empty string, string not in trie, and very long string
    assert test(None) == None, print("Test 05 failed")
    assert test("") == None, print("Test 06 failed")
    assert test("blah") == "blah not found", print("Test 07 failed")
    long_string = "a" * 10000
    assert test(long_string) == f"{long_string} not found", print("Test 08 failed")
    print("All tests passed for autocomplete_with_tries.py")
