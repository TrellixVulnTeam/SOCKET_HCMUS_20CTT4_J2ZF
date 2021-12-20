        #               R
        #              /|\
        #             / | \
        #            a  b  c
        #           /|\
        #          / | \ 
        #         b  d  e
        #  ... (trie tree)
        
from os import pardir


class Node():
    # struct of trie node
    def __init__(self, character):
        self.character = character
        self.isEndOfString = False
        # a counter indicating how many times a word is inserted (if this node's isEndOfString is True)
        self.counter = 0
        # a dictionary of child nodes keys are characters, values are nodes
        self.children = {}

class TrieTree(object):
    def __init__(self):
        self.TrieRoot = Node("")
    def add(self, strg):
        parentNode = self.TrieRoot
        # Loop through each character in the strg
        # Check if there is no child containing the character, 
        # create a new child for the current node
        # If a character is not found, create a new node in the trie
        for character in strg:
            if character in parentNode.children:
                parentNode = parentNode.children[character]
            else:
                newNode = Node(character)
                parentNode.children[character] = newNode
                parentNode = newNode
        # Mark the end of a word
        parentNode.isEndOfString = True
        # Increment the counter to indicate that we see this word once more
        parentNode.counter += 1

    def query(self, keyPrefix):
        self.output = []
        parent = self.TrieRoot
        # Check if the prefix is in the trie
        for char in keyPrefix:
            if char in parent.children:
                parent = parent.children[char]
            else:
                return []
        # Traverse the trie to get all candidates
        self.DepthFirstSearch(parent, keyPrefix[:-1])
        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def DepthFirstSearch(self, startNode, prefix):
        # node is a start node with
        # prefix: the current prefix, for tracing a word while traversing the trie
        if startNode.isEndOfString:
            self.output.append((prefix + startNode.character, startNode.counter))
        for child in startNode.children.values():
            self.DepthFirstSearch(child, prefix + startNode.character)

# a = TrieTree()
# a.add("Quảng Ngãi")
# a.add("Quảng Nam")
# a.add("Hà Nội")
# a.add("Hồ Chí Minh")
# a.add("Hải Phòng")
# print(a.query("Quảng"))