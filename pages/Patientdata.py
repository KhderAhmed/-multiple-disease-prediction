
# Using an f-string that does not have any interpolated variables
import streamlit as st
import sqlite3
import pandas as pd
import streamlit as ast 
from navigation import make_sidebar
make_sidebar()

st.markdown(
  '''<style>
    #MainMenu{visibility: hidden;} footer{visibility: hidden;}
    #root>div:nth-child(1)>div>div>div>div>section>div{padding-top: .2rem;}
  </style>''', unsafe_allow_html=True
)

con=sqlite3.connect('Patientdata.db')
cur=con.cursor()
cur.execute(
  '''
    CREATE TABLE IF NOT EXISTS Patientdata (
      namecol TEXT, 
      agecol TEXT, 
      notescol TEXT
    )
  '''  # key_col INTEGER NOT NULL PRIMARY KEY,
)

st.title('Patient Data')
col1, col2=st.columns([3,3])
with col1:
  names=[
    str(row[0]) for row in cur.execute(
      f"SELECT namecol FROM Patientdata;"
    )
  ]
  names.insert(0, '')
  name_to_update=st.selectbox('', names)
  if name_to_update!='':
    createorupdate='update'
    row_to_update=cur.execute(
      f'SELECT * FROM Patientdata WHERE namecol="{name_to_update}";'
    )
    nameval=row_to_update[0]
    ageval=int(row_to_update[1])
    notesval=row_to_update[2]
  else:
    createorupdate='create'
    nameval=''
    ageval=25
    notesval=''
  with st.form("Create or Update a Row of Data", clear_on_submit=True):
    name=st.text_input('FullName', value=nameval)
    age=st.number_input(
      'Age', min_value=1, max_value=120, value=ageval, step=1
    )
    
    notes=st.text_area('Notes', placeholder='Some Text', value=notesval)
    if st.form_submit_button("Submit"):
      if createorupdate=='create':
        cur.execute(  
          '''
            INSERT INTO Patientdata(
              namecol, 
              agecol, 
              notescol
            ) 
            VALUES(?,?,?)
          ''', (name,age,notes)
        )
        con.commit()  # con.close()
      else:
        cur.execute(
          ''' 
            UPDATE Patientdata
            SET namecol = ? ,
                agecol = ? ,
                notescol = ?
            WHERE namecol = ?;
          ''', (
            name,     
            age, 
            notes, 
          )
      )
        con.commit()  # con.close()
        st.experimental_rerun()
    if st.form_submit_button("Delete"):
      cur.execute(
        f'''DELETE FROM Patientdata WHERE namecol="{name_to_update}";'''
      )
      con.commit()
      st.write(f"{name_to_update} has been deleted")

with col2:
  st.header("Table Patientdata")
  if st.checkbox('Recheck to refresh display', value=True):
    myrows=[
      list(row) for row in cur.execute(
        '''
          SELECT 
            rowid, 
            namecol, 
            agecol, 
            notescol
          FROM Patientdata
          ORDER BY namecol
        '''
      )
    ]
    st.dataframe(
      pd.DataFrame(
        myrows, 
        columns=[
          'rowid', 
          'name', 
          'age', 
          'notes'
        ]
      ), 
      height=800
    )