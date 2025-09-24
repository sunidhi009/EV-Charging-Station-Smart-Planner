import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
from math import radians, sin, cos, sqrt, atan2
import plotly.express as px
from io import BytesIO

# Page configuration
st.set_page_config(page_title="EV Charging Planner", layout="wide")
st.title("🔌 EV Charging Station Smart Planner")
st.markdown("🚗 **Plan smart. Charge smarter.** Upload your Excel file to identify the best EV charging locations.")

# Upload Excel file
file = st.file_uploader("📁 Upload Excel File", type=["xlsx"])

if file:
    df = pd.read_excel(file)
    st.success("✅ File uploaded successfully!")
    st.subheader("📊 Uploaded Data")
    st.dataframe(df)

    # Compute distance between two coordinates using Haversine formula
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c

    # Compute average distance of each location from all others
    avg_distances = []
    for i in range(len(df)):
        lat1, lon1 = df.loc[i, 'Latitude'], df.loc[i, 'Longitude']
        total_dist = 0
        for j in range(len(df)):
            if i != j:
                lat2, lon2 = df.loc[j, 'Latitude'], df.loc[j, 'Longitude']
                total_dist += haversine(lat1, lon1, lat2, lon2)
        avg_distances.append(total_dist / (len(df) - 1))
    df['Avg_Distance'] = avg_distances

    # Normalize columns
    def normalize(col):
        return df[col] / df[col].max()

    df['Area_Norm'] = normalize('Area')
    df['Vehicles_Norm'] = normalize('Vehicles')
    df['Footfall_Norm'] = normalize('Footfall')
    df['Distance_Norm'] = normalize('Avg_Distance')

    # Show metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("📍 Total Locations", len(df))
    col2.metric("🚗 Avg Vehicles", int(df['Vehicles'].mean()))
    col3.metric("👣 Avg Footfall", int(df['Footfall'].mean()))

    # Sidebar: weight preferences for scoring
    st.sidebar.header("⚙️ Set Preferences")
    w_area = st.sidebar.slider("Weight: Area", 0.0, 1.0, 0.2)
    w_veh = st.sidebar.slider("Weight: Vehicles", 0.0, 1.0, 0.2)
    w_foot = st.sidebar.slider("Weight: Footfall", 0.0, 1.0, 0.25)
    w_dist = st.sidebar.slider("Weight: Distance", 0.0, 1.0, 0.35)

    # Compute overall score
    df['Score'] = (w_area * df['Area_Norm'] +
                   w_veh * df['Vehicles_Norm'] +
                   w_foot * df['Footfall_Norm'] +
                   w_dist * df['Distance_Norm'])

    # Select top N locations
    top_n = st.sidebar.slider("🔝 Number of Top Locations", 1, len(df), 5)
    top_locations = df.sort_values(by='Score', ascending=False).head(top_n)

    # Display top locations
    st.subheader("🏆 Top Suggested Locations")
    st.write(top_locations[['Location', 'Score']])

    # Visualize scores
    st.subheader("📈 Score Comparison Chart")
    fig = px.bar(top_locations, x='Location', y='Score', color='Score', text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

    # Map visualization
    st.subheader("🗺️ Top Locations on Map")
    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=5)
    for _, row in top_locations.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['Location']}\nScore: {row['Score']:.2f}",
            icon=folium.Icon(color='green', icon='bolt', prefix='fa')
        ).add_to(m)
    st_folium(m, width=1000, height=600)

    # Download top locations
    st.subheader("📥 Download Top Locations")
    buffer = BytesIO()
    top_locations.to_excel(buffer, index=False)
    st.download_button("Download as Excel", data=buffer.getvalue(), file_name="top_locations.xlsx")
else:
    st.info("👆 Please upload an Excel file to start planning your EV stations.")
