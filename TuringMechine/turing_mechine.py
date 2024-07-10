import streamlit as st

def simulate_turing_machine(tape, head_pos, state, rules, step=1):
    """
    模拟图灵机的一步运行。
    
    :param tape: 纸带内容，列表形式，包含'0'、'1'和其他符号。
    :param head_pos: 读写头的当前位置。
    :param state: 图灵机的当前状态。
    :param rules: 转移规则，字典形式，例如{('A', '0'): ('B', '1', -1), ...}。
    :param step: 运行的步数。
    :return: 更新后的纸带内容、读写头位置和状态。
    """
    for _ in range(step):
        current_symbol = tape[head_pos]
        next_state, new_symbol, move = rules.get((state, current_symbol), (None, None, None))
        if next_state is not None:
            tape[head_pos] = new_symbol
            if move == -1:
                head_pos -= 1
            elif move == 1:
                head_pos += 1
            state = next_state
        else:
            break  # 没有规则匹配，停止模拟

    return tape, head_pos, state

def main():
    st.title('图灵机模拟')

    # 图灵机的初始状态
    tape = [None] * 10  # 纸带，None表示空白
    tape[0] = '1'       # 初始内容为...0001000...
    head_pos = 0        # 读写头初始位置
    state = 'A'         # 初始状态

    # 转移规则示例
    rules = {
        ('A', '1'): ('B', '0', 1),
        ('B', '0'): ('A', '1', -1),
    }

    # 模拟按钮
    step = st.sidebar.slider('步数', 1, 10, 1)
    if st.sidebar.button('运行'):
        tape, head_pos, state = simulate_turing_machine(tape, head_pos, state, rules, step)

    # 展示纸带和读写头位置
    st.subheader('纸带内容')
    st.write(tape)
    st.subheader('读写头位置')
    st.write(head_pos)

    # 展示当前状态
    st.subheader('当前状态')
    st.write(state)

if __name__ == '__main__':
    main()