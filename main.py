import streamlit as st
import plotly.graph_objects as go
import numpy as np
from css.markdown import load_button_css


st.set_page_config(page_title="Axis Freq - Live Monitor", layout="wide")
st.markdown(load_button_css(), unsafe_allow_html=True)

# button callback
if "running" not in st.session_state:
    st.session_state.running = False

def start_logging():
    st.session_state.running = True

def stop_logging():
    st.session_state.running = False


# UI
st.title("📊 Axis Freq - Live Dashboard")
st.write("")
st.write("")

# UI compresssion section
st.subheader("Suspension Compression")
st.divider()

# initial readout or setting
InitialCarWeight_kg = 1000
InitialStringPot_mm = 150

# 一行两列
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="InitialCarWeight_kg", value=InitialCarWeight_kg)
with col2:
    st.metric(label="InitialStringPot_mm", value=InitialStringPot_mm)
with col3:
        st.button(
            "Lock Initial Value",
            on_click=start_logging,
            key="lock_initial_log_compress_btn"
        )
st.divider()

# Plotly
def create_line_chart(title):
    x = np.arange(0, 50)
    y = np.random.randn(50).cumsum()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name=title))
    fig.update_layout(
        title=title,
        height=250,
        margin=dict(l=20, r=20, t=30, b=20)
    )
    return fig

# Plotly
titles = [
    "Load-FL", "Load-FR", "Load-RL", "Load-RR",
    "String-FL", "String-FR", "String-RL", "String-RR"
]

for row in range(2):
    cols = st.columns(4)
    for col in range(4):
        idx = row * 4 + col
        with cols[col]:
            st.plotly_chart(create_line_chart(titles[idx]), use_container_width=True)

st.divider()

# button
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    col1, col2 = st.columns(2)

    with col1:
        st.button(
            "▶ Start Logging",
            on_click=start_logging,
            key="start_log_compress_btn"
        )

    with col2:
        st.button(
            "🔴 Stop Logging",
            on_click=stop_logging,
            key="stop_log_compress_btn"
        )


# UI tension section
st.write("")
st.write("")
st.subheader("Suspension Tension")
st.divider()

# initial readout or setting
InitialStringPot_Tension_mm = 150

# 一行两列
col1, col2 = st.columns(2)
with col1:
    st.metric(label="InitialStringPot_Tension_mm", value=InitialStringPot_Tension_mm)
with col2:
        st.button(
            "Lock Initial Value - Tension",
            on_click=start_logging,
            key="lock_initial_log_tension_btn"
        )
st.divider()

# Plotly
def create_line_chart_tension(title):
    x = np.arange(0, 50)
    y = np.random.randn(50).cumsum()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name=title))
    fig.update_layout(
        title=title,
        height=250,
        margin=dict(l=20, r=20, t=30, b=20)
    )
    return fig

# Plotly
titles_tension = [
    "String-FL", "String-FR", "String-RL", "String-RR"
]

for row in range(1):
    cols = st.columns(4)
    for col in range(4):
        idx = row * 4 + col
        with cols[col]:
            st.plotly_chart(create_line_chart_tension(titles_tension[idx]), use_container_width=True)

st.divider()

# button
col_left_tension, col_center_tension, col_right_tension = st.columns([1, 2, 1])

with col_center_tension:
    col1_tension, col2_tension = st.columns(2)

    with col1_tension:
        st.button(
            "▶ Start Logging",
            on_click=start_logging,
            key="start_log_tension_btn"
        )

    with col2_tension:
        st.button(
            "🔴 Stop Logging",
            on_click=stop_logging,
            key="stop_log_tension_btn"
        )


# UI tension section
st.write("")
st.write("")
st.subheader("Generate & Export")
st.divider()

# button
col_left_generate, col_center_generate, col_right_generate = st.columns([1, 2, 1])

with col_center_generate:
    col1_generate, col2_export = st.columns(2)

    with col1_generate:
        st.button(
            "🚀 Generat",
            on_click=start_logging,
            key="start_log_generate_btn"
        )

    with col2_export:
        st.button(
            "📤 Export",
            on_click=stop_logging,
            key="stop_log_export_btn"
        )

# chart to show result





# TODO
# # ======================
# # status
# # ======================
# if st.session_state.running:
#     st.success("Logging Running ")
# else:
#     st.warning("Logging Stopped 🔴")

