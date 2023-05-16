import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather prediction for the next few days")

place = st.text_input("Place: ")

days = st.slider("Forecast Days: ", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view: ", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

data = get_data(place, days, option)
d, t = get_data(days)

fig = px.line(x=d, y=t, labels={"x":"Dates", "y":"Temperature (C)"})
st.plotly_chart(fig)