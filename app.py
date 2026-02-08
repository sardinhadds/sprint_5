import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles.csv')
st.header('Anúncio online de carros')
hist_button = st.button('Criar histograma')
scatter_button = st.button('Criar gráfico')
        
if hist_button: # se o botão for clicado
    st.write('Criando um histograma')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Criando um gráfico de dispersão')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
