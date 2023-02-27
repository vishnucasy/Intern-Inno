import streamlit as st


st.title(":red[About] Me")


btn_click = st.button("Click to know About Me!")

if btn_click == True:
    st.text("My Name Is Vishnu Preeth")
    st.text("A Data Science Intern")
    st.text("Aged 24")
    st.text("Graduate in B-Tech Mechanical Engineering")
    st.text("Born in Kerala")

    