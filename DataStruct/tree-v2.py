import sys
import os
import time
sys.path.append(os.path.dirname(__file__))
from components.base import Node,Tree
from components.tree_fuc import reset,visualize_tree
import streamlit as st
def main():
    if "tree" not in st.session_state:
        st.session_state.tree = Tree()
    if "travel" not in st.session_state:
        st.session_state.travel = [0,0,0]
    if "log" not in st.session_state:
        st.session_state.log = [0,0,0]
    build_tree,travel_tree= st.sidebar.columns(2)
    st.graphviz_chart(visualize_tree(st.session_state.tree.root).source)
    build_tree.title("构建树")
    with build_tree:
        if st.button("添加左子树"):
            st.session_state.tree.add_node(left=True)
            st.rerun()
        if st.button("添加右子树"):
            st.session_state.tree.add_node(right=True)
            st.rerun()
        if st.button("切换到左子树"):
            st.session_state.tree.change_now_node(left=True)
            st.rerun()
        if st.button("切换到右子树"):
            st.session_state.tree.change_now_node(right=True)
            st.rerun()
        if st.button("切换到parent"):
            st.session_state.tree.change_now_node(parent=True)
            st.rerun()
        if st.button("删除左子树"):
            st.session_state.tree.delete(left=True)
            st.rerun()
        if st.button("删除右子树"):
            st.session_state.tree.delete(right=True)
            st.rerun()
    travel_tree.title("遍历树")
    with travel_tree:
        if st.button("前序遍历") or st.session_state.travel[0]:
            if not st.session_state.travel[0]:
                st.session_state.travel[0] = st.session_state.tree.num + 1
                st.session_state.tree.now_node.color = None
            if st.session_state.travel[0]:
                st.session_state.log[0] = 1
            st.session_state.tree.pre_travel_pre_one(st.session_state.tree.root,st.session_state.log)
            st.session_state.travel[0] -= 1
            if st.session_state.travel[0] == 0:
                time.sleep(0.5)
                reset(st.session_state.tree.root)
            time.sleep(0.5)
            st.rerun()
        if st.button("中序遍历") or st.session_state.travel[1]:
            if not st.session_state.travel[1]:
                st.session_state.travel[1] = st.session_state.tree.num + 1
                st.session_state.tree.now_node.color = None
            if st.session_state.travel[1]:
                st.session_state.log[1] = 1
            st.session_state.tree.middle_travel_pre_one(st.session_state.tree.root,st.session_state.log)
            st.session_state.travel[1] -= 1
            if st.session_state.travel[1] == 0:
                time.sleep(0.5)
                reset(st.session_state.tree.root)
            time.sleep(0.5)
            st.rerun()
        if st.button("后序遍历") or st.session_state.travel[2]:
            if not st.session_state.travel[2]:
                st.session_state.travel[2] = st.session_state.tree.num + 1
                st.session_state.tree.now_node.color = None
            if st.session_state.travel[2]:
                st.session_state.log[2] = 1
            st.session_state.tree.end_travel_per_one(st.session_state.tree.root,st.session_state.log)
            st.session_state.travel[2] -= 1
            if st.session_state.travel[2] == 0:
                time.sleep(0.5)
                reset(st.session_state.tree.root)
            time.sleep(0.5)
            st.rerun()
        if st.button("重置"):
            reset(st.session_state.tree.root)
            st.rerun()

if __name__ == "__main__":
    main()