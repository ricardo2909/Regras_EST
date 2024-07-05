import streamlit as st
from auth import login


# Função para verificar autenticação
def check_auth():
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

check_auth()

if st.session_state['authenticated']:

    st.title('Regras Gerais - EST')

    st.write("")
    st.write("")
    st.write("")
    with st.expander("Como Selecionamos Ativos"):
        st.write("explicacao...")

    with st.expander("Como Escolhemos Fundos"):
        st.write("explicacao...")
else:
    login()