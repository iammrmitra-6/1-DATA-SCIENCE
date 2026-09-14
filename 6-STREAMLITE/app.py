import streamlit as st
import pandas as pd
import numpy as np

##title of the application
st.title("hello Streamlit")


##display simple text

st.write("this is a simple text")

df=pd.DataFrame({
    'first column' :[1,2,3,4],
    'second column' :[10,20,30,40]
})

##display dataframe
st.write("here is the dataframe")
st.write(df)

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)