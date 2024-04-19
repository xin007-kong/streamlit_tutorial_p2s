import streamlit as st
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






    
