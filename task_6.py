#importing libarries
import pandas as pd
import streamlit as st
import plotly.express as px


st.title('Visualiztion Of Titanic Dataset')
titanic = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

#plot scatter chatter between age and fare
scatter = px.scatter(x = titanic['Age'],y= titanic['Fare'],title='Scatter Plot Between Age And Fare')
st.plotly_chart(scatter)

#plot bargraph of survived and not survived passsengers
survived = titanic[titanic['Survived']==1]
not_survived = titanic[titanic['Survived']==0]
no_of_survived = survived.shape[0]
no_of_not_survived = not_survived.shape[0]
#df = pd.DataFrame({'Condition': [ 'Survived','Not_survived'], 'Value' : [no_of_survived, no_of_not_survived]})
bar = px.bar(x=['survived','not_survived'],y=[no_of_survived,no_of_not_survived],title='Bar Graph Of Survived')
st.plotly_chart(bar)