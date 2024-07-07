from graphviz import Digraph
from typing import Dict, List
from base import Graph



def visualize_graph(graph: Graph,lis:List[int] = None,num:int = None):
    """
    lis is used to signing the index of travel, num is the current index of travel the graph
    """
    nod = ""
    dot = Digraph()
    for index in range(len(graph.node)):
        print(index, lis)
        if lis and num:
            if lis[index] <= num:
                if lis[index] == num:
                    nod = graph.node[index]
                    print("nod",nod)
                dot.node(graph.node[index],color="red",style="filled")
            else:
                dot.node(graph.node[index])
        else:
            dot.node(graph.node[index])
    if graph.edge:
        for keys in graph.edge.keys():
            for value in graph.edge[keys]:
                dot.edge(keys, value)
    
    return dot,nod


def visualize_tree(root):
    dot = Digraph()

    def add_nodes_edges(node, parent=None):
        if node is None:
            return
        node_attributes = {"label": str(node.value)}
        if node.color:
            node_attributes["color"] = node.color
            node_attributes["style"] = "filled"
        dot.node(str(node.value), **node_attributes)
        # print(node.value)
        if parent is not None:
            dot.edge(str(parent.value), str(node.value))
        add_nodes_edges(node=node.left, parent=node)
        add_nodes_edges(node=node.right, parent=node)

    add_nodes_edges(root)
    return dot
