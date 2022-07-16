import pandas as pd
import streamlit as st

st.title('Dummy dataframe')
#creating an empty dataframe of columns of original data
titanic = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
columns = titanic.columns
dummy_df = pd.DataFrame(columns = columns)
#adding rows in empty dataframe
dummy_df = dummy_df.append({'PassengerId':892,'Survived':1,'Pclass':1,'Name':'George Bush','Sex':'male','Age':1.2,'Sibsp':0,'Parch':3,'Ticket':'r2189','Fare':21.1,'Cabin':None,'Embarked':'S'},ignore_index=True)
dummy_df = dummy_df.append({'PassengerId':893,'Survived':0,'Pclass':2,'Name':'Jasmine Bush','Sex':'female','Age':0.2,'Sibsp':0,'Parch':3,'Ticket':'r2189','Fare':21.1,'Cabin':None,'Embarked':'S'},ignore_index=True)
dummy_df = dummy_df.append({'PassengerId':893,'Survived':1,'Pclass':1,'Name':'James Smith','Sex':'male','Age':1.2,'Sibsp':0,'Parch':3,'Ticket':'r2189','Fare':21.1,'Cabin':None,'Embarked':'S'},ignore_index=True)
dummy_df = dummy_df.append({'PassengerId':894,'Survived':0,'Pclass':3,'Name':'Madame Julie','Sex':'female','Age':1.2,'Sibsp':0,'Parch':3,'Ticket':'r2189','Fare':21.1,'Cabin':None,'Embarked':'S'},ignore_index=True)
dummy_df = dummy_df.append({'PassengerId':895,'Survived':1,'Pclass':1,'Name':'Jim Bush','Sex':'male','Age':1.2,'Sibsp':0,'Parch':3,'Ticket':'r2189','Fare':21.1,'Cabin':None,'Embarked':'S'},ignore_index=True)
dummy_df = dummy_df.append({'PassengerId':896,'Survived':1,'Pclass':1,'Name':'Cannl Thomas','Sex':'male','Age':1.2,'Sibsp':0,'Parch':3,'Ticket':'r2189','Fare':21.1,'Cabin':None,'Embarked':'S'},ignore_index=True)
st.dataframe(dummy_df)