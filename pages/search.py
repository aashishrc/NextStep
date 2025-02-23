# import streamlit as st
# import pandas as pd

# # College data
# data = [
#     {"Name": "Harvard University", "Latitude": 42.3732, "Longitude": -71.119, "Tuition": "$57,261", "location": "Cambridge, MA"},
#     {"Name": "University of Massachusetts-Amherst", "Latitude": 42.3732, "Longitude": -72.5199, "Tuition": "$16,952", "location": "Amherst, MA"},
#     {"Name": "University of Massachusetts-Boston", "Latitude": 42.3154, "Longitude": -71.0361, "Tuition": "$15,132", "location": "Boston, MA"},
#     {"Name": "Western New England University", "Latitude": 42.3732, "Longitude": -71.0594, "Tuition": "$44,500", "location": "Springfield, MA"}
# ]

# df = pd.DataFrame(data)

# st.title("Top Colleges for Mathematics in Massachusetts")

# selected = st.dataframe(df, use_container_width=True)

# if st.button("View Details"):
#     for college in data:
#         if college["Name"] == selected:
#             st.subheader(college["Name"])
#             st.write(f"**Location:** {college['location']}")
#             st.write(f"**Website:** {college['Name'].split()[0].lower()}.edu")
#             st.write(f"**Tuition:** {college['Tuition']}")
#             st.write(f"**Acceptance Rate:** {college.get('acceptance_rate', 'N/A')}")
#             st.write(f"**Mathematics Program Quality:** {college.get('program_quality', 'N/A')}")
#             break
