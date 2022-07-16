import streamlit as st

if st.button("Click here"):
    st.snow()

radio_box = st.radio("Pick your color",['Red','Blue','Green'])
st.write(f"You picked {radio_box} ")