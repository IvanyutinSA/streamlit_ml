import streamlit as st
from streamlit_ml.lib.data_structures.red_black_tree import RedBlackTree, RBTNode

def display_tree(node: RBTNode, n = 0) -> None:
    color = ':' + node.color.lower()
    column = '|'*(n>0)
    minus = '-'*5*n
    if node.color != 'RED':
        st.write(f'{column}{minus}:blue[{node.key}]')
    else:
        st.write(f'{column}{minus}:red[{node.key}]')
    if node.key == 'nil':
        return
    display_tree(node.left, n+1)
    display_tree(node.right, n+1)
    

def insert(tree:RedBlackTree, x: int) -> None:
    tree.insert(RBTNode(key=x))

def delete(tree: RedBlackTree, x: int) -> None:
    x_node = tree.search(x)
    if x_node.key != 'nil':
        tree.delete(x_node)
        st.title(f'Element {x} successfully deleted')
    else:
        st.title(f'There\'s no such element: {x}')

def maximum(tree: RedBlackTree) -> None:
    st.title(f'Maximum element: {tree.maximum().key}')

def minimum(tree: RedBlackTree) -> None:
    st.title(f'Minimum element: {tree.minimum().key}')

def successor(tree: RedBlackTree, x: int) -> RBTNode | None:
    x_node = tree.search(x)
    if x_node.key != 'nil':
        st.title(f'Successor of {x} is {tree.successor(x_node).key}')
    else:
        st.title(f'There\'s no such element: {x}')

def predecessor(tree: RedBlackTree, x: int) -> RBTNode | None:
    x_node = tree.search(x)
    if x_node.key != 'nil':
        st.title(f'Predecessor of {x} is {tree.predecessor(x_node).key}')
    else:
        st.title(f'There\'s no such element: {x}')

def search(tree: RedBlackTree, x: int) -> None:
    x_node = tree.search(x)
    if x_node.key != 'nil':
        st.title('Search result: :green[Yes]')
    else:
        st.title('Search result: :red[No]')


def rb_tree():
    if 'tree' not in st.session_state:
        st.session_state['tree'] = RedBlackTree()
    tree = st.session_state['tree']

    with st.sidebar:
        x = int(st.number_input('Enter number'))
        action = lambda: ()

        if st.button('Insert'):
            action = lambda: insert(tree, x)

        if st.button('Delete'):
            action = lambda: delete(tree, x)

        if st.button('Search'):
            action = lambda: search(tree, x)

        if st.button('Minumum'):
            action = lambda: minimum(tree)

        if st.button('Maximum'):
            action = lambda: maximum(tree)

        if st.button('Successor'):
            action = lambda: successor(tree, x)

        if st.button('Predecessor'):
            action = lambda: predecessor(tree, x)

        action()

    display_tree(tree.root)



