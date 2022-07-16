import streamlit as st
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.subheader("This is subheader for cat")
    st.caption("This is caption for cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.subheader("This is subheader for dog")
    st.caption("This is caption for dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("A owl")
    st.subheader("This is subheader for owl")
    st.caption("This is caption for owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
