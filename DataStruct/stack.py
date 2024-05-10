# 展示数据，第一列是空和top，第二列是元素


import streamlit as st
import pandas as pd
MAX_LEN = 8
# 上传文件✅✨❓❗🆘🈚🈲🌈🌍🌒🌸🍁💯🍄🍅🏰🏵️🏀🐁🐇	🐤🐬🐲👏👻💀😀😁😂😅😇😘😭😱🙉🙊🙈🚀🤔🤖🤗🤡🥰☀️⭐🎉

def change_list2special(mylist:list):
    list1 = []
    list2 = []
    for i in range(20):
        if i==20-len(mylist):
            list1.append('->')  
        else:
            list1.append('')
        if i>=20-len(mylist):
            list2.append(mylist[len(mylist)-20-i])
    
def show(mylist:list) -> pd.DataFrame:
    data = {
        'col1':[],
        'col2':[]
    }
    for i in range(MAX_LEN-len(mylist)):
        data['col1'].append("")
        data['col2'].append("") 
    for index in range(len(mylist)):
        if index == 0:
            data['col1'].append("->")
            data['col2'].append(mylist[len(mylist)-1])
        else:
            data['col1'].append(" ")
            data['col2'].append(mylist[len(mylist)-index-1])
    
    data = pd.DataFrame(data)
    return data
if 'stack' not in st.session_state:
    st.session_state['stack'] = []
col1, col2 = st.columns(2)
with col1:
    message = st.text_input("请输入压栈元素： ", value="")
    if st.button("add"):
        if message:
            if len(st.session_state['stack'])<=MAX_LEN:
                st.session_state['stack'].append(message)
                st.write(f"{message} 入栈 ！🥰")
                # st.experimental_rerun()
            else:
                st.write("满了满了，别加了，🈲")
        else:
            st.write("没输入text，记得输入呦🈚")
    if st.button("delete"):
        if st.session_state['stack']:
            out = st.session_state['stack'].pop()
            st.write(f"{out}  出栈！😭")
        else:
            st.write("哭了，毁了，全部都毁了,啥都没有了 😭")
with col2:

    st.write(show(st.session_state['stack']))
st.text("栈的基本原则是先进后出，就像将书堆叠起来，放在箱子里，\n放的时候一本一本放，拿的时候必须将最上面的书拿走才能拿到下面的书")

