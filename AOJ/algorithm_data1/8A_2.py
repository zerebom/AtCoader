# import sys

# class Node:
#     __slots__ = ['key', 'left', 'right']
#     def __init__(self, key):
#         self.key = key
#         self.left = self.right = None

# root = None

# def insert(key):
#     global root
#     x, y = root, None
#     while x: x, y = x.left if key < x.key else x.right, x
#     if y is None: root = Node(key)
#     elif key < y.key: y.left = Node(key)
#     else: y.right = Node(key)

# def inorder(node):
#     return inorder(node.left) + f' {node.key}' + inorder(node.right) if node else ''
# def preorder(node):
#     return f' {node.key}' + preorder(node.left) + preorder(node.right) if node else ''

# input()
# for e in sys.stdin:
#     if e[0] == 'i': insert(int(e[7:]))
#     else: print(inorder(root)); print(preorder(root))

import sys
class Tree():
    def __init__(self):
        self.root = None
    def insert(self, key):
        z = Node(key)
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
    def print(self):
        print('',' '.join(map(str, self.root.inwalk())))
        print('',' '.join(map(str, self.root.prewalk())))
    
class Node():
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
    def prewalk(self):
        ret = [self.key]
        if self.left:
            ret += self.left.prewalk()
        if self.right:
            ret += self.right.prewalk()
        return ret
    def inwalk(self):
        ret = []
        if self.left:
            ret += self.left.inwalk()
        ret += [self.key]
        if self.right:
            ret += self.right.inwalk()
        return ret
tree = Tree()
n = sys.stdin.readline()
for line in sys.stdin:
    if line[0] == 'i':
        tree.insert(int(line.split()[1]))
    else:
        tree.print()
