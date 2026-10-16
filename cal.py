import streamlit as st
st.title("Addition")
number_1 = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write("The current number is ", number_1)
number_2 = st.number_input("Insert another number", value=None, placeholder="Type another number...")
st.write("The current number is ", number_2)
if st.button("add"):
    st.write(number_1+number_2)
st.image("img/cat.jpg")