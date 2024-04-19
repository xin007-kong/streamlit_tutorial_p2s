from .base import Node
from graphviz import Digraph
def build_tree(node:Node,left=True,right=False):
    new_tree = Node()
    if left:
        node.left =  new_tree
    else:
        node.right = new_tree
    return node
def skip2leaf(root:Node,left=True,right=False):
    # root should be the root of our tree
    pass
def visualize_tree(root):
    dot = Digraph()
    def add_nodes_edges(node, parent=None):
        if node is None:
            return
        node_attributes = {"label": str(node.value)}
        if node.color:
            node_attributes["color"] = node.color
            node_attributes["style"] = "filled"
        dot.node(str(node.value),**node_attributes)
        # print(node.value)
        if parent is not None:
            dot.edge(str(parent.value), str(node.value))
        add_nodes_edges(node = node.left, parent=node)
        add_nodes_edges(node = node.right, parent=node)

    add_nodes_edges(root)
    return dot
def reset(root:Node):
    if not root:
        return  
    if root.color:
        root.color = None
        # print(f"{root.value}已变色")
    reset(root.left)
    reset(root.right)