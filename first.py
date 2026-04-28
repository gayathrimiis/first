import streamlit as st
st.title("Interactive Streamlit App")
name=st.text_input("Enter ur name")
if st.button("Submit"):
  st.write("Hello Welcome")

