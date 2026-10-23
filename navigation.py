import streamlit as st
from time import sleep

def make_sidebar():
    with st.sidebar:
        if st.session_state.get("logged_in", False):
            st.page_link("pages/home.py", label="Home")
            st.page_link("pages/Dashbord.py", label="Dashboard")
            st.page_link("pages/Patientdata.py", label="Patient Data")

            st.write("")
            if st.button("Log out"):
                logout()
        else:
            st.caption("Please log in to continue")

def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("login.py")
