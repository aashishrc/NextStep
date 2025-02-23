import streamlit as st
import altair as alt
import pandas as pd
import pages.results as college_search_page

def show_landing():
    st.title("Welcome to NextStep!")
    st.subheader("A simple way to explore schools and opportunities based on your preferences")

    # Main description or introduction
    st.markdown(
        """
        This application helps you:
        - Find colleges based on your preferences
        - Explore scholarships and financial aid
        - Get insights into average pay after completing various programs
        - Much more...
        """
    )

    # Add some statistics (static example)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Colleges", "250+")
    with col2:
        st.metric("Scholarships", "80+")
    with col3:
        st.metric("Average Salary (Graduates)", "$45,000")

    st.write("---")

    st.title("Education & Career Insights")

    # ------------------------------------------------------
    # 1. Text Highlights / Infographics
    # ------------------------------------------------------
    st.subheader("Why a Degree Matters")
    st.markdown(
        """
        - **Higher Earning Potential**: On average, bachelor’s degree holders earn 40% more over a lifetime than high school graduates.
        - **Better Job Security**: College graduates have significantly lower unemployment rates.
        - **Career Growth**: Many emerging fields (e.g., technology, healthcare) prefer or require a college degree.
        """
    )

    st.info(
        "“Education is the most powerful weapon which you can use to change the world.” \n— Nelson Mandela"
    )

    # ------------------------------------------------------
    # 2. Employment Rate: With vs. Without Degrees (Bar Chart)
    # ------------------------------------------------------
    st.subheader("Employment Rate Differences")

    employment_data = pd.DataFrame({
        "Category": ["With Degree", "Without Degree"],
        "Employment Rate (%)": [85, 70]
    })

    employment_bar = alt.Chart(employment_data).mark_bar().encode(
        x=alt.X("Category", sort=None),
        y=alt.Y("Employment Rate (%)", title="Employment Rate (%)"),
        tooltip=["Category", "Employment Rate (%)"]
    ).properties(width='container', height=300)

    st.altair_chart(employment_bar, use_container_width=True)

    # ------------------------------------------------------
    # 3. Projected Job Growth by Field (Bar Chart)
    # ------------------------------------------------------
    st.subheader("Projected Job Growth in Fields Requiring Higher Education")

    growth_data = pd.DataFrame({
        "Field": ["Technology", "Healthcare", "Finance", "Engineering", "Education"],
        "Projected Growth (%)": [15, 20, 10, 18, 12]  # dummy data
    })

    growth_bar = alt.Chart(growth_data).mark_bar().encode(
        x=alt.X("Field", sort=None),
        y=alt.Y("Projected Growth (%)", title="Growth Rate (%)"),
        tooltip=["Field", "Projected Growth (%)"]
    ).properties(width='container', height=300)

    st.altair_chart(growth_bar, use_container_width=True)

    # ------------------------------------------------------
    # 4. Distribution of Popular Majors (Pie Chart)
    # ------------------------------------------------------
    st.subheader("Distribution of Popular Majors")

    major_data = pd.DataFrame({
        "Major": ["Engineering", "Business", "Healthcare", "Arts", "Computer Science"],
        "Students": [300, 400, 250, 150, 350]  # dummy data
    })

    # Altair donut chart
    majors_pie = alt.Chart(major_data).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="Students", type="quantitative"),
        color=alt.Color(field="Major", type="nominal", legend=None),
        tooltip=["Major", "Students"]
    )

    st.altair_chart(majors_pie, use_container_width=True)

    # ------------------------------------------------------
    # 5. Breakdown of Employment Sectors Preferring Degree (Pie Chart)
    # ------------------------------------------------------
    st.subheader("Employment Sectors Favoring College-Educated Applicants")

    sector_data = pd.DataFrame({
        "Sector": ["Technology", "Healthcare", "Finance", "Manufacturing", "Government"],
        "Preference (%)": [85, 80, 75, 60, 70]  # dummy data
    })

    sector_pie = alt.Chart(sector_data).mark_arc(innerRadius=0).encode(
        theta=alt.Theta(field="Preference (%)", type="quantitative"),
        color=alt.Color(field="Sector", type="nominal", legend=None),
        tooltip=["Sector", "Preference (%)"]
    )

    st.altair_chart(sector_pie, use_container_width=True)

    # ------------------------------------------------------
    # 6. Salary Comparisons by Degree Level (Bar Chart)
    # ------------------------------------------------------
    st.subheader("Salary Comparisons Based on Degree Level")

    salary_data = pd.DataFrame({
        "Degree Level": [
            "High School Diploma", "Associate’s", "Bachelor’s", "Master’s", "Doctorate"
        ],
        "Average Salary ($)": [35000, 42000, 60000, 70000, 90000]
    })

    salary_bar = alt.Chart(salary_data).mark_bar().encode(
        x=alt.X("Degree Level", sort=None),
        y=alt.Y("Average Salary ($)", title="Average Salary (USD)"),
        tooltip=["Degree Level", "Average Salary ($)"]
    ).properties(width='container', height=300)

    st.altair_chart(salary_bar, use_container_width=True)

    # ------------------------------------------------------
    # 7. Unemployment Rate by Education Level (Bar Chart)
    # ------------------------------------------------------
    st.subheader("Unemployment Rate by Education Level")

    unemployment_data = pd.DataFrame({
        "Education Level": [
            "Less Than High School", "High School Graduate", "Associate’s",
            "Bachelor’s", "Master’s"
        ],
        "Unemployment Rate (%)": [8, 6, 4.5, 3.2, 2.5]  # dummy data
    })

    unemployment_bar = alt.Chart(unemployment_data).mark_bar().encode(
        x=alt.X("Education Level", sort=None),
        y=alt.Y("Unemployment Rate (%)", title="Unemployment Rate (%)"),
        tooltip=["Education Level", "Unemployment Rate (%)"]
    ).properties(width='container', height=300)

    st.altair_chart(unemployment_bar, use_container_width=True)

    # ------------------------------------------------------
    # 8. Growth in Scholarships & Enrollment Over Time (Line Chart)
    # ------------------------------------------------------
    st.subheader("Growth in Scholarship Availability & Student Enrollment Over Time")

    # Example multi-series data for line chart
    timeline_data = pd.DataFrame({
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Scholarships Available": [600, 650, 700, 800, 1000],
        "Enrollment (thousands)": [200, 210, 230, 250, 280]
    })

    # Melt the data to have a single 'Metric' column for easier plotting
    timeline_melted = timeline_data.melt("Year", var_name="Metric", value_name="Value")

    line_chart = alt.Chart(timeline_melted).mark_line(point=True).encode(
        x=alt.X("Year:O", axis=alt.Axis(labelAngle=0)),  # treat Year as ordinal
        y="Value:Q",
        color="Metric:N",
        tooltip=["Year:O", "Metric:N", "Value:Q"]
    ).properties(width='container', height=400)

    st.altair_chart(line_chart, use_container_width=True)
    
    # Simple 'Get Started' button
    st.write("Ready to explore schools?")
    
    if st.button("Go to Search Page"):
        st.switch_page("pages/results.py")
