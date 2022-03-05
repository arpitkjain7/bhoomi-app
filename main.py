import streamlit as st
from external_call import APIInterface
import pandas as pd
import numpy as np

st.image("bhoomi-logo.png")
"""
### Data driven hydroponic agriculture automation suite.
Framework to automate all the processes and steps involved in hydroponic agriculture.
Its a pipeline management platform, that gives the farmer a holistic picture of the current conditions.
Smart actuator module, powered by ML algorithm to maintain the desired conditioning for the plants.
Checkout our [github](https://github.com/arpitkjain7/bhoomi) for more details.
"""
response_data = [
    {
        "water_temperature": 0,
        "tds_level": 0,
        "ph_level": 0,
        "air_temperature": 0,
    },
    {
        "water_temperature": 0,
        "tds_level": 0,
        "ph_level": 0,
        "air_temperature": 0,
    },
]
old_water_temp = response_data[1].get("water_temperature")
current_water_temp = response_data[0].get("water_temperature")
old_water_tds = response_data[1].get("tds_level")
current_water_tds = response_data[0].get("tds_level")
old_water_ph_level = response_data[1].get("ph_level")
current_water_ph_level = response_data[0].get("ph_level")
old_air_temp = response_data[1].get("air_temperature")
current_air_temp = response_data[0].get("air_temperature")
with st.expander("Setup"):
    ip = "192.168.1.100"
    ip = st.text_input(label="Server IP", value="", placeholder="Enter Server IP")
    st.write(ip)
    if ip == "":
        ip = "192.168.1.100"
        st.write(f"Server IP defaulted to: {ip}. Please update the IP address.")
    #     sensor_data_url = f"http://{ip}:8000/bhoomi/sensor/get_latest"
    #     response_data, _ = APIInterface().get(route=sensor_data_url)
    # else:
    #     sensor_data_url = f"http://{ip}:8000/bhoomi/sensor/get_latest"
    #     response_data, _ = APIInterface().get(route=sensor_data_url)
if st.button("Refresh"):
    sensor_data_url = f"http://{ip}:8000/bhoomi/sensor/get_latest"
    response_data, _ = APIInterface().get(route=sensor_data_url)
    old_water_temp = response_data[1].get("water_temperature")
    current_water_temp = response_data[0].get("water_temperature")
    old_water_tds = response_data[1].get("tds_level")
    current_water_tds = response_data[0].get("tds_level")
    old_water_ph_level = response_data[1].get("ph_level")
    current_water_ph_level = response_data[0].get("ph_level")
    old_air_temp = response_data[1].get("air_temperature")
    current_air_temp = response_data[0].get("air_temperature")
st.header("Live Sensor Data")
col1, col2 = st.columns(2)
col1.metric(
    "Water Hardness Level",
    f"{current_water_tds} ppm",
    f"{round(current_water_tds-old_water_tds,2)} ppm",
)
col2.metric(
    "Water pH Level",
    f"{current_water_ph_level}",
    f"{round(current_water_ph_level-old_water_ph_level,2)}",
)
col3, col4 = st.columns(2)
col3.metric(
    "Water Temperature",
    f"{current_water_temp} °C",
    f"{round(current_water_temp-old_water_temp,2)} °C",
)
col4.metric(
    "Air Temperature",
    f"{current_air_temp} °C",
    f"{round(current_air_temp-old_air_temp,2)} °C",
)
st.header("Historical Data")
with st.expander("Historical Data"):
    sensor_data_url = f"http://{ip}:8000/bhoomi/sensor/get_all"
    response_data, _ = APIInterface().get(route=sensor_data_url)
    df = pd.DataFrame(response_data)
    # df = df.set_index("created_at")
    ph_level_data = df["ph_level"]
    st.subheader("pH Level over time")
    st.line_chart(ph_level_data)
    tds_level_data = df["tds_level"]
    st.subheader("Water TDS Level over time")
    st.line_chart(tds_level_data)
    water_temperature_data = df["water_temperature"]
    st.subheader("Water Temperature over time")
    st.line_chart(water_temperature_data)
    air_temperature_data = df["air_temperature"]
    st.subheader("Air Temperature over time")
    st.line_chart(air_temperature_data)

st.write("copyright@Bhoomi")
