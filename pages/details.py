import streamlit as st
import pandas as pd
import altair as alt

# Optional: If you have shared database logic in a separate file, e.g. utils/db_queries.py
# from utils.db_queries import get_college_details_from_db

def get_college_details_from_db(college_id):
    """
    Placeholder function to simulate retrieving data from a database.
    Replace this with your real DB logic or function calls.
    """
    # Dummy example data for demonstration purposes
    dummy_data = {
        "college_name": "NextStep University",
        "location": "Boston, MA",
        "programs_offered": [
            {"name": "Computer Science", "avg_salary": 80000},
            {"name": "Business Administration", "avg_salary": 60000},
            {"name": "Nursing", "avg_salary": 65000}
        ],
        "financial_aid": "Available scholarships and grants for eligible students.",
        "description": (
            "NextStep University is a renowned institution known for its "
            "cutting-edge curriculum, diverse student body, and strong "
            "industry partnerships."
        ),
    }
    # In a real scenario, you'd query your database:
    # result = execute_sql_query("SELECT * FROM colleges WHERE id = %s", (college_id,))
    # return result
    return dummy_data

def show_details(college_id=None):
    """
    Renders a detailed view for a single college.
    `college_id` can be passed via query params, session state, or function arguments.
    """
    # If you do not have an ID yet, handle gracefully
    if college_id is None:
        st.error("No college ID provided.")
        return

    # 1. Fetch data from database
    college_data = get_college_details_from_db(college_id)

    # 2. Page Title / Header
    st.title(f"College Details: {college_data['college_name']}")
    st.write(f"**Location:** {college_data['location']}")

    st.write("---")

    # 3. Description or Overview
    st.subheader("Overview")
    st.write(college_data["description"])

    # 4. Financial Aid
    st.subheader("Financial Aid")
    st.write(college_data["financial_aid"])

    # 5. Programs Table / Chart
    st.subheader("Available Programs & Average Salary")
    programs = pd.DataFrame(college_data["programs_offered"])
    st.dataframe(programs)  # Renders a quick interactive table

    # Optional: Show a bar chart of average salaries per program
    bar_chart = alt.Chart(programs).mark_bar().encode(
        x=alt.X("name", sort=None, title="Program"),
        y=alt.Y("avg_salary", title="Average Salary (USD)"),
        tooltip=["name", "avg_salary"]
    )
    st.altair_chart(bar_chart, use_container_width=True)

    # 6. Apply / More Info Section
    st.subheader("Next Steps")
    st.markdown("""
    - **Apply**: [Click here](#) to apply or visit the official college website.
    - **Contact Admissions**: admissions@nextstep.edu
    """)

    # 7. Back / Navigation
    if st.button("Back to Results"):
        st.session_state["page"] = "results"

    st.write("---")
    st.info("Adjust the layout, charts, or style as needed for your data and branding.")

if __name__ == "__main__":
    show_details()