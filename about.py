import streamlit as st

st.set_page_config(
    page_title="milhamat",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🏠"
)

st.title("About.")
# st.write("Welcome to the main application! Use the sidebar to navigate to other pages.")

col1, col2 = st.columns([1, 4])

with col1:
    st.image("artifacts/photo.png", width=200)

with col2:
    st.markdown(
    """
    Hai my name is Ilham 🖐😄. 
    
    I'm a Machine Learning Anthusiast, and this project is a part of my journey @Dibimbing Bootcamp.
    - You can check my profile on [LinkedIn](linkedin.com/in/milhamat)
    - You can check my full portofolion on [milhamat](https://milhamat.github.io/about.html)
    - You can check my github on [milhamat](https://github.com/milhamat)
    - You can check my [RESUME](https://drive.google.com/file/d/1ZMSHgpSi_Z0VIo1tpmJr0yxYU1vEqiTG/view?usp=sharing)
    """
    )
    