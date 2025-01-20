import streamlit as st
from Home import app as home_app
from Page1 import app as page1_app
from Page2 import app as page2_app

# Dictionary to hold pages
pages = {
    "Home": home_app,
    "Page 1": page1_app,
    "Page 2": page2_app
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Render the selected page
if selection in pages:
    pages[selection]()
