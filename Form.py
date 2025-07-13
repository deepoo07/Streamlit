import streamlit as st
with st.form("form"):
    st.write("Please fill the form")
    name=st.text_input("Name:")
    college_name=st.text_input("Institution Name:")
    Percentage=st.number_input("Percentage:",min_value=0.0, max_value=100.0, format="%.2f")
    Working=st.radio("Are you currently working?", ("Yes", "No"))
    
    submitted=st.form_submit_button("Submit")
    if submitted:
        st.write("Name:",name)
        st.write("Institution Name:",college_name)
        st.write(f"Percentage: {Percentage:.2f}%")
        st.write("Job Status:", Working)