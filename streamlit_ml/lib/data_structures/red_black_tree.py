from __future__ import annotations

class RBTNode:
    def __init__(
            self,
            key = None,
            parent: RBTNode = None,
            left: RBTNode = None, 
            right: RBTNode = None,
            colour: str = 'b',
    ):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.colour = colour


class RedBlackTree:
    def __init__(self):
        self.nil = RBTNode()
        self.nil.right = self.nil
        self.nil.left = self.nil
        self.nil.parent = self.nil
        self.root = self.nil
        pass

    def search(self):
        pass

    def minimum(self):
        pass

    def maximum(self):
        pass

    def successor(self):
        pass

    def predecessor(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

    def __left_rotate(self, x: RBTNode) -> None:
        y = x.right
        x.right = y.left
        if not y.left == self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else: 
            x.parent.right = y
        y.left = x
        x.parent = y


    def __right_rotate(self, x: RBTNode) -> None:
        y = x.left
        x.left = y.right

        if not y.right == self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == self.root:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

