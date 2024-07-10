import streamlit as st
import time
def findIndex(a:str) -> int:
    sign = False
    for index,i in enumerate(a):
        if sign and i == "#":
            return index
        if ord(i)>=48 and ord(i)<= 57:
            sign = True
    
def transforme(state:str,t:str):
    next_state = ""
    next_text = ""
    next_step = 0
    if state == "<":
        if t == "1":
            next_text = "0"
            next_state = "<"
            next_step = -1
        if t == "0" or t == "#":
            next_text = "1"
            next_state = ">"
            next_step = 1
    if state == ">":
        next_step = 1
        next_text = t
        next_state = state
        if t == "#":
            next_state = "h"
            next_step = 0
    return next_state,next_text,next_step
if "state" not in st.session_state:
    st.session_state.state = "h"
if "text" not in st.session_state:
    st.session_state.text = "###1010110####"
if "last_index" not in st.session_state:
    st.session_state.last_index = findIndex(st.session_state.text)
if "start" not in st.session_state:
    st.session_state.start = False
st.markdown("# Turing Mechine Visualization")
st.markdown("### 以二进制加法举例")

col = st.columns(len(st.session_state.text))

color = ""
for i in range(len(col)):
    with col[i]:
        if st.session_state.text[i] == "#":
            color = "#00662F"
        else:
            color = "#00b07f"
        st.markdown(f"""
        <div style='width: 30px; height: 30px; background-color: {color};display: flex; justify-content: center; align-items: center;'>{st.session_state.text[i]}</div>
        """, unsafe_allow_html=True)
print(len(col),st.session_state.last_index)
with col[st.session_state.last_index]:
    st.markdown(f"""
        <div style='width: 30px; height: 30px; display: flex; justify-content: center; align-items: center;'>↑</div>
        """, unsafe_allow_html=True)
with col[st.session_state.last_index]:
    st.markdown(f"""
        <div style='width: 30px; height: 30px; background-color: {color};display: flex; justify-content: center; align-items: center;'>{st.session_state.state}</div>
        """, unsafe_allow_html=True)

col1,col2 = st.columns(2)
with col1:
    if st.button("start"):
        st.session_state.last_index -= 1
        st.session_state.start = True
        st.session_state.state = "<"
        st.rerun()
with col2:
    if st.button("reset"):
        st.session_state.last_index = findIndex(st.session_state.text)
        st.session_state.text = "###1010110####"
        st.session_state.start = False
        st.rerun()
if st.session_state.start:
    st.session_state.state,text,step = transforme(st.session_state.state,st.session_state.text[st.session_state.last_index])
    if step == 0:
        st.session_state.start = False
        st.rerun()
    st.session_state.text = st.session_state.text[:st.session_state.last_index] + text + st.session_state.text[st.session_state.last_index + 1:] 
    st.session_state.last_index += step
    time.sleep(2)
    st.rerun()
# with col[1]:
#     st.markdown("""
#     <div style='width: 30px; height: 30px; background-color: blue;display: flex; justify-content: center; align-items: center;'>2</div>
#     """, unsafe_allow_html=True)
