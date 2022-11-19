import streamlit as st

st.header('Hello Page')

if st.button('Balloon'):
  st.balloons()
  
col1,col2 = st.columns(2)
with col1:
  st.write('LED')

with col2:
  radio=st.radio(label='radio', options=('On','Off'), key='k1',label_visibility='collapsed', horizontal=True)


        
