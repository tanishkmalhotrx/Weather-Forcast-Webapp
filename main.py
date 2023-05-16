import streamlit as st
import plotly.express as px

st.title("Weather prediction for the next few days")

place = st.text_input("Place: ")

days = st.slider("Forcast Days: ", min_value=1, max_value=5,
                 help="Select the number of forcasted days")

option = st.selectbox("Select data to view: ", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2023-16-05", "2023-17-05", "2023-18-05"]
temperatures = ["36", "38", "39"]
temperatures = [days * i for i in  temperatures]

fig = px.line(x=dates, y=temperatures, labels={"x":"Dates", "y":"Temperature (C)"})
st.plotly_chart(fig)