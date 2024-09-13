import streamlit as st
from motorrcPatrimonial import pagePatrimonial

##############################################################################################################################################
#CHAMANDO O MOTOR POR PRODUTO

with st.sidebar:
   st.title("Motor de Cálculo")
   pageProduto = st.selectbox('Selecione o Produto',['RC Patrimonial'],index=None, placeholder="Produtos")
   
if pageProduto =='RC Patrimonial':
     pagePatrimonial()

