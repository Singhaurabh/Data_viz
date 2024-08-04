import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


data = pd.read_csv(r"C:\Users\SAURABH SINGH\Desktop\India-data-viz-mini-project\india_csv")

list_of_states = list(data['State name'].unique())
list_of_states.insert(0,'Overall India')

st.set_page_config(layout = 'wide')
st.sidebar.title("India's Data Vizualisation")

selected_state = st.sidebar.selectbox('select a state',list_of_states)
pirmary_parameter = st.sidebar.selectbox('select primary parameter',sorted(data.columns[5:]))
secondary_parameter = st.sidebar.selectbox('select secondary parameter',sorted(data.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents the primary parameter')
    st.text('Color represents the secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(data, lat="Latitude", lon="Longitude", zoom=3,size = pirmary_parameter,color = secondary_parameter,size_max =40,
                                mapbox_style="carto-positron", width=3000,height= 800,hover_name = 'District')
        st.plotly_chart(fig,use_container_width = True)
    else:
        state_data = data[data['State name'] == selected_state]

        fig = px.scatter_mapbox(state_data, lat="Latitude", lon="Longitude", zoom=3, size=pirmary_parameter,
                                color=secondary_parameter, size_max=40,
                                mapbox_style="carto-positron", width=3000, height=800,hover_name = 'District')
        st.plotly_chart(fig, use_container_width=True)
