#Importing the necessary library
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def main():
    
    app()

def app(): 
    # Importing the files
    path1 = "C:/Users/Moise/Documents/Data visualization/My time on earth/Data/youtube.csv"

    # Creating the DataFrames
    df1 = pd.read_csv(path1)

    # Controls How the data is displayed
    def display_preference(df):
                st.sidebar.title('Youtube Data')
                choice1 = st.sidebar.selectbox("Choose a year", [2018, 2019, 2020, 2021])
                compareYear(choice1, df)
                df = df.loc[df['year'] == choice1]
                year = Number('year',df)
                st.title(f'In {choice1} ')
                st.write(f"I have watched {year[choice1]} videos in {choice1}")
                histo(df, 'month')
                line_chart(df, 'month')
                st.title('What kind of videos do I watch')
                st.write("Let us see")
                pie_chart(df, 'genre')
                st.write("If we just take the channels I am subscribed to:")
                pie_chartS(df, 'genre')
                choice2 = st.sidebar.selectbox("Choose a month",[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
                if(choice2):
                    #if(choice2 > 8):
                        #compareMonth(choice2, df)
                    df = df.loc[df['month'] == choice2]
                    month = Number('month', df)
                    if((choice2 < 7) and (choice1 == 2018)):
                        st.error("the video data starts in July of 2018")  
                    elif((choice2 >= 10) and (choice1 == 2021)):
                        st.error("the video data ends in september of 2021")
                    else:
                        st.title(f'In {current_month(choice2)}  {choice1} ')
                        st.write(f"I have watched {month[choice2]} videos in {current_month(choice2)} {choice1}")
                        histo(df, 'day')
                        line_chart(df, 'day')
                        st.title(f'What kind of videos did I watch this month.')
                        st.write("Let us see.")
                        pie_chart(df, 'genre')
                        st.write("If we just take the channels I am subscribed to:")
                        pie_chartS(df, 'genre')
                        choice3 =  st.sidebar.selectbox("Choose a day",[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,22, 23, 24, 25, 26, 27, 28, 29, 30,31])
                        if(choice3):
                            if(choice2 in [4,6,9,11,2] and choice3 == 31):
                                st.error("the month selected does not have 31 days.")  
                            elif(choice2 == 2 and choice3 > 29 and choice1 != 2020):
                                st.error("february has 28 days.")
                            elif(choice2 == 2 and choice3 > 28):
                                st.error("february has 28 days.")
                            else:
                                #compareDay(choice3, df)
                                st.title(f'On the {choice3} of {current_month(choice2)}  {choice1}')
                                df =  df.loc[df['day'] == choice3]
                                histo(df, 'hour')
                                line_chart(df, 'hour')
                                st.title(f'What kind of videos did I watch today.')
                                st.write("Let us see.")
                                pie_chart(df, 'genre')
                                st.write("If we just take the channels I am subscribed to:")
                                pie_chartS(df, 'genre')

    #counting rows
    def count_rows(rows):
        return len(rows)

    #returns a series object with the number of rows for a certain feature
    def Number(feature, df):
        return df.groupby(feature).apply(count_rows)

    # Creates an histogram depending on the data
    def histo(df, feature):
        fig, ax = plt.subplots()
        binss = Number(feature, df)
        binss = binss.shape[0]
        if(binss != 0):
            ax.hist(df[feature], bins= binss, rwidth = 0.7)
            if(feature == 'month'):
                ax.set_xlabel('Months of the year')
            elif(feature == 'day'):
                ax.set_xlabel('Days of the month')
            else:
                ax.set_xlabel('hours of the day')
            ax.set_ylabel('Number of videos')
        st.pyplot(fig)


    # pie chart with the kind 'other'
    def pie_chart(df, feature):
        genre =Number(feature, df)
        if(len(genre) > 0):
            fig = px.pie(getPieData(genre), values='number', names='Genre', title='The videos I watch')
            st.write(fig)
        else:
            st.write(f"There is no data of type {feature} or it is inconsistant")

    # pie chart without the kind 'other
    def pie_chartS(df, feature):
        genre =Number(feature, df)
        if(len(genre) > 0):
            genre = genre.drop(['Other'])
            fig = px.pie(getPieData(genre), values='number', names='Genre', title='The videos I watch')
            st.write(fig)
        else:
            st.write(f"There is no data of type {feature} for the chart or it is inconsistant")
    #creates a line chart
    def line_chart(df, feature):
        data =Number(feature, df)
        if(len(data) > 0):
            fig = px.line(getChartData(data, feature), x = feature, y='number of videos', title='The videos I watch')
            st.write(fig)
        else:
            st.write(f"There is no data of type {feature} for the chart or it is inconsistant")

    # Prepares the data for the pie chart
    def getPieData(data):
        labels = []
        for row in data.index:
            labels.append(row)
        for row in data:
            labels.append(row)
        label = labels[0:len(data)]
        number = labels[len(data):]
        pieData = {'Genre':label, 'number':number}
        df = pd.DataFrame(pieData)
        return df
    
    # Prepares the data for the line chart
    def getChartData(data, feature):
        labels = []
        for row in data.index:
            labels.append(row)
        for row in data:
            labels.append(row)
        mesure = labels[0:len(data)]
        number = labels[len(data):]
        pieData = {feature:mesure, 'number of videos':number}
        df = pd.DataFrame(pieData)
        return df
    #compare the increase or decrease in video consumption between years
    def compareYear(choice, df):
        if(choice > 2018):
            year = Number('year',df)
            percentage = ((year[choice] / year[choice - 1]) * 100) - 100
            percentage = round(percentage, 2)
            st.metric(label="Augmentation", value = choice, delta = percentage )
    
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

    st.title("My activity on youtube")
    display_preference(df1)

if __name__ == "__main__":
    main()