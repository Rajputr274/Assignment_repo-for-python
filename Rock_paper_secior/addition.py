import streamlit as st
st.set_page_config(page_title="number Addition",page_icon="➕",layout="centered")
st.title("addition of two number")
st.caption("enter two number  and it will return addition of them ")

form=st.form("add_form")
num1=form.number_input("first number")
num2=form.number_input("second number")
submitted=form.form_submit_button("Calculate Sum")

if submitted:
    result=num1+num2
    st.divider()
    st.metric(label="Result",value=result)

for i in range(1,11):
    st.write(f"2  X  {i}  = {2*i}")