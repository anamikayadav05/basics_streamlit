import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
st.title('Visualization in titanic datasets')
titanic = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
st.header('Bar chart of survived and not survived passengers')
no_of_surv = (titanic['Survived']==1).sum()
no_of_not_surv = (titanic['Survived']==0).sum()
bar = pd.DataFrame({'index':['Survived','Not_survived'],'value':[no_of_surv,no_of_not_surv]}).sort_index('index')
st.bar_chart(bar,width=0)

st.header('Line chart of age and fare')
df = pd.DataFrame()
df['Age'] = titanic['Age']
df['Fare']= titanic['Fare']
st.line_chart(df)

st.header('Boxplot of fare')
fig = plt.figure()
titanic.boxplot(column = ['Fare'])
st.pyplot(fig)

st.header('Distribution of fare')
fig = plt.figure()
titanic['Fare'].plot.hist()
st.pyplot(fig)

st.header('Pie chart of pclass')
new_data = titanic[titanic['Age'].notna()]
fig = plt.figure()
new_data['Pclass'].value_counts().plot.pie()
st.pyplot(fig)