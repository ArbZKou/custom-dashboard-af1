import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="Axis Freq - Live Monitor", layout="wide")

st.title("📡 Axis Freq - Live Monitor")

# 初始化数据
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame({
        "t": [],
        "A": [],
        "B": [],
        "C": [],
        "D": []
    })

placeholder = st.empty()

# 模拟实时数据
t = 0

while True:
    # 新数据
    new_row = {
        "t": t,
        "A": np.sin(t / 5),
        "B": np.cos(t / 5),
        "C": np.sin(t / 10) * 2,
        "D": np.random.randn()
    }

    st.session_state.data = pd.concat(
        [st.session_state.data, pd.DataFrame([new_row])],
        ignore_index=True
    )

    df = st.session_state.data

    with placeholder.container():

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        with col1:
            st.subheader("Load-Cell vs Time")
            st.line_chart(df.set_index("t")["A"])

        with col2:
            st.subheader("Spring-Pot vs Time")
            st.line_chart(df.set_index("t")["B"])

        with col3:
            st.subheader("Load-Cell vs Spring-Pot")
            st.line_chart(df.set_index("t")["C"])

        with col4:
            st.subheader("TBC")
            st.line_chart(df.set_index("t")["D"])

    t += 1
    time.sleep(0.1)