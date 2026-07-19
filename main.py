import streamlit as st
from components.sidebar import show_sidebar
from pages import (
    home,
    prediction,
    analytics,
    model_comparison,
    explainability,
    downloads,
    about,
)

# -----------------------------------------
# Page Configuration
# -----------------------------------------

st.set_page_config(
    page_title="Climate Visibility Intelligence",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown("""
<style>

/* Hide default Streamlit multipage navigation */
[data-testid="stSidebarNav"] {
    display: none;
}

/* Hide the separator above the navigation */
[data-testid="stSidebarNavSeparator"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------------------
# Session State
# -----------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

show_sidebar()
# -----------------------------------------
# Display Selected Page
# -----------------------------------------

page = st.session_state.page

if page == "Home":
    home.show()

elif page == "Prediction":
    prediction.show()

elif page == "Analytics":
    analytics.show()

elif page == "Model Comparison":
    model_comparison.show()

elif page == "Explainability":
    explainability.show()

elif page == "Downloads":
    downloads.show()

elif page == "About":
    about.show()