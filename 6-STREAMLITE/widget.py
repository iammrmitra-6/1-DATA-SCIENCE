import streamlit as st

st.title("streamlit text input")

name=st.text_input("enter your name:")

age=st.slider("select your age :",0,25,100)

st.write(f"your age is {age}.")
if name:
    st.write(f"hello ,{name}")


options=["python","javascript","java","c++"]
choice=st.selectbox("choose your favourite lanhguage",options)
st.write(f"you selected {choice}.")

uploaded=st.file_uploader("choose a csv file",type="csv")