import os,sys
sys.path.append(os.path.dirname(__file__))
import streamlit as st
from typing import Dict , List
class Node:
    def __init__(self, value,color=None,parent=None):
        self.value = value
        self.color = color
        self.left : Node=None
        self.right : Node=None
        self.parent = parent

class Tree:
    def __init__(self,node=Node(value=1,color="red")) -> None:
        self.root = node
        self.num = 1
        self.now_node = node
    def change_now_node(self,left=False,right=False,parent=False):
        if self.now_node.left and left:
            self.now_node.color = None
            self.now_node = self.now_node.left
            self.now_node.color = "red"
            return True
        elif self.now_node.right and right:
            self.now_node.color = None
            self.now_node = self.now_node.right
            self.now_node.color = "red"
            return True
        elif self.now_node.parent and parent:
            self.now_node.color = None
            self.now_node = self.now_node.parent
            self.now_node.color  = "red"
        return False
    def skip2leaf(self,left=True,right=False,parent=False):
        pass
    def add_node(self,left=False,right=False):
        if not self.now_node.left and left:
            self.num += 1
            self.now_node.left = Node(value=self.num,parent=self.now_node)
            print(f"添加节点为{self.num}的左子树,父节点为{self.now_node.value}")
        elif not self.now_node.right and right:
            self.num += 1
            self.now_node.right = Node(value=self.num,parent=self.now_node)
            print(f"添加节点为{self.num}的右子树,父节点为{self.now_node.value}")

    def delete(self,left=False,right=False):
        if self.now_node.left and left :
            self.now_node.left = None
            return True
        elif self.now_node.right and right:
            self.now_node.right = None
            return True
    # @st.cache_resource
    def log(fuc):
        def wrapper(*args,**kwargs):
            # print("开始遍历")
            result = fuc(*args,**kwargs)
            print(result)
        return wrapper
    @log
    def pre_travel_pre_one(self,root,sign):
        if sign[0] == 0:
            return 
        if not root:
            return  
        if not root.color:
            root.color = "red"
            sign[0] = 0
            # print(f"{root.value}已变色")
            return root.value
        self.pre_travel_pre_one(root.left,sign)
        self.pre_travel_pre_one(root.right,sign)
    @log
    def middle_travel_pre_one(self,root,sign):
        if sign[1] == 0:
            return
        if not root:
            return
        num = self.middle_travel_pre_one(root.left,sign)
        if not num:
            if not root.color and sign[1]:
                root.color = "red"
                sign[1] = 0
                print(f"{root.value}已变色")
                return root.value
            self.middle_travel_pre_one(root.right,sign) 
    @log        
    def end_travel_per_one(self,root,sign):
        if sign[2] == 0:
            return
        if not root:
            return
        self.end_travel_per_one(root.left,sign)
        self.end_travel_per_one(root.right,sign) 
        if not root.color and sign[2]:
            root.color = "red"
            sign[2] = 0
            # print(f"{root.value}已变色")
            return root.value
class Graph:
    def __init__(self):
        self.node:List[str] = []
        self.edge: Dict[str, List[str]] = {}
        self.width:List[int] = []
        self.depth:List[int] = []
        self.topology:List[int] = []

    def add_node(self, node: str):
        if not self.node.__contains__(node):
            self.node.append(node)

    def add_edge(self, start: str, end: str):
        self.add_node(start)
        self.add_node(end)
        if start not in self.edge:
            self.edge[start] = [end]  # 使用字符串列表
        elif end not in self.edge[start]:  # 避免重复边
            self.edge[start].append(end)

    def delete_edge(self, start: str, end: str):
        if start in self.edge and end in self.edge[start]:  # 检查边是否存在
            self.edge[start].remove(end)
    def delete_node(self, node: str):
        if node in self.node:
            self.node.remove(node)
        if node in self.edge:
            del self.edge[node]
        for key in self.edge:
            if node in self.edge[key]:
                self.edge[key].remove(node)
    def width_first_travel(self):
        # queue 实现, 遍历的顺序
        num = len(self.node)
        self.width = [0]*num
        queue = Queue()
        if num != 0:
            queue.enqueue(self.node[0])
        else:
            return
        index = 1
        while num != 0:
            nod = queue.dequeue()
            if self.width[self.node.index(nod)] == 0:
                self.width[self.node.index(nod)] = index
                index += 1
            for key in self.edge:
                if key == nod:
                    for n in self.edge[key]:
                        queue.enqueue(n)
                    break
            num-=1
        print(self.width)
    def get_queue(self,nodd:str):
        num = len(self.node)
        w = [0]*num
        queue = Queue()
        if num != 0:
            queue.enqueue(self.node[0])
        else:
            return None
        index = 1
        while num != 0:
            nod = queue.dequeue()
            if w[self.node.index(nod)] == 0:
                w[self.node.index(nod)] = index
                index += 1
            for key in self.edge:
                if key == nod:
                    for n in self.edge[key]:
                        queue.enqueue(n)
                    break
            if nod == nodd:
                return queue
            num-=1
    def depth_first_travel(self):
        # stack 实现
        pass
    def topology_sort(self):
        # queue 实现
        pass

class Queue:
    def __init__(self) -> None:
        self.queue:List[str] = []

    def enqueue(self,obj:str):
        self.queue.append(obj)

    def dequeue(self) -> str:
        if len(self.queue) != 0:
            text = self.queue[0]
            self.queue.remove(text)
            return text
        return "!<0>!"
        
class Stack:
    def __init__(self) -> None:
        self.stack:List[str] = []

    def pop(self) -> str:
        if len(self.stack) != 0:
            text = self.stack[-1]
            self.stack.remove(text)
            return text
    
    def push(self,text:str):
        self.stack.append(text)

    
