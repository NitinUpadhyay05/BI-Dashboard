import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

Data = pd.read_csv('Sales.N.csv')

st.set_page_config(page_title="Sale by Products.",page_icon=':bar_chart:' , layout= 'wide')
st.title("Sale by Products.")
st.markdown('##')
st.write('Now, We are going to Draw some Chart .')



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

Data_Selection = Data.query(
    "City == @city & Customer_type == @cust_type & Gender == @Gender "
)


sales_by_product_line = Data_Selection.groupby(by=['Products']).sum().sort_values(by='Total')


fig_product_line = px.bar(
    sales_by_product_line,
    x = 'Total',
    y = sales_by_product_line.index,
    orientation='h',
    title= "<b>Sales By Product Bar chart<b>",
    color_discrete_sequence=['#9467bd']*len(sales_by_product_line),
    template='plotly_white'


)
fig_product_line.update_layout(
    
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis = (dict(showgrid = False)),
    xaxis = (dict(showgrid = False))
)







Quantity_product = px.line(sales_by_product_line, x= sales_by_product_line.index, y  = 'Quantity' , title='<b> Quantity sale of Products<b>')


col1 , col2 = st.columns([50,50])

with col1:
    st.title('Bar Chart Total sale of products')
    st.plotly_chart(fig_product_line,use_container_width=True)

with col2:
    st.title('Line Chart sale of product by quantity')
    st.plotly_chart(Quantity_product,use_container_width=True)

st.title('Histogram of tax 5%:')


Tax_chart_by_Member_a_products = px.histogram(Data_Selection , x = 'Products',y = 'Tax 5%' , color = 'Customer_type', barmode = 'group', title = '<b>Tax pay by customer type.<b>')
st.plotly_chart(Tax_chart_by_Member_a_products,use_container_width=True)
Tax_chart_by_Member_a_products.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis = (dict(showgrid = False)),
    xaxis = (dict(showgrid = False))
)


st.title('Histogram of Tyeps of payments:')


Type_of_payments = px.histogram(Data_Selection , x = 'Products',y = 'Total',color =  'Payment',barmode = 'group', title='<b>Types of payments by there products<b>')
st.plotly_chart(Type_of_payments,use_container_width=True)

Type_of_payments.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis = (dict(showgrid = False))
)


st.markdown('...')