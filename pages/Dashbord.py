import time
import numpy as np
import streamlit as st
from navigation import make_sidebar

if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.switch_page("login.py")
    st.stop()
make_sidebar()

st.title("Dashboard")
st.sidebar.header("Monitoring Dashboard")

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text(f"{i}% Complete")
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()
st.button("Re-run")
