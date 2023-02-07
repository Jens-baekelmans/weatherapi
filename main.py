import streamlit as st
import requests


response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=50.85&longitude=4.35&hourly=temperature_2m")
st.write(response.json()['hourly']['temperature_2m'])





