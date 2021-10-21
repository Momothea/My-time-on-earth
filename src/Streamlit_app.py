#Importing the necessary library
import app1
import app2
import app3
import streamlit as st
import matplotlib.pyplot as plt

PAGES = {
    "Home": app1,
    "Map data": app2,
    "Youtube data":app3
}
link1 = '[GitHub](http://github.com)'
st.sidebar.markdown(link1, unsafe_allow_html=True)
link2 = "[LinkedIn](http://www.linkedin.com/in/moïse-iloo)"
st.sidebar.markdown(link2, unsafe_allow_html=True)
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()