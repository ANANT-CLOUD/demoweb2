import streamlit as st

name = st.text_input("ENTER YOUR NAME: ")
fname = st.text_input("ENTER YOUR FATHER NAME: ")
add = st.text_input("ENTER YOUR ADDRESS:")
bio = st.text_area("write about yourself in short:")
dept = st.selectbox("Enter your department:", ("BCA", "MCA", "B.TECH", "BBA", "MBA"))

button = st.button("DONE")
if button:
    st.markdown(f"""
    **Name:** {name}  
    **Father's Name:** {fname}  
    **Address:** {add}  
    **About:** {bio}  
    **Department:** {dept}  
    """)
