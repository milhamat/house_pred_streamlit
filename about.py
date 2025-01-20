import streamlit as st

st.set_page_config(
    page_title="Multi-Page Streamlit App",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Main Application")
st.write("Welcome to the main application! Use the sidebar to navigate to other pages.")
