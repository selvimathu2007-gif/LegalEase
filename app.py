import streamlit as st

st.title("LegalEase - AI Legal Document Generator")

st.write("Generate legal documents easily")

doc_type = st.selectbox("Document Type", ["Rental Agreement", "Sale Agreement", "Employment Contract", "NDA"])
party1 = st.text_input("Party 1 Name")
party2 = st.text_input("Party 2 Name")
terms = st.text_area("Terms and Conditions")
date = st.date_input("Date")

if st.button("Generate Document"):
    st.subheader("Generated Document")
    st.write(f"*{doc_type}*")
    st.write(f"This agreement is made on {date} between {party1} and {party2}.")
    st.write("Terms:")
    st.write(terms)
    st.success("Document generated successfully!")