import streamlit as st
import pandas as pd
MAX_LEN = 5  
def show(mylist:list) -> pd.DataFrame:
    data = {
        'queue':[]
    }
    if len(mylist) > MAX_LEN:
        mylist = mylist[len(mylist)-MAX_LEN:]
    for index in range(len(mylist)):
        if index == 0:
            data['queue'].append(mylist[len(mylist)-1])
        else:
            data['queue'].append(mylist[len(mylist)-index-1])
    for i in range(MAX_LEN-len(mylist)):
        data['queue'].append("") 
        
    data = pd.DataFrame(data)
    return data



if 'queue' not in st.session_state:
    st.session_state['queue'] = []
col1, col2 = st.columns(2)
with col1:
    message = st.text_input("请输入入队元素： ", value="")
    if st.button("入队"):
        if message:
                st.session_state['queue'].append(message)
                st.write(f"{message} 入队！🥰")

                if len(st.session_state['queue']) > MAX_LEN:
                    st.write(f"{st.session_state['queue'][len(st.session_state['queue'])-MAX_LEN-1]} 出队！😭")
                # st.experimental_rerun()
        else:
            st.write("没输入text，记得输入呦")
with col2:

    st.write(show(st.session_state['queue']))
