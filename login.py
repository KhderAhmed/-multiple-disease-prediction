import os
import streamlit as st
from time import sleep
from navigation import make_sidebar

make_sidebar()

st.title("Login Admin")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    expected_user = os.getenv("APP_USERNAME", "Admin")
    expected_pass = os.getenv("APP_PASSWORD", "123456789")

    if username == expected_user and password == expected_pass:
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        st.switch_page("pages/home.py")
    else:
        st.error("Incorrect username or password")
