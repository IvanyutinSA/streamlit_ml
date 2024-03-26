from __future__ import annotations

class RBTNode:
    def __init__(
            self,
            key = None,
            parent: RBTNode = None,
            left: RBTNode = None, 
            right: RBTNode = None,
            color: str = 'BLACK',
    ):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.color = colour


class RedBlackTree:
    def __init__(self):
        self.nil = RBTNode()
        self.nil.right = self.nil
        self.nil.left = self.nil
        self.nil.parent = self.nil
        self.root = self.nil
        pass

    def search(self, item) -> RBTNode | None:
        x = self.root
        if x != self.nil:
            if x.key < item:
                x = x.left
            elif x.key == item:
                return x
            else:
                x = x.right
        return None
        

    def minimum(self, node: RBTNode | None = None) -> RBTNode:
        x = self.root if node is None else node
        if x.left != self.nil:
            return self.minimum(x.left)
        else:
            return x

    def maximum(self, node: RBTNode | None = None) -> RBTNode:
        x = self.root if node is None else node
        if x.right != self.nil:
            return self.maximum(x.right)
        else:
            return x

    def successor(self, x: RBTNode) -> RBTNode:
        if x.right != self.nil:
            return self.minimum(x.right)
        else:
            y = x.parent
            while y != self.nil and x == y.right:
                x = y
                y = y.parent
            return y

    def predecessor(self, x: RBTNode) -> RBTNode:
        if x.left != self.nil:
            return self.maximum(x.left)
        else:
            y = x.parent
            while y != self.nil and x == y.left:
                x = y
                y = y.parent
            return y

    def insert(self, z):
        x = self.root
        y = self.nil
        while not x == self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = 'RED'
        self.__insert_fixup(z)
        
    def delete(self, z: RBTNode) -> None:
        # x - child of y
        y = z
        y_original_color = y.color
        # z has at most 1 child
        if z.left == self.nil:
            x = z.right
            self.__transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.__transplant(z, z.right)
        # z has 2 children
        else:
            y = self.minimum(z.right)
            x = y.right
            if y != z.right:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            else:
                x.parent = y
            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'BLACK':
            self.__delete_fixup(x)


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

    def __insert_fixup(self, z: RBTNode) -> None:
        # proof: clrs - page 342
        # invariant of loop: 
        # a. Node z is red
        # b. if z.parent is the root, then z.parent is black
        # c. If the tree violates any of the red-black properties,
        #    then it violates either property 2 or property 4 
        #    if property 2, then z is root
        #    else z.parent is red
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                # case 1
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    # case 2
                    # falls into case 3
                    if z == z.parent.right:
                        z = z.parent
                        self.__left_rotate(z)
                    # case 3
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.__right_rotate(z.parent.parent)
            # symmetric
            else:
                y = z.parent.parent.left
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.__right_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.__left_rotate(z.parent.parent)
        self.root.color = 'BLACK'

    def __transplant(self, u: RBTNode, v: RBTNode) -> None:
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __delete_fixup(self, x: RBTNode) -> None:
        # 352 page
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.__left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.right.color == 'BLACK':
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self.__right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.__left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.__right_rotate(x.parent)
                    w = x.parent.left
                    if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                        w.color = 'RED'
                        x = x.parent
                    else:
                        if w.left.color == 'BLACK':
                            w.right.color = 'BLACK'
                            w.color = 'RED'
                            self.__left_rotate(w)
                            w = x.parent.left
                        w.color = x.parent.color
                        x.parent.color = 'BLACK'
                        w.left.color = 'BLACK'
                        self.__right_rotate(x.parent)
                        x = self.root
        x.color = 'BLACK'
        



