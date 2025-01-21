import streamlit as st

st.set_page_config(
    page_title="milhamat",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🏠"
)

st.title("🏠 About")
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
    - You can download my [RESUME](https://drive.google.com/file/d/1ZMSHgpSi_Z0VIo1tpmJr0yxYU1vEqiTG/view?usp=sharing)
    """
    )
    
st.header("Project Background")
st.markdown(
    """
    This project is a part of my journey @Dibimbing Bootcamp. 
    The main goal of this project is to predict the price of a house based on several features.
    And use streamlit as a platform to deploy the model and presenting the data analytics, preprocessing and model prediction.
    """
)

st.header("Author Background")
st.markdown(
    """
    Ilham is a passionate Machine Learning enthusiast dedicated to harnessing the power of data to build intelligent solutions. 
    Their expertise includes developing predictive models, optimizing algorithms, and applying deep learning techniques to address real-world challenges. 
    With a knack for transforming complex data into actionable insights, they are committed to exploring cutting-edge AI technologies to drive innovation. 
    Focused on solving problems through automation and intelligent systems, Ilham aims to make a meaningful impact across diverse industries.
    """
)

st.header("Mini Projects Showcase")
st.markdown(
    """
    1. **Campus Data Dashboard App** - May 2024
        (National Taipei University of Business)
        - Built a web data dashboard for National Taipei University of Business student alumni using Dash (Python).
        - Setting the server and deploy the website on campus server.
        - Design the User Interface of the Website
    
    Project Url: [here](https://isdc-ntub-dashboard.onrender.com/)
    
    2. **Machine Learning Tools** - March 2024
        (Personal Projects)
        - Build web app for exploratory data visualization using R and Shiny.
        - Build an regresion and Classification model within the web app.
        - Deploy the web app using shinyapps.io. 
    
    Project Url: [here](https://milhamat.shinyapps.io/ML_module/)
    
    3. **Enhancing Data Through Augmentation to Address Few-class Scenarios of Few-shot Learning** - December 2023
        (Project article-National Taipei University of Business)
        - Developing Image Enhancement Technique for class augmentation using CLAHE and binary inverse thresholding.
        - Developing Class enrichment using Mathematic Combination function.
        - Increase the model accuracy by 22%.
    
    4. **Steel Surface Defect Classification using Few-Shot Learning** - June 2023
        (Master Thesis-Ming Chi University of Technology)
        - Developing few shot learning models (Siamese, matching, prototypical network) for NEU (steel surface defect) image dataset.
        - Combined k-means clustering to add more class based on the similarity of the images.
        - Based on this combination the model improve 17% of accuracy.
    """
)

st.subheader("More Projects Available on: [here](https://milhamat.github.io/portfolio.html)")