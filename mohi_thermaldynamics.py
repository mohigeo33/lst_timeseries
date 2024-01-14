import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
import altair as alt
DATA_URL = "https://raw.githubusercontent.com/mohigeo33/lst_timeseries/main/lst.csv"
st.title("Thermal Dynamics of a City")
st.markdown("This application is a dashboard that can be used to understand the thermal dynamics of Phnom Penh City (Cambodia) through time series analysis of land surface temperature (LST) ☀️🏙️📈")
@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
data = load_data()
data = data[data['MinLST'] >= 20]
raw_data = data
st.markdown("<h2 style='text-align: center; font-size: 24px;'>1. Selected images, source satellites and cloud coverage</h2>", unsafe_allow_html=True)
sensor_label = {
    'LS5': 'Landsat 5',
    'LS7': 'Landsat 7',
    'LS8': 'Landsat 8'
}
data['Sensor_Label'] = data['Sensor'].map(sensor_label)
cloud = st.slider("Cloud cover", 0, 60, 60)
st.markdown("Maximum cloud coverage %i percent" % cloud)
corresponding_data = data[data['Cloud'] <= cloud]
st.markdown(f"Number of images: {len(corresponding_data)}")
chart = alt.Chart(corresponding_data).mark_point(size=50, filled=True).encode(
    x=alt.X('Year:O', title='Year'),
    y=alt.Y('DOY:Q', title='Day of year'),
    color=alt.Color(
        'Sensor_Label:N',
        legend=alt.Legend(title="Satellite Type")
    ),
    tooltip=[
        alt.Tooltip('Year:O', title='Year'),
        alt.Tooltip('DOY:Q', title='Day of year'),
        alt.Tooltip('Sensor_Label:N', title='Satellite Type')
    ]
).properties(width=600, height=300)
st.altair_chart(chart, use_container_width=True)
if st.checkbox("Show corresponding data", False):
    st.subheader('Corresponding Data')
    st.write(corresponding_data)
st.markdown("<h2 style='text-align: center; font-size: 24px;'>2. Calendar heatmaps of LST</h2>", unsafe_allow_html=True)
# Dropdown menu for selecting LST type
lst_type = st.selectbox("Select LST Type:", ["Mean LST", "Minimum LST", "Maximum LST"])
if lst_type == "Mean LST":
    lst_column = "MeanLST"
    lst_title = "Mean LST (in °C)"
    max_domain = 45
elif lst_type == "Minimum LST":
    lst_column = "MinLST"
    lst_title = "Minimum LST (in °C)"
    max_domain = 37
else:
    lst_column = "MaxLST"
    lst_title = "Maximum LST (in °C)"
    max_domain = 66
chart = alt.Chart(data).mark_rect().encode(
    x='Year:O',
    y='Month:O',
    color=alt.Color(
        f'{lst_column}:Q',
        title=lst_title,
        scale=alt.Scale(scheme='viridis', domain=(20, max_domain))),
    tooltip=[
        alt.Tooltip('Year:O', title='Year'),
        alt.Tooltip('Month:O', title='Month'),
        alt.Tooltip(f'{lst_column}:Q', title=lst_title)
    ]).properties(width=600, height=300)
st.altair_chart(chart, use_container_width=True)
st.markdown("<h2 style='text-align: center; font-size: 24px;'>3. Trend of LST</h2>", unsafe_allow_html=True)
show_mean_lst = st.checkbox("Mean LST", value = True)
show_min_lst = st.checkbox("Minimum LST")
show_max_lst = st.checkbox("Maximum LST")
base = alt.Chart(data).encode(
    x=alt.X('Timestamp:T', title='Year'),
    tooltip=[
        alt.Tooltip('Timestamp:T', title='Year')
    ]
)
line_charts = []
if show_mean_lst:
    line_chart_mean = base.mark_line(color='red').encode(
        y=alt.Y('MeanLST:Q', scale=alt.Scale(domain=[20, 70]), title='LST in °C'),
        tooltip=alt.Tooltip('MeanLST:Q'),
        color=alt.value('red')
    )
    line_charts.append(line_chart_mean)
if show_min_lst:
    line_chart_min = base.mark_line(color='blue').encode(
        y=alt.Y('MinLST:Q', scale=alt.Scale(domain=[20, 70]), title='LST in °C'),
        tooltip=alt.Tooltip('MinLST:Q'),
        color=alt.value('blue')
    )
    line_charts.append(line_chart_min)
if show_max_lst:
    line_chart_max = base.mark_line(color='green').encode(
        y=alt.Y('MaxLST:Q', scale=alt.Scale(domain=[20, 70]), title='LST in °C'),
        tooltip=alt.Tooltip('MaxLST:Q'),
        color=alt.value('green')
    )
    line_charts.append(line_chart_max)
if line_charts:
    line_chart = alt.layer(*line_charts).properties(width=600, height=300).interactive()
    st.altair_chart(line_chart, use_container_width=True)
