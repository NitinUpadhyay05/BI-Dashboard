import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px

Data = pd.read_csv('Sales.N.csv')
st.set_page_config(page_title="Sales by products and there payment modes Charts:",page_icon=':bar_chart:' , layout= 'wide')
st.title('Sales by products and there payment modes Charts:')
st.markdown('___')
Data.rename(columns={'Product line':'Products'}, inplace=True)

st.sidebar.header('Please Filter Here:')
city = st.sidebar.multiselect(
    "Select The City:",
    options= Data['City'].unique(),
    default= Data['City'].unique()
)


cust_type = st.sidebar.multiselect(
    "Select The customer type:",
    options= Data['Customer_type'].unique(),
    default= Data['Customer_type'].unique()
)

Gender = st.sidebar.multiselect(
    "Select The Gender:",
    options= Data['Gender'].unique(),
    default= Data['Gender'].unique()
)

Products = st.sidebar.multiselect(
    'Choose The Products:',
    options=Data['Products'].unique(),
    default=Data['Products'].unique()
)

Data_Selection = Data.query(
    "City == @city & Customer_type == @cust_type & Gender == @Gender &  Products == @Products"
)

st.markdown('We are going to plot some other charts related to there payments mode and total sale . ')




st.title('1.Sunburst Chart on City ,Gender and Product:')
sunburst_Of_Products = px.sunburst(Data_Selection , path =['City' , 'Gender', 'Products'  ], values = 'Total', color = 'Total' , title ='<b>Total sale by there city gender and products<b>')

st.plotly_chart(sunburst_Of_Products,use_container_width=True)

st.markdown('In the above sunburst chart we have use total 4 variables . ')
st.markdown('The variables is City , Gender,Products and Total sale.')
st.write('This chart shows,In different  cities how much product sale had done by males and females ')


st.title('2.Histogram of Tyeps of payments:')


Type_of_payments = px.histogram(Data_Selection , x = 'Products',y = 'Total',color =  'Payment',barmode = 'group', title='<b>Types of payments by there products<b>')
st.plotly_chart(Type_of_payments,use_container_width=True)


st.write('The above histogram shows ,what are the payments mode used by the customers for purchasing there products.')
st.markdown('...')