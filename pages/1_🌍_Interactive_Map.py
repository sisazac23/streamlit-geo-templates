import streamlit as st
import leafmap.foliumap as leafmap



st.title("Interactive Map")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:
    basemap = st.selectbox("Select a basemap:", options, index)

with col1:
    m = leafmap.Map(location=[6.249999, -75.5999976],locate_control=True, latlon_control=True, draw_export=True, minimap_control=True,zoom_start=12)
    m.add_basemap(basemap)
    #m.set_center(6.249999, -75.5999976, 11)  # Set the center to the Aburrá Valley
    # Add a rectangle to focus on the Aburrá Valley
    #bounds = [[6.0, -75.9], [6.4, -75.2]]
    #m.add_rectangle(bounds, color="red", fill_opacity=0.1)
    m.to_streamlit(height=700)
