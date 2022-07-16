#importing libraries
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.title("Generates report of dataframe")
titanic = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
st.dataframe(titanic)

#generates report
report = ProfileReport(titanic)

#adding button
if st.button("Generates report"):
    st.title("Titanic Report")
    st_profile_report(report)
    