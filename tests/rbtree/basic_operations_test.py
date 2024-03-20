import unittest
import sys
from streamlit_ml.lib.data_structures.red_black_tree import RedBlackTree, RBTNode

class TestRBTree(unittest.TestCase):
    def test_left_rotation(self):
        tree = RedBlackTree()
        x = RBTNode(key='x', left=tree.nil, right=tree.nil, parent=tree.nil)
        y = RBTNode(key='y', left=tree.nil, right=tree.nil, parent=tree.nil)
        alpha = RBTNode(key='alpha', left=tree.nil, right=tree.nil, parent=tree.nil)
        betta = RBTNode(key='betta', left=tree.nil, right=tree.nil, parent=tree.nil)
        gamma = RBTNode(key='gamma', left=tree.nil, right=tree.nil, parent=tree.nil)

        tree.root = x
        x.left = alpha
        alpha.parent = x
        x.right = y
        y.parent = x
        y.left = betta
        betta.parent = y
        y.right = gamma
        gamma.parent = y

        tree._RedBlackTree__left_rotate(x)

        self.assertTrue([
            x.left == alpha,
            alpha.parent == x,
            x.left == betta,
            betta.parent == x,
            x.parent == y,
            y.left == x,
            y.right == gamma,
            gamma.parent == y,
            tree.root == y,
        ])


    def test_right_rotation(self):
        tree = RedBlackTree()
        x = RBTNode(key='x', left=tree.nil, right=tree.nil, parent=tree.nil)
        y = RBTNode(key='y', left=tree.nil, right=tree.nil, parent=tree.nil)
        alpha = RBTNode(key='alpha', left=tree.nil, right=tree.nil, parent=tree.nil)
        betta = RBTNode(key='betta', left=tree.nil, right=tree.nil, parent=tree.nil)
        gamma = RBTNode(key='gamma', left=tree.nil, right=tree.nil, parent=tree.nil)

        tree.root = x
        x.right = gamma
        gamma.parent = x
        x.left = y
        y.parent = x
        y.left = alpha
        alpha.parent = y
        y.right = betta
        betta.parent = y

        tree._RedBlackTree__right_rotate(x)

        self.assertTrue([
            tree.root == y,
            y.left == alpha,
            alpha.parent == y,
            y.right == x,
            x.parent == y,
            x.left == betta,
            betta.parent == x,
            x.right == gamma,
            gamma.parent == x,
        ])



if __name__ == '__main__':
    path = '~/Projects/AppliedProgramming/4thSemestr'
    if  not path in sys.path:
        sys.path.append(path)
    unittest.main()

