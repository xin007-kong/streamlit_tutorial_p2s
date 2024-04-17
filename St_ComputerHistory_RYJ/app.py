import streamlit as st
from streamlit_timeline import timeline
import json

# 加载事件数据
with open("events.json", "r", encoding='utf-8') as f:
    events = json.load(f)

# 设置页面配置
st.set_page_config(page_title="计算机发展史时间线", layout="wide")

# 标题
st.title("计算机发展史时间线")

# 渲染时间线
timeline(events, height=600)
