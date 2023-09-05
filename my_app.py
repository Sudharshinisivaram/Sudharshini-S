import streamlit as st
import folium
from streamlit_folium import folium_static  # Add this import
import geopy.distance
from streamlit_folium import folium_static


# Function to calculate distance between two points (latitude, longitude)
def calculate_distance(coord1, coord2):
    return geopy.distance.distance(coord1, coord2).m

# Create a Streamlit app
st.title("Vehicle Tracking System")

# Input fields for latitude and longitude
latitude = st.number_input("Enter Latitude:")
longitude = st.number_input("Enter Longitude:")

# Create a map centered on the entered coordinates
m = folium.Map(location=[latitude, longitude], zoom_start=15)

# Add a marker for the entered coordinates
folium.Marker([latitude, longitude]).add_to(m)

# Circle center coordinates and radius (in meters)
circle_center = (40.7128, -74.0060)  # Replace with your desired latitude and longitude values
circle_radius = 1000  # Replace with your desired radius in meters

# Calculate the distance between the entered coordinates and the circle center
distance = calculate_distance((latitude, longitude), circle_center)

# Check if the entered coordinates are within the circle
if distance <= circle_radius:
    st.success("Entered coordinates are inside the circle.")
else:
    st.warning("Entered coordinates are outside the circle.")

# Display the map
folium_static(m)

