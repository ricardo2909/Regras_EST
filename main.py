import streamlit as st
from auth import login

# Função para adicionar o CSS customizado
def add_custom_css():
    st.markdown(
        """
        <style>
        .custom-title {
            font-size: 2em;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Função para verificar autenticação
def check_auth():
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

# Adicionar CSS customizado
add_custom_css()

# Verificar autenticação
check_auth()

if st.session_state.get('authenticated', False):  # Use get to avoid KeyError
    st.markdown('<p class="custom-title">Regras Gerais - EST</p>', unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")
    with st.expander("Como Selecionamos Ativos"):
        st.write("explicacao...")
    st.write("")
    with st.expander("Como Escolhemos Fundos"):
        st.write("explicacao...")
else:
    login()
