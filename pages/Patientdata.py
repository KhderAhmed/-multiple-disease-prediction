import sqlite3
import pandas as pd
import streamlit as st
from navigation import make_sidebar

make_sidebar()

if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.switch_page("login.py")
    st.stop()

st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

conn = sqlite3.connect("Patientdata.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Patientdata (
        namecol TEXT,
        agecol INTEGER,
        notescol TEXT
    )
    """
)

st.title("Patient Data")

col1, col2 = st.columns([3, 3])

with col1:
    names = [str(row[0]) for row in cursor.execute("SELECT namecol FROM Patientdata;")]
    names.insert(0, "")
    name_to_update = st.selectbox("Select patient", names)

    if name_to_update != "":
        row = cursor.execute(
            'SELECT namecol, agecol, notescol FROM Patientdata WHERE namecol = ?',
            (name_to_update,)
        ).fetchone()
        nameval, ageval, notesval = row
        create_or_update = "update"
    else:
        create_or_update = "create"
        nameval, ageval, notesval = "", 25, ""

    with st.form("patient_form", clear_on_submit=True):
        name = st.text_input("Full Name", value=nameval)
        age = st.number_input("Age", min_value=1, max_value=120, value=ageval, step=1)
        notes = st.text_area("Notes", placeholder="Some Text", value=notesval)

        submit_col, delete_col = st.columns(2)

        if submit_col.form_submit_button("Submit"):
            if create_or_update == "create":
                cursor.execute(
                    "INSERT INTO Patientdata(namecol, agecol, notescol) VALUES (?, ?, ?)",
                    (name, age, notes),
                )
                conn.commit()
            else:
                cursor.execute(
                    "UPDATE Patientdata SET namecol = ?, agecol = ?, notescol = ? WHERE namecol = ?",
                    (name, age, notes, name_to_update),
                )
                conn.commit()
                st.rerun()

        if delete_col.form_submit_button("Delete"):
            if name_to_update:
                cursor.execute("DELETE FROM Patientdata WHERE namecol = ?", (name_to_update,))
                conn.commit()
                st.success(f"{name_to_update} has been deleted")
                st.rerun()

with col2:
    st.header("Patient Table")
    rows = cursor.execute(
        "SELECT rowid, namecol, agecol, notescol FROM Patientdata ORDER BY namecol"
    ).fetchall()
    df = pd.DataFrame(rows, columns=["rowid", "name", "age", "notes"])
    st.dataframe(df, height=800)
