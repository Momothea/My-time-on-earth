#Importing the necessary library
import streamlit as st
import pandas as pd
import pydeck as pdk
import reverse_geocoder as rg
import matplotlib.pyplot as plt


def main():
    
    app()


# This is the main app app itself, which appears when the user selects "Run the app".
def app(): 
    # Importing the files
    path1 = "C:/Users/Moise/Documents/Data visualization/My time on earth/Data/map_data.csv"

    # Creating the DataFrames
    df1 = pd.read_csv(path1)

    st.title("My activity on land")

    # Controls How the data is displayed
    def display_preference(df):
        st.sidebar.title('Map Data')
        choice1 = st.sidebar.selectbox("Choose a year", [2017, 2018])
        df = df.loc[df['year'] == choice1]
        choice2 = st.sidebar.selectbox("Choose a month", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        if(choice2):
            df = df.loc[df['month'] == choice2]
        
        if((choice1 == 2017) and (choice2 < 10)):
            st.error("The Map data starts in October of 2017")
        else:
            display_3D_Map(df, choice2)
            display_hist(df)
            select_date(df)
            trajet(df)
        
    # Display a 3D map for a given date
    def display_3D_Map(df, month):
        st.title(f"3D map in {current_month(month)}")
        st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude= 48.85,#default lon and lat
         longitude= 2.34,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=df,
            get_position='[longitude, latitude]',
            radius=200,
            elevation_scale=10,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=df,
             get_position='[longitude, latitude]',
             get_color='[200, 30, 0, 160]',
             get_radius=200,
         ),
     ],
 ))

    # Display an histogram
    def display_hist(df):
        fig, ax = plt.subplots()
        ax.hist(df['day'], bins= 30, rwidth= 0.7)
        plt.xlabel('Days of the month')
        plt.ylabel('Frequency of position')
        st.pyplot(fig)
        
    # Display a position for a certain date IIII I could use/modify this function to plot mes trajets
    def select_date(df):
        st.title("My location at a precise time.")
        my_datetime = st.select_slider("Choose a time",df['time'])
        df = df.loc[df['time'] == my_datetime]
        #print(df['time'])
        for a, b in zip(df['latitude'], df['longitude']):
            #print(a, b)
            place = reverseGeocode((a, b))
            st.title(place)
            map = pd.DataFrame(
            np.array([[a,b]]),
            columns=['lat', 'lon'])
            boulder_coords = [a, b]
            my_map = folium.Map(location = boulder_coords, zoom_start = 13)
            my_map
            st.map(map)
            break
    def trajet(df):
        st.title("My timeline.")
        my_datetime1 = st.select_slider("Choose a starting time",df['time'])
        my_datetime2 = st.select_slider("Choose an ending time",df['time'])
        df = df.loc[(df['time'] > my_datetime1) & (df['time'] < my_datetime2)]
        lon = []
        lat = []
        for a, b in zip(df['latitude'], df['longitude']):
            lat.append(a)
            lon.append(b)
        dic = { 'lat':lat, 'lon':lon}
        timeline = pd.DataFrame(dic)
        st.map(timeline)

        

    # Find a location from the coordinates    
    def reverseGeocode(coordinates):
        result = rg.search(coordinates)
        # result is a list containing ordered dictionary.
        return (result[0]['name'])    

    # This should allow me to display a month, but it doesn' work
    def current_month(month):
        if(month == 1):
            return 'January'
        elif(month == 2):
            return 'February'
        elif(month == 3):
            return 'March'
        elif(month == 4):
            return 'April'
        elif(month == 5):
            return 'May'
        elif(month == 6):
            return 'Jun'
        elif(month == 7):
            return 'July'
        elif(month == 8):
            return 'August'
        elif(month == 9):
            return 'September'
        elif(month == 10):
            return 'October'
        elif(month == 11):
            return 'November'
        elif(month == 12):
            return 'December'
        

    display_preference(df1)
    

if __name__ == "__main__":
    main()