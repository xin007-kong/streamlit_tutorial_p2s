import sys
import os
sys.path.append(os.path.dirname(__file__))
from components.base import Graph
from components.graph_fuc import visualize_graph
import time
import streamlit as st
if __name__ == "__main__":
    if "graph" not in st.session_state:
        st.session_state.graph = Graph()
    if "travel" not in st.session_state:
        st.session_state.travel = []
    if "width" not in st.session_state:
        st.session_state.width = 0
    if "depth" not in st.session_state:
        st.session_state.depth = 0
    if "topology" not in st.session_state:
        st.session_state.topology = 0
    st.markdown(
        """
        <style>
        .stButton>button {
            display: flex;
            margin: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.sidebar:
        st.markdown("# 快速创建图")
        if st.button("创建图"):
            st.session_state.graph.add_node("1")
            st.session_state.graph.add_node("2")
            st.session_state.graph.add_node("3")
            st.session_state.graph.add_node("4")
            st.session_state.graph.add_node("5")
            st.session_state.graph.add_node("6")
            st.session_state.graph.add_node("7")
            st.session_state.graph.add_node("8")
            st.session_state.graph.add_node("9")

            st.session_state.graph.add_edge("1","2")
            st.session_state.graph.add_edge("1","3")
            st.session_state.graph.add_edge("1","4")
            st.session_state.graph.add_edge("1","5")
            st.session_state.graph.add_edge("1","6")
            st.session_state.graph.add_edge("2","7")
            st.session_state.graph.add_edge("2","8")
            st.session_state.graph.add_edge("2","9")



        st.markdown("# 添加点")
        node = st.text_input("点")
        col1, col2= st.sidebar.columns(2)
        if st.button("确定",key = "a") and node:
            st.session_state.graph.add_node(node)



        st.markdown("# 添加边")
        col1,col2,col3= st.sidebar.columns([5,1,5])
        with col1:
            edge_start = st.text_input("起始点")
        with col2:
            st.text("\n")
            st.text("\n")
            st.text("->")
        with col3:
            edge_end = st.text_input("终点")
        # 创建按钮
        if st.button("确定", key = " b") and edge_start and edge_end:
            st.session_state.graph.add_edge(edge_start,edge_end)



        st.markdown("# 遍历图")
        if st.session_state.width >= 1:
            st.session_state.width -= 1
        if st.session_state.depth >= 1:
            st.session_state.depth -= 1
        if st.session_state.topology >= 1:
            st.session_state.topology -= 1
        if st.button("广度优先遍历"):
            st.session_state.graph.width_first_travel()
            st.session_state.width = len(st.session_state.graph.node)

        if st.button("深度优先遍历"):
            st.session_state.graph.depth_first_travel()
            st.session_state.depth = len(st.session_state.graph.node)

        if st.button("拓扑排序") or st.session_state.topology >= 1:

            if st.session_state.topology == 0:
                st.session_state.topology = len(st.session_state.graph.node)
            node,edge,result = st.session_state.graph.topology_sort(len(st.session_state.graph.node)-st.session_state.topology+1)



    if st.session_state.width >= 1:
        dot,nod = visualize_graph(st.session_state.graph,st.session_state.graph.width,len(st.session_state.graph.node)-st.session_state.width + 1)
        st.graphviz_chart(dot.source)
        st.text("广度优先遍历就是利用队列从起点开始，将接下来的节点全部加入到队列中，\n然后出队一个元素将其接下来的节点加入到队列中，递归进行。")
        col1,col2 = st.columns([1,10])
        with col1:
            st.text("出队元素")
            print("nodddd",nod)
            st.text(str(nod))
        with col2:
            st.text("队列元素")
            if n := st.session_state.graph.get_queue(nod).queue:
                if n:
                    text = ""
                    for a in n:
                        text += str(a) + " " 
                    st.text(text)
                else:
                    st.text(" ")
        time.sleep(2)
        st.rerun()
    elif st.session_state.depth >= 1:
        dot, nod = visualize_graph(st.session_state.graph,st.session_state.graph.depth,len(st.session_state.graph.node)-st.session_state.depth + 1)
        st.graphviz_chart(dot.source)
        st.text("深度优先遍历就是利用栈，从起点开始，将接下来的节点全部依次压入栈中，然后弹出来一个，将接下来的节点依次压入栈中，循环进行")
        col1,col2 = st.columns([1,10])
        with col1:
            st.text("出栈元素")
            # print("nodddd",nod)
            st.text(str(nod))
        with col2:
            st.text("栈内元素")
            if n := st.session_state.graph.get_stack(nod).stack:
                if n:
                    n.reverse()
                    text = ""
                    for a in n:
                        text += str(a) + " " 
                    st.text(text)
                else:
                    st.text(" ")
        time.sleep(2)
        st.rerun()
    elif st.session_state.topology >= 1:
        dot, nod = visualize_graph(graph=Graph(node,edge))
        st.graphviz_chart(dot.source)
        st.text("拓扑排序就是给有向无环图进行排序，遍历并删除入度为0的点，重复进行，体现的整个图的先后顺序")
        st.markdown("# 排序结果")
        text = ""
        for i in result:
            text += str(i) + " "
        st.text(text)
        time.sleep(2)
        st.rerun()
    else:
        dot, node = visualize_graph(st.session_state.graph)
        st.graphviz_chart(dot.source)
    if st.session_state.travel:
        st.markdown("# 遍历结果")
        st.text(str(a) + " " for a in st.session_state.travel)
