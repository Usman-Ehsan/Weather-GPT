import streamlit as st
from meta_ai_api import MetaAI

def get_weather(country_name):
    llm = MetaAI()
    prompt = f"""You are a custom GPT, and you have to tell about the weather of countries that the user asks for: {country_name}

    You have to tell the weather of the country according to the following format:
    Country Name: Weather
    Example: India: Sunny
    Temperature: 20C
    Humidity: 60%
    Wind: 10km/h
    Precipitation: 0mm
    Cloud Cover: 50%
    Visibility: 10km
    Weather Description: Sunny

    

    If the user asks something else, clarify that you are a custom GPT and not trained on that topic. Stick to your topic and strictly follow the format and rules.
    """
    response = llm.prompt(prompt)
    return response["message"]

st.title("Weather Information Chatbot")

country = st.text_input("Enter the Country Name:")

if st.button("Get Weather"):
    if country:
        weather_info = get_weather(country)
        st.text_area("Weather Report:", weather_info, height=200)
    else:
        st.warning("Please enter a country name.")
