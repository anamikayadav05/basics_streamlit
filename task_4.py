import streamlit as st

select = st.selectbox("Select your favourite ice-cream flavour",['Vanilla','Chocolate','Strawberry'])
st.write(f"You selected {select} flavour.")

multi_select = st.multiselect("Which ice-cream flavour do you like?",['Vanilla','Chocolate','Strawberry','Pistachio','Butterscotch'],)
st.write("You chose :", multi_select)

sprinkle = st.text_input("Enter your favourite sprinkles on ice-cream")
st.write(f"Your favourite sprinkles are {sprinkle}")

birt_date = st.date_input("Enter your birthdate")
st.write(f"Your birth date is {birt_date}")