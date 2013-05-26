# Some classes/examples for basic data structure elements.

# Weighted Directed Graph (http://www.python.org/doc/essays/graphs/)
graph = {'A': {'B': 5, 'C': 3},
        'B': {'C': 4, 'D': 8},
        'C': {'D': 1},
        'D': {'C': 4},
        'E': {'F': 2},
        'F': {'C': 7}}

# Binary tree
class BTNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
