import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

Data = pd.read_csv('Sales.N.csv')

st.set_page_config(page_title="Sale by Products.",page_icon=':bar_chart:' , layout= 'wide')
st.title("Sale by Products.")
st.markdown('##')
st.markdown('Now, We are going to Draw some Chart .')

st.title('1. Bar Chart Total sale of products')

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
    yaxis = (dict(showgrid = False))
)

st.plotly_chart(fig_product_line,use_container_width=True)


st.markdown('As we can see the bar chart represents the total sale of products.')
st.markdown('This bar chart shows which product sale is higher. As, we can see In  this bar chart Food and Beverage sale is higher then the others.')


st.title('2. Line Chart sale of product by quantity')

Quantity_product = px.line(sales_by_product_line, x= sales_by_product_line.index, y  = 'Quantity' , title='<b> Quantity sale of Products<b>')
st.plotly_chart(Quantity_product,use_container_width=True)

st.markdown('The above line chart represents in how much quantity customers purchased the products.')
st.markdown('And, This is also represents which product sale  is higher in quantity or we can say as per the quantity of Product  which product purchased more by the customers. ')

st.title('Histogram of tax 5%:')


Tax_chart_by_Member_a_products = px.histogram(Data_Selection , x = 'Products',y = 'Tax 5%' , color = 'Customer_type', barmode = 'group', title = '<b>Tax pay by customer type.<b>')
st.plotly_chart(Tax_chart_by_Member_a_products,use_container_width=True)

st.markdown('In this Histogram we have used three variables.on x-axis products , on y axis = sum of tax and the third variable is customer type .')
st.markdown('In the customer type there are two type of customers  normal customers and member customers .')
st.markdown('Histogram shows tax payed from the member customer and tax payed bt the normal customer omn there Products .')
