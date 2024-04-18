import streamlit as st
from graphviz import Digraph
import time
log_ = 1
class Node:
    def __init__(self, value,color=None):
        self.value = value
        self.color = color
        self.left : Node=None
        self.right : Node=None
        

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
def cut_pre_travel(root:Node, sign):
    if sign[0] == 0:
        return 
    if not root:
        return  
    if not root.color:
        root.color = "red"
        sign[0] = 0
        # print(f"{root.value}已变色")
        return 
    cut_pre_travel(root.left,sign)
    cut_pre_travel(root.right,sign)
    global log_
    # print(f"第{log_}次")
    log_ +=  1
    # return True
def reset(root:Node):
    if not root:
        return  
    if root.color:
        root.color = None
        # print(f"{root.value}已变色")
    reset(root.left)
    reset(root.right)
    
def cut_inorder_travel(root:Node,sign):
    if sign[0] == 0:
        return
    if not root:
        return
    cut_inorder_travel(root.left,sign)
    if not root.color and sign[0]:
        root.color = "red"
        sign[0] = 0
        # print(f"{root.value}已变色")
        return 
    cut_inorder_travel(root.right,sign)   
    
def cut_postorder_travel(root:Node,sign):
    if sign[0] == 0:
        return
    if not root:
        return
    cut_postorder_travel(root.left,sign)
    cut_postorder_travel(root.right,sign) 
    if not root.color and sign[0]:
        root.color = "red"
        sign[0] = 0
        # print(f"{root.value}已变色")
        return 
 
def main():
    st.title("Binary Tree Visualization")
    if "tree" not in st.session_state:
        st.session_state.tree = Node(1)
        st.session_state['tree'].left = Node(2)
        st.session_state['tree'].right = Node(3)
        st.session_state['tree'].left.left = Node(4)
        st.session_state['tree'].left.right = Node(5)
        st.session_state['tree'].right.left = Node(6)
        st.session_state['tree'].right.right = Node(7)
        st.session_state['tree'].left.left.left = Node(8)
        st.session_state['tree'].left.left.right = Node(9)
        st.session_state['tree'].left.right.left = Node(10)
        st.session_state['tree'].left.right.right = Node(11)
        st.session_state['tree'].right.left.left = Node(12)
        st.session_state['tree'].right.left.right = Node(13)
        st.session_state['tree'].right.right.left = Node(14)
        st.session_state['tree'].right.right.right = Node(15)
    if "log" not in st.session_state:
        st.session_state.log = [0,0,0]
    if "sign" not in st.session_state:
        st.session_state.sign = [0]
    if "count" not in st.session_state:
        st.session_state.count = 0
    # print(type(st.session_state.sign), st.session_state.sign)

    # Define your binary tree here


    # Visualize the binary tree
    tree_viz = visualize_tree(st.session_state['tree'])
    st.graphviz_chart(tree_viz.source)
    # ccol1,ccol2,ccol3 = st.sidebar.columns(3)
    # st.write("\n")
    # st.write("\n")
    # st.write("\n")
    # st.write("\n")
    # st.write("\n")

    # with ccol1:
    #     st.write(" ")
    #     st.write(" ")
    #     st.write(" ")
    #     st.write(" ")

    #     if st.button("hello",key="button1"):
    #         pass
    # with ccol2:
    #     st.write(" ")
    #     st.write(" ")
    #     st.write(" ")
    #     st.write(" ")

    #     if st.button("hello",key="button2"):
    #         pass
    # with ccol3:
    #     st.write(" ")
    #     st.write(" ")
    #     st.write(" ")
    #     st.write(" ")
    
    #     if st.button("hello",key="button3"):
    #         pass

    col1,col2,col3 = st.sidebar.columns(3)
    with col1:
        if st.button("前序遍历") or st.session_state["log"][0]:
            st.session_state["log"][0] = 1
            if st.session_state.count <= 16:
                st.session_state.sign = [1]
                cut_pre_travel(st.session_state.tree,st.session_state.sign)
                # tree_viz = visualize_tree(st.session_state['tree'])
                # st.graphviz_chart(tree_viz.source)
                print("st.session_state.count: ", st.session_state.count)
                time.sleep(1)
                st.session_state.count += 1
                st.rerun()
            else:
                st.session_state.count = 0
                st.session_state.log[0] = 0
                reset(st.session_state.tree)
                st.rerun()
            

    with col2:
        if st.button("中序遍历") or st.session_state["log"][1]:
            st.session_state["log"][1] = 1
            if st.session_state.count <= 16:
                st.session_state.sign = [1]
                cut_inorder_travel(st.session_state.tree,st.session_state.sign)
                # tree_viz = visualize_tree(st.session_state['tree'])
                # st.graphviz_chart(tree_viz.source)
                print("st.session_state.count: ", st.session_state.count)
                time.sleep(1)
                st.session_state.count += 1
                st.rerun()
            else:
                st.session_state.count = 0
                st.session_state.log[1] = 0
                reset(st.session_state.tree)
                st.rerun()
            
    with col3:
        if st.button("后序遍历") or st.session_state["log"][2]:
            st.session_state["log"][2] = 1
            if st.session_state.count <= 16:
                st.session_state.sign = [1]
                cut_postorder_travel(st.session_state.tree,st.session_state.sign)
                # tree_viz = visualize_tree(st.session_state['tree'])
                # st.graphviz_chart(tree_viz.source)
                print("st.session_state.count: ", st.session_state.count)
                time.sleep(1)
                st.session_state.count += 1
                st.rerun()
            else:
                st.session_state.count = 0
                st.session_state.log[2] = 0
                reset(st.session_state.tree)
                st.rerun()

if __name__ == "__main__":
    main()

