import streamlit as st

st.set_page_config(page_title="LegalEase", layout="centered")

st.markdown("<h2 style='text-align: center;'>AI Legal Document Generator</h2>", unsafe_allow_html=True)

st.write("Welcome to LegalEase - Generate legal documents using AI")

document_type = st.selectbox("Document Type", ["Contract", "Agreement", "NDA", "Lease"])
parties = st.text_input("Involved Parties")
terms = st.text_area("Terms and Conditions")
dates = st.date_input("Effective Date")

if st.button("Generate Document"):
    st.success("Document Generated Successfully!")
    st.write(f"**Document Type:** {document_type}")
    st.write(f"**Parties:** {parties}")
    st.write(f"**Terms:** {terms}")
    st.write(f"**Date:** {dates}")
