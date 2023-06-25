import streamlit as st
import plotly.express as px
from backend import get_date

st.title("Weather Forcast for Upcoming Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for next {days} days in {place}")

if place:
    try:
        filtered_data = get_date(place, days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"] for dict in filtered_data]
            temperature = [temp / 10 for temp in temperature]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("**THAT PLACE DOES NOT EXIST**", )
