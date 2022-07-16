import streamlit as st

num1 = st.number_input("Enter any number")
if num1%2 == 0:
    st.write("It is even")
else:
    st.write("It is odd")

num2 = st.slider("Pick a number",1,10)
st.write(f"You picked {num2}")
for i in range(1,11):
    j = num2*i
    st.write(f"{num2} * {i} = {j}")


num3 = st.slider("Pick another number",1,10)
st.write(f"You picked {num3}")

i=1
while i<=10:
    j = num3*i
    st.write(f"{num3} * {i} = {j}")
    i= i +1
