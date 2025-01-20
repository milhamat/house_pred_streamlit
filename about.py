import streamlit as st

st.set_page_config(
    page_title="milhamat",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("About.")
# st.write("Welcome to the main application! Use the sidebar to navigate to other pages.")

col1, col2 = st.columns([1, 4])

with col1:
    st.image("artifacts/photo.png", width=200)

with col2:
    st.write("Hai my name is Ilham. I'm an Machine Learning Anthusiast, and this project is a part of my journey @Dibimbing Bootcamp.")
    st.write("You can check my profile on [LinkedIn](linkedin.com/in/milhamat)")
    st.write("You can check my full portofolion on [milhamat](https://milhamat.github.io/about.html)")