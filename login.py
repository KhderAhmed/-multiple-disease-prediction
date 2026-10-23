import streamlit as st
from time import sleep
from navigation import make_sidebar

make_sidebar()

st.title("Login Admin")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "Admin" and password == "123456789":
        st.session_state.logged_in = True
        st.success("Logged in successfully!")

        st.switch_page("pages/home.py")
        st.switch_page("pages/Dashbord.py")
        st.switch_page("pages/Patientdata.py")
    else:
        st.error("Incorrect username or password")
        
