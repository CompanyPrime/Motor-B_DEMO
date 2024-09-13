import streamlit as st
#from motorrcOperacional import pageOperacional
#from motorrctransp      import pageTransporte
from motorrcPatrimonial import pagePatrimonial

##############################################################################################################################################
#CHAMANDO O MOTOR POR PRODUTO
#st.set_page_config(layout="wide") para deixar a tela justificada e ocupar toda a tela.

with st.sidebar:
   st.title("Motor de Cálculo")
   pageProduto = st.selectbox('Selecione o Produto',['RC Patrimonial'],index=None, placeholder="Produtos")
   #pageProduto = st.selectbox('Selecione o Produto',['RC Patrimonial', 'RC Ambiental Transporte', 'RC Ambiental Operacional'],index=None, placeholder="Produtos")
   
if pageProduto =='RC Patrimonial':
     pagePatrimonial()

#if pageProduto =='RC Ambiental Operacional':
#     pageOperacional()

#if pageProduto =='RC Ambiental Transporte':
#     pageTransporte()


# streamlit run "c:/Users/fabricio/OneDrive - MB CONSULTORIA EMPRESARIAL E CONTABIL LTDA/1.Programas Python Company/BMG/Motor_calculo/PainelMotor.py"