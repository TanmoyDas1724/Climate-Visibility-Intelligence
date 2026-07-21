import streamlit as st


def show_footer():
    st.divider()

    st.markdown(
    """
    <div style="
        text-align:center;
        padding:10px;
        color:inherit;
    ">
        🌦️ <b>Climate Visibility Intelligence Dashboard</b><br>
        Built using Streamlit, Scikit-learn, XGBoost & SHAP
    </div>
    """,
    unsafe_allow_html=True,
)