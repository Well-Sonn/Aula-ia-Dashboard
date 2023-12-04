import streamlit as st
import pandas as pd
import plotly.express as px
import pathlib

css_code = pathlib.Path("style.css").read_text()

df = pd.read_csv("BancodeDadosA3_2023.csv", sep=",", decimal=",")

st.set_page_config(layout='wide')
st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)

st.markdown('<div class="header">Análise de Diagnósticos </div>', unsafe_allow_html=True)

col2, col3, col1 = st.columns(3)

col1.markdown("**Quantidade de pacientes por diagnóstico**")
counts = df['Diagnóstico'].value_counts()
df_counts = pd.DataFrame({'Diagnóstico': counts.index, 'Quantidade': counts.values})
df_counts = df_counts.sort_values('Quantidade')  # Ordenar do menor para o maior
fig_bar = px.bar(df_counts, y='Diagnóstico', x='Quantidade', labels={'Diagnóstico': 'Diagnóstico', 'Quantidade': 'Quantidade'})
col1.plotly_chart(fig_bar, use_container_width=True)

st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
st.write("\n")
st.write("\n")

col2.markdown("**Distribuição das métricas por diagnóstico**")
col_parameter = col2.selectbox("Escolha a coluna para análise:", df.columns)
fig_scatter = px.scatter(df, x=col_parameter, y='Diagnóstico', color='Diagnóstico' )
fig_scatter.update_layout(showlegend=False)
col2.plotly_chart(fig_scatter, use_container_width=True)

# Histograma
col3.markdown("**Distribuição por histograma**")
fig_hist = px.histogram(df, x=col_parameter, nbins=15)
col3.plotly_chart(fig_hist, use_container_width=True)

col4, graf = st.columns([1, 1.5])

# Gráfico de dispersão 
col4.markdown("**Relação entre Covariáveis (Gráfico de dispersão)**")
x_variable = col4.selectbox("Escolha a variável para o eixo X:", df.columns, key='x_variable')
y_variable = col4.selectbox("Escolha a variável para o eixo Y:", df.columns, key='y_variable')
fig_scatter_2 = px.scatter(data_frame=df, x=x_variable, y=y_variable)
col4.plotly_chart(fig_scatter_2, use_container_width=True)

graf.markdown("**Tabela de Dados**")
diagnosis_options = df['Diagnóstico'].unique()
filter_table = graf.selectbox("Escolha o diagnóstico para análise:", diagnosis_options)
filtered_df = df.loc[df['Diagnóstico'] == filter_table]
graf.dataframe(filtered_df.head(5), height=350)

if len(filtered_df) > 5:
    graf.markdown(f"*Mostrando apenas 5 de {len(filtered_df)} linhas. Utilize a barra de rolagem para ver mais.*")
