import streamlit as st


def show_sidebar():

    st.sidebar.markdown(
        """
        <h2 style="text-align:center;">🌦️ Climate Visibility</h2>
        <p style="text-align:center;color:gray;">
        Intelligence Dashboard
        </p>
        <hr>
        """,
        unsafe_allow_html=True
    )

    pages = {
        "🏠 Home": "Home",
        "🔮 Prediction": "Prediction",
        "📊 Analytics": "Analytics",
        "📈 Model Comparison": "Model Comparison",
        "🧠 Explainability": "Explainability",
        "📥 Downloads": "Downloads",
        "ℹ️ About": "About",
    }

    for label, value in pages.items():

        if st.sidebar.button(label, use_container_width=True):
            st.session_state.page = value

    st.sidebar.markdown("---")

    st.sidebar.success("🌤 Good Visibility\n\nPowered by AI")