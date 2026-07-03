import streamlit as st 

st.title("My first app created by Murari")

st.write("Welcome! This app calculates the square of a number")

st.header("Select a number")
number = st.slider("Pick a number", 0, 50, 5)

st.subheader("Result")
squared_number= number * number
st.write(f"The square of **{number}** is **{squared_number}**.")