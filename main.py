import streamlit as st

st.title("Weather prediction for the next few days")

place = st.text_input("Place: ")

days = st.slider("Forcast Days: ", min_value=1, max_value=5,
                 help="Select the number of forcasted days")

option = st.selectbox("Select data to view: ", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")