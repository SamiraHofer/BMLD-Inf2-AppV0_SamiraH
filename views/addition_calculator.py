import streamlit as st
from functions import add

st.title("Addition")

st.wirte("Hier ist mein Rechner")

with st.form("addition_form"):
    nummer_1 = st.number_input()
    nummer_2 = st.number_input()
    resultat = add(nummer_1, nummer_2)

    submit = st.form_submit_button("Berechnen")

 if submit:
        st.write(resultat)
        