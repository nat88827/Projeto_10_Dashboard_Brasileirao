import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')

df=pd.read_csv('Tabela_Clubes.csv')

Temporadas= sorted(df['Ano'].unique().tolist())

anos= st.sidebar.multiselect('Temporadas',Temporadas,Temporadas)

df=df[df['Ano'].apply(lambda x:x in anos)]

with st.container():
    col1, col2, col3, col4= st.columns(4)

    with col1:
        with st.container(border=True, height= "stretch"):
            st.metric('QTD Vitórias',df['Vitorias'].sum())

    with col2:
        with st.container(border=True, height= "stretch"):
            st.metric ('QTD Derrotas',df['Derrotas'].sum())       

    with col3:
        with st.container(border=True, height= "stretch"):
            st.metric ('QTD Empates',df['Empates'].sum())

    with col4:
        with st.container(border=True, height= "stretch"):
            st.metric ('QTD Estrangeiros',df['Estrangeiros'].sum())



with st.container():
    col1, col2= st.columns(2)

    with col1:
        with st.container(height= "stretch"):    
            podio=df[(df['Pos.']==1) | (df['Pos.']==2) | (df['Pos.']==3)].sort_values(['Ano','Pos.']).reset_index()
            podio=podio[['Ano', 'Clubes', 'Pos.']]
            st.subheader('Podio')
            st.table(podio)

    with col2:
        with st.container(height= "stretch"):


            df_aux=df.groupby("Ano")['Valor_total'].sum().reset_index()
            fig= px.line(df_aux, x= 'Ano', y='Valor_total', title= 'Valor Total de Clubes por Ano', markers= True)
            st.plotly_chart(fig)

            df_aux= df.groupby('Clubes')['Qtd_Jogadores'].sum().reset_index().sort_values('Qtd_Jogadores', ascending=False)
            fig=px.bar(df_aux, x= 'Clubes', y='Qtd_Jogadores', title= 'Quantidade de Jogadores por Time')
            st.plotly_chart(fig)