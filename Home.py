
import pandas as pd
import numpy as np
import streamlit as st


Data = pd.read_csv('Sales.N.csv')

st.set_page_config(page_title="SuperMarket Sales Dashboard",page_icon=':bar_chart:' , layout= 'wide')

st.title(':bar_chart: SuperMarket Sales Dashboard')
st.markdown('##')


total_sales = int(Data['Total'].sum())
average_rating = round(Data['Rating'].mean(),1)
star_rating = ':star:'*int(round(average_rating,0))
average_sales = round(Data['Total'].mean(),2)

left_column , middle_column , right_column = st.columns(3)

with left_column:
    st.subheader('Total Sales:')
    st.subheader(f'{total_sales:}')

with middle_column:
    st.subheader('Average Rating')
    st.subheader(f'{average_rating} {star_rating}')

with right_column:
    st.subheader('Average Sales Per Transaction')
    st.subheader(f'{average_sales}')
st.markdown('---')

st.markdown('We are going creat a Dhasboard on supermarket sales data .')

st.title('Here is the Data:')
Data

st.markdown('This is the data and it is represent sales data .')
st.markdown('There are 1000 rows and 17 columns in sales data. ')
st.markdown('On the basis of this data we are going to plot some charts . From that charts we are concluding what that charts represent.')


st.markdown('Lets go on Sales by product page.')