import streamlit as st
import pandas as pd
import pydeck as pdk
import math
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import model
import utils.data_scraper as ds

# Haversine formula to calculate distance in miles
def haversine(lat1, lon1, lat2, lon2):
    R = 3958.8  # Earth radius in miles
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c  # Distance in miles

# Function to get latitude and longitude from ZIP code using geopy
def get_lat_lon_from_zip(zip_code):
    geolocator = Nominatim(user_agent="college_finder")
    try:
        location = geolocator.geocode({"postalcode": zip_code, "country": "US"})
        if location:
            return {"Latitude": location.latitude, "Longitude": location.longitude}
    except GeocoderTimedOut:
        st.error("Geocoder service timed out. Please try again.")
    return None

def get_boston_colleges():
    return [
        {"Name": "Bunker Hill Community College", "Latitude": 42.3732, "Longitude": -71.0594, "Tuition": 10000},
        {"Name": "Roxbury Community College", "Latitude": 42.3317, "Longitude": -71.0955, "Tuition": 9000},
        {"Name": "MassBay Community College", "Latitude": 42.2964, "Longitude": -71.2924, "Tuition": 10500},
        {"Name": "Middlesex Community College", "Latitude": 42.6369, "Longitude": -71.3162, "Tuition": 9800},
        {"Name": "North Shore Community College", "Latitude": 42.5234, "Longitude": -70.9295, "Tuition": 9500},
        {"Name": "Quincy College", "Latitude": 42.2519, "Longitude": -71.0033, "Tuition": 11000},
        {"Name": "Northern Essex Community College", "Latitude": 42.7735, "Longitude": -71.1073, "Tuition": 9200},
        {"Name": "Bristol Community College", "Latitude": 41.7106, "Longitude": -71.1531, "Tuition": 8900},
        {"Name": "Springfield Technical Community College", "Latitude": 42.1056, "Longitude": -72.5913, "Tuition": 8800},
        {"Name": "Holyoke Community College", "Latitude": 42.2043, "Longitude": -72.6405, "Tuition": 9200}
    ]


def college_search_page():
    st.title("College Search")
    
    # User input for search criteria
    st.subheader("Enter Search Criteria")
    area_of_interest = st.text_input("Area of Interest", st.session_state.get("area_of_interest", ""))
    gender = st.selectbox("Gender", options=["Any", "Male", "Female", "Other"], index=["Any", "Male", "Female", "Other"].index(st.session_state.get("gender", "Any")))
    state = st.text_input("Enter State", st.session_state.get("state", ""))
    city = st.text_input("Enter City", st.session_state.get("city", ""))
    zip_code = st.text_input("Enter ZIP Code")
    
    if st.button("Search"):
        # Store user input in session state
        st.session_state.area_of_interest = area_of_interest
        st.session_state.gender = gender
        st.session_state.state = state
        st.session_state.city = city
        
        # Default to Boston if no ZIP is entered
        if zip_code:
            user_location = get_lat_lon_from_zip(zip_code)
            if not user_location:
                st.warning("Could not find location for this ZIP code. Using Boston as default.")
                user_location = {"Latitude": 42.3601, "Longitude": -71.0589}
        else:
            user_location = {"Latitude": 42.3601, "Longitude": -71.0589}  # Boston Default

        current_location = {"Latitude": user_location["Latitude"], "Longitude": user_location["Longitude"], "Name": "Your Location"}
        
        # Invoke model search
        query = f"{area_of_interest} {user_location['Latitude']},{user_location['Longitude']} {city},{state}"
        query_result_output = model.invokeSearch(query)
        print(query_result_output.content)
        # results = ds.extract_college_info_as_json(query_result_output)
        # print(results)

        # Store results persistently in session state
        st.session_state.results = get_boston_colleges()  
        st.session_state.current_location = current_location  # Store user's selected location

    # Display search results
    if "results" in st.session_state:
        display_results(st.session_state.results, st.session_state.current_location)

def display_results(results, current_location):
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.subheader("Search Results")
        for college in results:
            with st.expander(college["Name"]):
                # st.write(f"**Distance:** {college['Distance']:.2f} miles")
                st.write(f"**Tuition Cost:** ${college['Tuition']}")

    with col2:
        st.subheader("College Locations")
        
        map_data = pd.DataFrame(results)
        current_location_df = pd.DataFrame([current_location])

        layer_colleges = pdk.Layer(
            "ScatterplotLayer",
            data=map_data,
            get_position="[Longitude, Latitude]",
            get_color="[255, 0, 0, 160]",  # Red for colleges
            get_radius=200,
            pickable=True,
        )
        
        layer_current = pdk.Layer(
            "ScatterplotLayer",
            data=current_location_df,
            get_position="[Longitude, Latitude]",
            get_color="[0, 0, 255, 200]",  # Blue for user's location
            get_radius=250,
            pickable=True,
        )
        
        view_state = pdk.ViewState(
            latitude=current_location["Latitude"], 
            longitude=current_location["Longitude"], 
            zoom=10, pitch=0
        )
        
        r = pdk.Deck(
            layers=[layer_colleges, layer_current], 
            initial_view_state=view_state, 
            tooltip={"text": "{Name}"},
            map_style='light'
        )
        
        st.pydeck_chart(r)

if __name__ == "__main__":
    college_search_page()
