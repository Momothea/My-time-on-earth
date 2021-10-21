import streamlit as st
import pandas as pd


def main():
    app()

def app(): 
    path1 = "C:/Users/Moise/Documents/Data visualization/My time on earth/Data/map_data.csv"
    path2 = "C:/Users/Moise/Documents/Data visualization/My time on earth/Data/youtube.csv"
    df1 = pd.DataFrame(pd.read_csv(path1))
    df2 = pd.DataFrame(pd.read_csv(path2))
    st.title("Moïse Iloo Liandja")
    st.title("🌍 My time on earth and on Youtube:")
    st.title("A data visualization project")
    st.title("Here are my datasets")
    st.title("My Map Data")
    st.dataframe(df1)
    st.title("My Youtube Data")
    st.dataframe(df2)

if __name__ == "__main__":
    main()