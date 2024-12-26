
import os
import dotenv
import streamlit as st

dotenv.load_dotenv()
token = os.environ['TOKEN_HF']

modelos = {
    'mistralai/Mixtral-8x7B-Instruct-v0.1': '[/INST]',
    'google/gemma-7b-it': '<start_of_turn>model\n',
}

modelo = st.selectbox('Selecione um modelo:', options=modelos)
token_modelo = modelos[modelo]


if 'modelo_atual' not in st.session_state:
    st.session_state['modelo_atual'] = modelo
    st.session_state['mensagens'] = []

area_chat = st.empty()
pergunta_usuario = st.chat_input('Faça sua pergunta:')