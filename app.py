import streamlit as st
import pandas as pd
import plotly_express as px

# .\venv\Scripts\activate

st.title("Dashboard de Veículos à Venda")


car_data = pd.read_csv('vehicles.csv') # lendo os dados

# Inicializa o estado, se ainda não tiver sido inicializado
if 'show_hist' not in st.session_state:
    st.session_state.show_hist = False

hist_button = st.button('Criar histograma') # criar um botão
hist_options = ['odometer', 'price']
hist_color = {'odometer': 'blue', 'price': 'green'}

if hist_button:
    st.session_state.show_hist = True  # Muda o estado ao clicar

if st.session_state.show_hist: # se o botão for clicado
    st.header("Histograma")
    # st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    st.write('Escolha a coluna para visualizar o histograma')

    hist_option = st.selectbox("Escolha a variável para mostrar o histograma", hist_options, index=0)
    st.write(f'Criando um histograma para a coluna {hist_option}')

    # criar um histograma
    fig = px.histogram(car_data, x=hist_option, color_discrete_sequence=[hist_color[hist_option]])

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


build_scatter = st.checkbox('Criar um gráfico de dispersão')
numeric_columns = car_data.select_dtypes(include='number').columns.tolist()

if build_scatter: # se a caixa de seleção for selecionada
    st.header("Gráfico de Dispersão")

    st.write('Escolha as colunas para o gráfico de dispersão')

    x_axis = st.selectbox("Escolha a variável para o eixo X", numeric_columns, index=numeric_columns.index("odometer"))
    y_axis = st.selectbox("Escolha a variável para o eixo Y", numeric_columns, index=numeric_columns.index("price"))


    st.write(f'Criando um gráfico de dispersão entre "{x_axis}" e "{y_axis}"')

    fig2 = px.scatter(car_data, x=x_axis, y=y_axis, color_discrete_sequence=["green"], title=f"<b>Relação entre {x_axis} e {y_axis}</b>")
    
    st.plotly_chart(fig2, use_container_width=True)


build_bar_plot = st.checkbox('Criar um gráfico de barras: Preço médio de acordo com alguma coluna categórica')
x_axis_list = ['type', 'model', 'condition', 'cylinders', 'fuel', 'transmission', 'paint_color']

if build_bar_plot: # se a caixa de seleção para gráfico de barras for selecionada
    st.header("Gráfico de Barras")
    st.write("Escolha a coluna categoria para visualizar o preço médio")
    x_axis_bar = st.selectbox("Escolha a variável para o eixo X", x_axis_list, index=0)

    st.write(f'Gráfico de barras: Preço médio por "{x_axis_bar}"')

    df_agg = car_data[[x_axis_bar, 'price']].groupby(by=[x_axis_bar])['price'].mean().round(1).reset_index()
    ordens = df_agg.sort_values(by='price', ascending=False)[x_axis_bar]

    fig3 = px.bar(df_agg, x=x_axis_bar, y="price", color_discrete_sequence=["green"], title=f"<b>Preço médio por {x_axis_bar}</b>", category_orders={x_axis_bar: ordens})
    st.plotly_chart(fig3, use_container_width=True)







