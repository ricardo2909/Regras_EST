import streamlit as st
import time

def login():
    st.title("Login")

    # Verifica se a senha foi submetida
    if 'password_submitted' not in st.session_state:
        st.session_state['password_submitted'] = False

    # Campo de senha
    password = st.text_input("Senha", type="password", on_change=lambda: st.session_state.update(password_submitted=True))

    # Verifica se a senha foi submetida e processa o login
    if st.session_state['password_submitted']:
        if password == "estgp":
            st.session_state['authenticated'] = True
            st.experimental_rerun()  # Força a recarga da página
        else:
            st.session_state['password_submitted'] = False
            erro = st.error("Senha incorreta. Tente novamente.")
            time.sleep(2)
            erro.empty()
    
    # Botão de login para fallback, caso o usuário prefira clicar
    if st.button("Entrar"):
        if password == "estgp":
            st.session_state['authenticated'] = True
            st.experimental_rerun()  # Força a recarga da página
        else:
            st.error("Senha incorreta. Tente novamente.")

def logout():
    st.session_state['authenticated'] = False
    st.session_state['password_submitted'] = False 