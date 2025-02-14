import streamlit as st
import pandas as ps

name = st.text_input("Enter you full name: ")
age = st.text_input("Enter your age: ")
addr = st.text_area("Enter your address: ")
cat = st.selectbox("Enter your category: ",("Gen","OBC/SC/ST"))

button = st.button("Submit")
if button:
    st.markdown(f"""
                Name: {name}
                Age: {age}
                Address: {addr}
                Categoty: {cat}
                """)