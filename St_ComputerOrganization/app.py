import streamlit as st
from components.simulator import Simulator


def main():
    st.title("Computer Organization Simulator")

    st.write("Enter a simple C program with variable declarations and assignments.")
    st.write("Supported operations: assignment, addition (+), multiplication (*)")

    code = st.text_area("Enter your code here:", height=200)

    simulator = Simulator(code)

    if st.button("Start Simulation"):
        simulator.run()


if __name__ == "__main__":
    main()
