import streamlit as st


st.title("Calculator")

col1,col2=st.columns(2)
with col1:
    num1=st.number_input("Enter The First Number:",value=0.0)
with col2:
    num2=st.number_input("Enter The Second Number:",value=0.0)

operations=st.selectbox("Select Operation",["Add","Substract","Multiplication","Divide"])



if operations=="Add":
    st.success(num1+num2)
elif operations=="Substract":
    st.success(num1-num2)
elif operations=="Multiplication":
    st.success(num1*num2)
elif operations=="Divide":
    if num2!=0:
        st.success(num1/num2)
    else:
        st.error("Denominator Should not be Zero")

