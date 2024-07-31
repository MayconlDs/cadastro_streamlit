import streamlit as st
from db import cadastrar_usuario, consultar_usuario

st.title('Crude de Aplicação')

menu = st.sidebar.title('Menu')
menu = st.sidebar.selectbox('Selecione uma opção', ['Cadastrar nome', 'Consultar nome'])

if menu == 'Cadastrar nome':
    nome = st.text_input(label='Nome', placeholder='Digite o nome a ser cadastrado')
    idade = st.text_input(label='Idade', placeholder='Digite a idade')

    if st.button('Cadastrar'):
        if nome and idade.isdigit():
            cadastrar_usuario(nome, int(idade))
            st.success('Usuário cadastrado com sucesso!')
        else:
            st.error('Por favor, insira um nome válido e uma idade numérica.')

elif menu == 'Consultar nome':
    nome = st.text_input(label='Nome', placeholder='Digite o nome a ser consultado')

    if st.button('Consultar'):
        resultado = consultar_usuario(nome)
        if resultado:
            st.write(f'Nome: {resultado[1]}')
            st.write(f'Idade: {resultado[2]}')
        else:
            st.error('Usuário não encontrado.')
