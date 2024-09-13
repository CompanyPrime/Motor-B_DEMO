import streamlit as st
import pandas as pd
from api_receita import consulta_cnpj
import locale

def pagePatrimonial():
     ##############################################################################################################################################
     #INCLUINDO O LOGO DA EMPRESA
     # URL da imagem do site
     url_imagem = 'https://www.bancobmg.com.br/lumis-theme/br/com/bmg/portal/theme/bmg-portal/img/logo-bmg.svg'
     
     # Exibir a imagem do site
     st.image(url_imagem, width=200)

     ##############################################################################################################################################
     #PRODUTO - TRANSPORTE OU OPERACIONAL
     st.subheader("Produto - Patrimonial")

     st.write("---") #Pular Linha     

     st.subheader("QAR - Questionário de Avaliação de Risco")

     ##############################################################################################################################################
     #CRIA O DICIONÁRIO COM AS RELATIVIDADES DE OPERACIONAL
     ml_intercepto= {"chave": [1],
                    "modelo": ['patrimonial'],
                    "intercepto":[1541.96]}

     import_coef_atividade  = {"chave": [1,1,1,1,1],
                    "atividade":['Academia de Ginástica', 'Acetileno', 'Acetona', 'Ácidos', 'Acolchoados'],
                    "coef_atividade":[1.500000, 1.150000, 1.150000, 1.150000, 1.100000]}

     import_coef_shopping = {"chave": [1,1], "local_shopping" : ['Sim', 'Não'], "coef_shopping" :[0.500000, 1.000000]}

     import_coef_lucro_cess  = {"chave": [1,1,1,1,1,1,1,1,1,1,1,1,1],
                    "lucro_cessante":['Não contratado', '1 mês', '2 meses', '3 meses', '4 meses', '5 meses', '6 meses', '7 meses', '8 meses', '9 meses', '10 meses', '11 meses', '12 meses'],
                    "coef_lucro_cessante":[1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000]}

     import_coef_protecao_incendio  = {"chave": [1,1,1,1,1],
                    "protecao_incendio":['Alarme de incêndio',
                                         'Extintor (com carga e dentro do prazo de validade)',
                                         'Hidrante',
                                         'Sistema de detecção de fumaça',
                                         'Sprinkers'],
                    "coef_protecao_incendio":[0.950000, 0.950000, 0.850000, 0.950000, 0.800000]}
     
     import_coef_protecao_roubo  = {"chave": [1,1,1,1],
                    "protecao_roubo":['Alarme monitorado por empresa especializada 24hrs',
                                      'Risco localiza-se a partir de 2º andar',
                                      'Sistema de alarme',
                                      'Vigilância exclusiva 24h (365 dias ao ano)'],
                    "coef_protecao_roubo":[0.90000, 0.90000, 0.95000, 0.85000]}

     import_coef_tot_sin_ind  = {"chave": [1,1,1,1,1],
                    "tot_sin_ind":['Até R$10.000,00',
                                   'De R$ 10.000,01 até R$ 100.000,00',
                                   'De R$ 100.000,01 até R$ 1.000.000,00',
                                   'Acima de R$ 1.000.000,01',
                                   'Sem Sinistro'],
                    "coef_tot_sin_ind":[1.10000, 1.20000, 1.50000, 5.00000, 1.00000]}

     import_coef_tip_cobert = {"chave": [1,1],
                    "tip_cobert" : ['LMI Risco a Risco', 'LMI Único'],
                    "coef_tip_cobert" :[1.000000, 1.000000]}

     import_coef_tip_construcao  = {"chave": [1,1,1,1],
                    "tip_construcao":['Inferior',
                                      'Mista',
                                      'Sólida',
                                      'Superior'],
                    "coef_tip_construcao":[1.20000, 1.10000, 0.90000, 0.80000]}

     import_coef_tip_contratacao  = {"chave": [1,1,1],
                    "tip_contratacao":['Apenas Conteúdo',
                                       'Apenas Prédio',
                                       'Prédio + Conteúdo'],
                    "coef_tip_contratacao":[0.800000, 0.800000, 1.000000]}

     import_coef_tip_risco  = {"chave": [1,1,1,1],
                    "tip_risco":['Comércio',
                                 'Depósito/Armazém/Centro Logístico/Transportadora/Distribuidora',
                                 'Indústria',
                                 'Serviço'],
                    "coef_tip_risco":[1.500000, 2.000000, 2.000000, 1.500000]}

     import_coef_qtde_cobert  = {"chave": [1,1],
                    "qtde_cobert":['Até 6', 'Acima de 6'],
                    "coef_qtde_cobert":[1.000000, 0.900000]}

     import_coef_bonus = {"chave": [1,1,1,1,1,1,1,1,1,1,1],
                         "BONUS": [0,1,2,3,4,5,6,7,8,9,10],
                         "coef_bonus":[1.000000, 0.989231, 0.979616, 0.968847, 0.958463, 0.948078, 0.939270, 0.930000, 0.929423, 0.919039, 0.909808,]}

     import_coef_tipseg = {"chave": [1,1,1],
                         "tip_seg": ['Novo', 'Renovação','Renovação Congênere'],
                         "coef_tipseg":[1.000000, 0.909505, 0.859752]}
     
     import_tx_cobertura = {"chave": [1,1,1,1,1,1,1,1],
               "cobertura":  ['C101401-Cobertura Básica nº 001A - Incêndio, Raio, Explosão, Implosão e Fumaça',
                              'C101402-Cobertura Básica nº 001B - Incêndio, (Inclusive de Tumultos, Greves e Lock-out), Raio, Explosão, Implosão e Fumaça',
                              'C101403-Cobertura Básica nº 001C - Incêndio, Raio, Explosão, Implosão, Fumaça e Queda de Aeronaves',
                              'C101404-Cobertura Básica nº 001D - Incêndio, (Inclusive decorrente de Tumulto, Greves e Lock-out), Raio, Explosão, Implosão, Fumaça e Queda de Aeronaves',
                              'C101405-Cobertura Adicional Nº. 006 - Danos Elétricos',
                              'C101406-Cobertura Adicional Nº. 007 - Tumultos, Greves, Lockout e Atos Dolosos',
                              'C101407-Cobertura Adicional Nº. 011 - Quebra de Vidros, Espelhos, Mármores e Granitos',
                              'C101408-Cobertura Adicional Nº. 014 - Desmoronamento'],
               "coef_TX_cobertura":[1.0203, 1.0204, 1.0241, 1.0242, 1.3664, 1.0080, 1.6863, 1.0344]}
     
     import_empresa_mulher = {"chave": [1,1,1],
                    "empresa_mulher": ['Sim', 'Não', 'Não sei informar'],
                    "coef_empresa_mulher":[0.970000, 1.0000000, 1.000000]}

     #LOADS DE AGRAVO/DESCONTO
     import_load_da              = {"chave": [1], "coef_load_DA":                     [1.250000]}
     import_load_do              = {"chave": [1], "coef_load_DO":                     [1.100000]}
     import_load_lucro           = {"chave": [1], "coef_load_lucro":                  [1.100000]}
     import_load_impostos        = {"chave": [1], "coef_load_impostos":               [1.350000]}
     import_load_ibnr            = {"chave": [1], "coef_load_ibnr":                   [1.030000]}
     import_load_tendencia       = {"chave": [1], "coef_load_tendencia":              [1.000000]}
     import_load_salvado         = {"chave": [1], "coef_load_salvado":                [1.000000]}
     import_load_ressarcimento   = {"chave": [1], "coef_load_ressarcimento":          [1.000000]}
     import_load_iof             = {"chave": [1], "coef_load_iof":                    [1.070000]}
     import_load_inflacaoSin     = {"chave": [1], "coef_load_inflacao_sinistro":      [1.000000]}
     import_load_sinistroJud     = {"chave": [1], "coef_load_sinistro_judicial":      [1.000000]}
     import_load_carregamentoSeg = {"chave": [1], "coef_load_carregamento_seguranca": [1.010000]}
     import_load_comCorretor     = {"chave": [1], "coef_load_comissao_corretor":      [1.020000]}
     import_load_franquia        = {"chave": [1], "coef_load_franquia":               [0.800000]}


     ##############################################################################################################################################
     #TRANSFORMA OS ARQUIVOS DO DICIONÁRIO EM DATAFRAME

     ml_intercepto               = pd.DataFrame(ml_intercepto)
     import_coef_tipseg          = pd.DataFrame(import_coef_tipseg)
     import_coef_bonus           = pd.DataFrame(import_coef_bonus)
     import_coef_atividade       = pd.DataFrame(import_coef_atividade)
     import_coef_shopping        = pd.DataFrame(import_coef_shopping)
     import_coef_protecao_incendio    = pd.DataFrame(import_coef_protecao_incendio)
     import_coef_lucro_cess      = pd.DataFrame(import_coef_lucro_cess)
     import_coef_protecao_roubo  = pd.DataFrame(import_coef_protecao_roubo)
     import_coef_tot_sin_ind     = pd.DataFrame(import_coef_tot_sin_ind)
     import_coef_tip_cobert      = pd.DataFrame(import_coef_tip_cobert)
     import_coef_tip_construcao  = pd.DataFrame(import_coef_tip_construcao)
     import_coef_tip_contratacao = pd.DataFrame(import_coef_tip_contratacao)
     import_coef_tip_risco       = pd.DataFrame(import_coef_tip_risco)
     import_coef_qtde_cobert     = pd.DataFrame(import_coef_qtde_cobert)
     import_empresa_mulher       = pd.DataFrame(import_empresa_mulher)
     import_tx_cobertura         = pd.DataFrame(import_tx_cobertura)
     
     import_load_da              = pd.DataFrame(import_load_da)
     import_load_do              = pd.DataFrame(import_load_do)
     import_load_lucro           = pd.DataFrame(import_load_lucro)
     import_load_impostos        = pd.DataFrame(import_load_impostos)
     import_load_ibnr            = pd.DataFrame(import_load_ibnr)
     import_load_tendencia       = pd.DataFrame(import_load_tendencia)
     import_load_salvado         = pd.DataFrame(import_load_salvado)
     import_load_ressarcimento   = pd.DataFrame(import_load_ressarcimento)
     import_load_iof             = pd.DataFrame(import_load_iof)
     import_load_inflacaoSin     = pd.DataFrame(import_load_inflacaoSin)
     import_load_sinistroJud     = pd.DataFrame(import_load_sinistroJud)
     import_load_carregamentoSeg = pd.DataFrame(import_load_carregamentoSeg)
     import_load_comCorretor     = pd.DataFrame(import_load_comCorretor)
     import_load_franquia        = pd.DataFrame(import_load_franquia)


     ##############################################################################################################################################
     #INICIO DO QAR-QUESTIONÁRIO DE AVALIAÇÃO DE RISCO - OPERACIONAL
     #st.subheader("Tipo de Risco")
     distinct_tip_risco = import_coef_tip_risco['tip_risco'].unique().tolist()
     response_tip_risco= st.selectbox('Tipo de Risco',distinct_tip_risco, index=None, placeholder="Selecione uma Opção")
     coef_tiprisco = import_coef_tip_risco[import_coef_tip_risco['tip_risco']==response_tip_risco]

     distinct_atividade = import_coef_atividade['atividade'].unique().tolist()
     response_atividade= st.selectbox('Atividade',distinct_atividade, index=None, placeholder="Selecione uma Opção")
     coef_atividade = import_coef_atividade[import_coef_atividade['atividade']==response_atividade]

     distinct_shopping = import_coef_shopping['local_shopping'].unique().tolist()
     response_shopping= st.selectbox('O risco está localizado em Shopping?',distinct_shopping, index=None, placeholder="Selecione uma Opção")
     coef_shopping = import_coef_shopping[import_coef_shopping['local_shopping']==response_shopping]

     distinct_tot_sin_ind = import_coef_tot_sin_ind['tot_sin_ind'].unique().tolist()
     response_tot_sin_ind= st.selectbox('Soma total de sinistro indenizado',distinct_tot_sin_ind, index=None, placeholder="Selecione uma Opção")
     coef_tot_sin_ind = import_coef_tot_sin_ind[import_coef_tot_sin_ind['tot_sin_ind']==response_tot_sin_ind]

     distinct_tip_construcao = import_coef_tip_construcao['tip_construcao'].unique().tolist()
     response_tip_construcao= st.selectbox('Tipo de Construção',distinct_tip_construcao, index=None, placeholder="Selecione uma Opção")
     coef_tip_construcao = import_coef_tip_construcao[import_coef_tip_construcao['tip_construcao']==response_tip_construcao]

     distinct_tip_contratacao = import_coef_tip_contratacao['tip_contratacao'].unique().tolist()
     response_tip_contratacao= st.selectbox('Tipo de Contratação',distinct_tip_contratacao, index=None, placeholder="Selecione uma Opção")
     coef_tip_contratacao = import_coef_tip_contratacao[import_coef_tip_contratacao['tip_contratacao']==response_tip_contratacao]

     distinct_tip_cobert = import_coef_tip_cobert['tip_cobert'].unique().tolist()
     response_tip_cobert= st.selectbox('Tipo de Cobertura',distinct_tip_cobert, index=None, placeholder="Selecione uma Opção")
     coef_tip_cobert = import_coef_tip_cobert[import_coef_tip_cobert['tip_cobert']==response_tip_cobert]

     distinct_lucro_cess = import_coef_lucro_cess['lucro_cessante'].unique().tolist()
     response_lucro_cess= st.selectbox('PI Lucro Cessante',distinct_lucro_cess, index=None, placeholder="Selecione uma Opção")
     coef_lucro_cess = import_coef_lucro_cess[import_coef_lucro_cess['lucro_cessante']==response_lucro_cess]
     
     #locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')  # Definir apenas para números
     colvl1, colvl2, colvl3 = st.columns(3)
     with colvl1:
          vl_edificio = st.number_input('Valor do Edifício', min_value=0.00)

     with colvl2:
          vl_conteudo = st.number_input('Valor do Conteúdo', min_value=0.00)

     with colvl3:
          vl_ben_edificio = st.number_input('Valor dos Bens Específicos', min_value=0.00)

     vl_risco = vl_edificio + vl_conteudo + vl_ben_edificio

     #with colvl4:
     #     vl_risco = vl_edificio + vl_conteudo + vl_ben_edificio
     #     formatted_risco = locale.format_string("%.2f", vl_risco, grouping=True)

          # Custom CSS para diminuir o tamanho da letra da métrica
     #     st.markdown(
     #          f"""
     #         <style>
     #          .small-font {{
     #               font-size: 15px !important;
     #               color: black !important;
     #     }}
     #     </style>
     #     """, unsafe_allow_html=True
     #     )
     #     st.markdown(f"""<div class="label-font">Valor Total do Risco</div>
     #                     <div class="small-font">R$ {formatted_risco}</div>
     #               """, unsafe_allow_html=True)
    
     distinct_qtde_cobert = import_coef_qtde_cobert['qtde_cobert'].unique().tolist()
     response_qtde_cobert = st.selectbox('Quantidade de Coberturas',distinct_qtde_cobert, index=None, placeholder="Selecione as Opções")
     coef_qtde_cobert = import_coef_qtde_cobert[import_coef_qtde_cobert['qtde_cobert'] == response_qtde_cobert]

     distinct_empresa_mulher = import_empresa_mulher['empresa_mulher'].unique().tolist()
     response_empresa_mulher = st.selectbox('A empresa tem mais que 50% de mulheres em seu quadro de funcionários?',distinct_empresa_mulher, index=None, placeholder="Selecione uma Opção")
     coef_empresa_mulher = import_empresa_mulher[import_empresa_mulher['empresa_mulher'] == response_empresa_mulher]
    
     ###################################################################################################################################################################
     # COBERTURAS
     st.title("Coberturas")
     distinct_tx_cobertura = import_tx_cobertura['cobertura'].unique().tolist()
     response_tx_cobertura = st.multiselect('Selecione a Cobertura', distinct_tx_cobertura, placeholder="Coberturas")

     # Filtrando a base com as coberturas selecionadas
     if response_tx_cobertura:
          coef_tx_cobertura = import_tx_cobertura[import_tx_cobertura['cobertura'].isin(response_tx_cobertura)]
     else:
          coef_tx_cobertura = pd.DataFrame()  # Retorna DataFrame vazio se nada for selecionado

     if not coef_tx_cobertura.empty:
          df_LMI = coef_tx_cobertura[['cobertura']].copy()
          df_LMI['LMI-(LimitInPage)'] = 0
          df_LMI = st.data_editor(df_LMI)
     else:
          st.write("Nenhuma cobertura selecionada.")
     
     ###################################################################################################################################################################
     # PROTEÇÃO CONTRA INCENDIO
     distinct_protecao_incendio = import_coef_protecao_incendio['protecao_incendio'].unique().tolist()
     response_protecao_incendio= st.multiselect('Sistemas Protecionais 100% Operantes - Incêndio:', distinct_protecao_incendio, placeholder="Selecione as Opções desejada")
     
     # Filtrando a base com as coberturas selecionadas
     if response_protecao_incendio:
          coef_protecao_incendio = import_coef_protecao_incendio[import_coef_protecao_incendio['protecao_incendio'].isin(response_protecao_incendio)]
     else:
          coef_protecao_incendio = pd.DataFrame()  # Retorna DataFrame vazio se nada for selecionado

     #st.write(coef_protecao_incendio)
     
     
     ###################################################################################################################################################################
     # PROTEÇÃO CONTRA ROUBO
     distinct_protecao_roubo = import_coef_protecao_roubo['protecao_roubo'].unique().tolist()
     response_protecao_roubo= st.multiselect('Sistemas Protecionais 100% Operantes - Roubo:', distinct_protecao_roubo, placeholder="Selecione as Opções desejada")
     
     # Filtrando a base com as coberturas selecionadas
     if response_protecao_roubo:
          coef_protecao_roubo = import_coef_protecao_roubo[import_coef_protecao_roubo['protecao_roubo'].isin(response_protecao_roubo)]
     else:
          coef_protecao_roubo = pd.DataFrame()  # Retorna DataFrame vazio se nada for selecionado

     #st.write(coef_protecao_roubo)

     ###################################################################################################################################################################
     # Fator de Desconto/Agravo
     coef_desconto_agravo = st.number_input("Fator de Desconto/Agravo (OBS: Para desconto, adicionar o 'Menos' na frente do Número. Ex. 5% de desconto = -5,00)", value=100.00, format="%.2f")

     if coef_desconto_agravo < 100:
          coef_desconto_agravo = (coef_desconto_agravo / 100) + 1

     if coef_desconto_agravo >= 100:
          coef_desconto_agravo = (coef_desconto_agravo / 100)
     
     coef_desconto_agravo = pd.DataFrame({'coef_desc_agravo': [coef_desconto_agravo]})

     # Exibe o DataFrame no Streamlit
     #st.write(coef_desconto_agravo)


     ###################################################################################################################################################################
     # DEMOSTRA OS FATORES


     #st.write(coef_tiprisco)
     #st.write(coef_atividade)
     #st.write(coef_shopping)
     #st.write(coef_tot_sin_ind)
     #st.write(coef_tip_construcao)
     #st.write(coef_tip_contratacao)
     #st.write(coef_tip_cobert)
     #st.write(df_LMI)
     #st.write(coef_lucro_cess)
     #st.write(vl_risco)
     #st.write(coef_qtde_cobert)
     #st.write(coef_empresa_mulher)
     #st.write(coef_protecao_incendio)
     #st.write(coef_protecao_roubo)


    
     #st.subheader("Selecione a Classe de Bônus")
     #distinct_BONUS = import_coef_bonus['BONUS'].unique().tolist()
     #response_bonus= st.selectbox('Classe de Bônus',distinct_BONUS, index=None, placeholder="Selecione uma Opção")
     #coef_bonus = import_coef_bonus[import_coef_bonus['BONUS']==response_bonus]

     
          
     ##############################################################################################################################################
     #FAZ O MERGE DAS TABELAS QAR COM INTERCEPTO 
     #ml_1 = pd.merge(ml_intercepto, coef_tipseg,       on='chave', how='left')

     #ml_1 = pd.merge(ml_1,  coef_tipempresa,           on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_uf,                   on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_LMI,                  on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_bonus,                on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_tipTanque,            on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_matConstTubulacao,    on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_matConstrucaoTanque,  on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_conteudoTanque,       on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_protTransbordamento,  on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_detectaVazTubulacao,  on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_detectaVazTanque,     on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_contencaoTanque,      on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_controleTanqueAereo,  on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_brigadaIncendio,      on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_sujeitoAlagamento,    on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_EteLocalRisco,        on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_lodoEte,              on='chave', how='left')
     #ml_1 = pd.merge(ml_1,  coef_sinistroUltAno,       on='chave', how='left')

     # MERGE DOS LOADS DE CARREGAMENTO
     #ml_1 = pd.merge(ml_1, import_load_da,              on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_do,              on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_lucro,           on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_impostos,        on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_ibnr,            on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_tendencia,       on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_salvado,         on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_ressarcimento,   on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_iof,             on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_inflacaoSin,     on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_sinistroJud,     on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_carregamentoSeg, on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_comCorretor,     on='chave', how='left')
     #ml_1 = pd.merge(ml_1, import_load_franquia,        on='chave', how='left')


     ##############################################################################################################################################
     #CALCULO DAS RELATIVIDADES DO QAR OPERACIONAL E INTERCEPTO DA MODELAGEM  - PRÊMIO DE RISCO SEM CARREGAMENTOS

     #ml_1['prRisco_0'] = ml_1['intercepto']*ml_1['coef_tipseg']*ml_1['coef_tipempresa']*ml_1['coef_uf']*ml_1['coef_tipTanque']*ml_1['coef_mat_const_tubulacao']*ml_1['coef_matConstrucaoTanque']*ml_1['coef_lmi']*ml_1['coef_conteudoTanque']*ml_1['coef_protTransbordamento']*ml_1['coef_detectaVazTubulacao']*ml_1['coef_detectaVazTanque']*ml_1['coef_contencaoTanque']*ml_1['coef_controleTanqueAereo']*ml_1['coef_brigadaIncendio']*ml_1['coef_sujeitoAlagamento']*ml_1['coef_EteLocalRisco']*ml_1['coef_lodoEte']*ml_1['coef_sinistroUltAno']*ml_1['coef_bonus']*ml_1['coef_load_franquia']
     #pr_risco = pd.DataFrame(ml_1)

     #PRÊMIO DE RISCO COM A INCLUSÃO DOS LOAD'S "INFLAÇÃO DE SINISTRO" - "TENDENCIA" e "IBNR" - CARREGAMENTO 01
     #pr_risco['prRisco_1'] = pr_risco['prRisco_0']*pr_risco['coef_load_inflacao_sinistro']*pr_risco['coef_load_tendencia']*pr_risco['coef_load_ibnr']

     #PRÊMIO DE RISCO COM A INCLUSÃO DOS LOAD'S - "SALVADO" e "RESSARCIMENTO" - "SINISTRO JUDICIAL" - CARREGAMENTO 02
     #pr_risco['prRisco_2'] = pr_risco['prRisco_1']*pr_risco['coef_load_salvado']*pr_risco['coef_load_ressarcimento']*pr_risco['coef_load_sinistro_judicial']

     ##############################################################################################################################################
     #PRÊMIO PURO COM A INCLUSÃO DO LOAD "INFLAÇÃO DE SINISTRO" - "CARREGAMENTO DE SEGURANÇA" - CARREGAMENTO 03
     #pr_puro = pd.DataFrame(pr_risco)
     #pr_puro['prPuro'] = pr_puro['prRisco_2']*pr_puro['coef_load_carregamento_seguranca']


     ##############################################################################################################################################
     #PRÊMIO LIQUIDO COM A INCLUSÃO DOS LOADS "COMISSÃO" - "DO" - "DA" - "IMPOSTOS" - "LUCRO" - (OBS: COMISSÃO ESTÁ FULL EM 1%)
     #pr_liquido = pd.DataFrame(pr_puro)
     #pr_liquido['prLiquido'] = pr_liquido['prPuro']*pr_liquido['coef_load_comissao_corretor']*pr_liquido['coef_load_DO']*pr_liquido['coef_load_DA']*pr_liquido['coef_load_impostos']*pr_liquido['coef_load_lucro']

     #print(pr_liquido)

     ##############################################################################################################################################
     #PRÊMIO TOTAL COM INCLUSÃO DO "IOF"
     #pr_total = pd.DataFrame(pr_liquido)
     #pr_total['prTotal'] = pr_total['prLiquido']*pr_total['coef_load_carregamento_seguranca']

     #SELECIONA APENAS O PRÊMIO FINAL
     #pr_total = (pr_total['prTotal'])

     #st.write("---") #Pular Linha    

     #print(pr_total)

     ##############################################################################################################################################
     #DADOS DO SEGURADO
     st.subheader("Dados do Segurado")

     cnpj = st.text_input(label='Digite o CNPJ do Segurado')
     st.markdown('**Digite o CNPJ e clique em Calcular**')
     st.markdown('OBS: Esta consulta permite 3 CNPJ por minuto (**API Pública**)')
     st.markdown('Caso ocorra algum erro, por favor, aguarde 1 minuto para calcular.')

     if cnpj == '':
          st.subheader('')
     else: 
          campos = consulta_cnpj(cnpj)

          col1, col2 = st.columns(2)
          with col2:st.write("**Situação:**",campos[0])
          with col1:st.write("**Nome Segurado:**",campos[1])

          col11, col12, col13 = st.columns(3)
          with col11:st.write("**Porte:**",campos[2])
          with col12:st.write("**Logradouro:**",campos[3])
          with col13:st.write("**Número:**",campos[4])

          col21, col22, col23, col24 = st.columns(4)
          with col21:st.write("**Municipio:**",campos[5])
          with col22:st.write("**Bairro:**",campos[6])
          with col23:st.write("**UF:**",campos[7])
          with col24:st.write("**CEP:**",campos[8].replace('.','').replace('-','').replace(')',''))

          col31, col32, col33 = st.columns(3)
          with col31:st.write("**E-mail:**",campos[9])
          with col32:st.write("**Telefone:**",campos[10])
          with col33:st.write("**Status:**",campos[11])

     st.write("---") #Pular Linha    


     ##############################################################################################################################################
     #DADOS DO CORRETOR
     #st.subheader("Dados do Corretor")
     #st.markdown('Código-23867')
     #st.markdown('Nome: LOJACORR S/A REDE DE CORRETORES DE SEGUROS')
     #load_comissao = st.number_input('Comissão do Corretor', min_value=0, max_value=50)

     #st.write("---") #Pular Linha    

     ##############################################################################################################################################
     #FORMATAR VALOR
     #with pd.option_context('display.float_format','R$ {:_.2f}'.format):
          
          #Retirando o Indice do arquivo de Risco
      #    serie = pr_total.to_string(index=False) 

     #serie = serie.replace(".",",").replace("_",".")

     #print(serie)


     ##############################################################################################################################################
     #BOTÃO CALCULAR
     #if st.button("Calcular"):
      #    st.write("**Prêmio Total (Com Carregamentos)**",serie)
       #   st.write("---") #Pular Linha   
        #  st.subheader("Carregamentos:")

     ##############################################################################################################################################
     #MOSTRAR CARREGAMENTOS NO MOTOR
          #import_load_da              = ((import_load_da              ['coef_load_DA']-1)*100)
          #import_load_do              = ((import_load_do              ['coef_load_DO']-1)*100)
          #import_load_lucro           = ((import_load_lucro           ['coef_load_lucro']-1)*100)
          #import_load_impostos        = ((import_load_impostos        ['coef_load_impostos']-1)*100)
          #import_load_ibnr            = ((import_load_ibnr            ['coef_load_ibnr']-1)*100)
          #import_load_iof             = ((import_load_iof             ['coef_load_iof']-1)*100)
          #import_load_carregamentoSeg = ((import_load_carregamentoSeg ['coef_load_carregamento_seguranca']-1)*100)
          #import_load_comCorretor     = ((import_load_comCorretor     ['coef_load_comissao_corretor']-1)*100)
          #import_load_franquia        = ((import_load_franquia        ['coef_load_franquia']-1)*100)

          #import_load_da              = import_load_da.to_string(index=False) 
          #import_load_do              = import_load_do.to_string(index=False) 
          #import_load_lucro           = import_load_lucro.to_string(index=False) 
          #import_load_impostos        = import_load_impostos.to_string(index=False) 
          #import_load_ibnr            = import_load_ibnr.to_string(index=False) 
          #import_load_iof             = import_load_iof.to_string(index=False) 
          #import_load_carregamentoSeg = import_load_carregamentoSeg.to_string(index=False) 
          #import_load_comCorretor     = import_load_comCorretor.to_string(index=False) 
          #import_load_franquia        = import_load_franquia.to_string(index=False)

          #st.write("**Despesa Administrativa:**",      import_load_da,"%")
          #st.write("**Despesa Operacional:**",         import_load_do,"%")
          #st.write("**Lucro:**",                       import_load_lucro,"%")
          #st.write("**Impostos:**",                    import_load_impostos,"%")
          #st.write("**IBNR:**",                        import_load_ibnr,"%")
          #st.write("**IOF:**",                         import_load_iof,"%")
          #st.write("**Carregamento de Segurança:**",   import_load_carregamentoSeg,"%")
          #st.write("**Comissão do Corretor (FULL):**", import_load_comCorretor,"%")
          #st.write("**Franquia:**",                   import_load_franquia,"%")
