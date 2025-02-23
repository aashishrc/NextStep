# 🎓 NextStep

Empowering learners from all walks of life to discover, aspire, and achieve their educational goals.  
This application helps users explore schools and opportunities, providing insights into colleges, scholarships, financial aid, and more.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://next-step.streamlit.app/)

---

## Inspiration
Many students—especially those unaware of higher education’s impact—miss out on crucial opportunities. Our team wanted to address this gap by creating a platform that highlights the **value of higher education**, provides **customized college recommendations**, and helps students see a clearer path to a brighter future.

> “Education is the most powerful weapon which you can use to change the world.” — Nelson Mandela  

### Why Education Matters
- **Higher Earning Potential**: Bachelor’s degree holders can earn up to 40% more over a lifetime than high school graduates.  
- **Better Job Security**: College graduates have significantly lower unemployment rates.  
- **Career Growth**: Many emerging fields (e.g., technology, healthcare) require or strongly prefer a college degree.  
- **Improved Quality of Life**: Educated individuals often experience better health, increased civic participation, and greater life satisfaction.

---

## What It Does
- **Personalized School & Program Recommendations**: Users input their interests and location preferences, and NextStep suggests relevant colleges.  
- **Scholarships & Financial Aid**: Provides awareness of aid options that can make higher education more accessible.  
- **Interactive Maps**: Visualize nearby colleges based on user-selected filters.  
- **Insights & Statistics**: Offers data-driven charts, salaries, and growth projections to illustrate the benefits of higher education.

---

## How We Built It
1. **Front-end**: Implemented with [Streamlit](https://docs.streamlit.io/), ensuring an intuitive, interactive interface.
2. **Data & Modeling**:  
   - A simple RAG (Retrieval-Augmented Generation) approach to personalize recommendations.  
   - Databases/CSV datasets for scholarships and college information.  
3. **Location Services**: [Geopy](https://geopy.readthedocs.io/) for distance calculations and mapping coordinates.  
4. **Deployment**: Hosted via Streamlit Cloud for easy access and sharing.

---

## Challenges We Ran Into
- **Data Quality & Availability**: Finding up-to-date, complete scholarship and college datasets was tricky.  
- **User Experience**: Ensuring a minimal learning curve for non-tech-savvy users required iterative design improvements.  
- **Scalability**: Balancing performance with the complexity of location-based filtering and dynamic data retrieval.

---

## Accomplishments That We're Proud Of
- **Comprehensive MVP**: We delivered a working prototype that covers the full journey—search, results, and details.  
- **User-Centric Design**: Simple navigation, readable charts, and clear calls to action for next steps.  
- **Team Collaboration**: Efficiently split tasks across data, frontend, and design, merging them into a coherent product.

---

## What We Learned
- **RAG Model Integration**: Experimenting with retrieval-augmented generation to improve recommendation accuracy.  
- **UI/UX Considerations**: Designing for clarity and inclusivity, especially for users who may be new to digital tools.  
- **Project Management**: Iterative sprint planning, version control, and regular syncs kept us on track.

---

## What's Next for NextStep
- **More Data Sources**: Integrate additional scholarship providers and college partnerships.  
- **Mentorship & Community**: Add forums or mentorship channels to connect students with current undergraduates and professionals.  
- **Mobile App**: Enhance accessibility through a lightweight mobile version.  
- **In-depth Financial Guidance**: Tools to compare tuition, ROI, and personalized financial planning.

---

## Project Structure

```plaintext
NextStep/
└── my_streamlit_app/
    ├── .devcontainer/
    │   └── devcontainer.json
    ├── .streamlit/
    │   └── config.toml
    ├── pages/
    │   ├── landing.py
    │   ├── search.py
    │   ├── results.py
    │   └── details.py
    ├── utils/
    │   └── model.py
    ├── README.md
    ├── streamlit_app.py
    └── requirements.txt


## Further Reading

- [US Department of Education Dataset](https://collegescorecard.ed.gov/data/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Geopy Documentation](https://geopy.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Pydeck Documentation](https://deckgl.readthedocs.io/en/latest/)
