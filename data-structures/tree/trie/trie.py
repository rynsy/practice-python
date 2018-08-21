class Node():
    def __init__(self):
        self.children = {}
        self.val = None
        self.terminated = False

class Trie():
    def __init__(self):
        self.root = Node()

    def find(self, node, key):
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.terminated

    def insert(self, string):
        node = self.root
        index_last_char = None
        for index_char, char in enumerate(string):
            if char in node.children:
                node = node.children[char]
            else:
                index_last_char = index_char
                break
        if index_last_char is not None:
            for char in string[last_index_char:]:
                node.children[char] = Node()
                node = node.children[char]
            node.terminated = True
