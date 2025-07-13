import streamlit as st
st.info('This is Data Science form.',icon="📊")
with st.form("form"):
    st.write("Please fill the form")
    name=st.text_input("*Name:")
    surname=st.text_input("Surname:")
    options = ["MSU Baroda", "IIT Bombay", "Other"]
    selected = st.selectbox("Institution:", options)
    if selected == "Other":
        college_name = st.text_input("*Enter your institution name:")
    else:
        college_name = selected

    Percentage=st.number_input("*Percentage:",min_value=0.0, max_value=100.0, format="%.2f")
    Working=st.radio("*Are you currently working?", ("Yes", "No"))
    
    submitted=st.form_submit_button("Submit")
    if submitted:
        if not name or not college_name or not Percentage or not Working:
            st.warning("⚠️ Please fill in all the * required fields.")
        else:
            st.success("Form submitted successfully!", icon="✅")
            st.write("Name:",name, surname)
            st.write("Institution Name:",college_name)
            st.write(f"Percentage: {Percentage:.2f}%")
            st.write("Job Status:", Working)