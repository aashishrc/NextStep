# streamlit_app.py
import streamlit as st
import pages.landing as landing_page
import pages.search as search_page
import pages.results as results_page
import pages.details as details_page
import model


# Configure the page (optional)
st.set_page_config(
    page_title="My School Suggestion App",
    page_icon="🎓",
    layout="centered"
)

def main():
    # Ensure a default page is set
    if "page" not in st.session_state:
        st.session_state["page"] = "landing"

    # Route to the correct page
    if st.session_state["page"] == "landing":
        landing_page.show_landing()
    elif st.session_state["page"] == "search":
        search_page.show_search()
    elif st.session_state["page"] == "details":
        details_page.show_details()
    else:
        # fallback or default
        landing_page.show_landing()

if __name__ == "__main__":
    main()