# Importando o streamlit e chatbot
import streamlit as st
import chatbot_backend as cb  # Importando o backend do chatbot

# Configuração da página do Streamlit
st.set_page_config(page_title="GambáBot", page_icon="🦨")  # Cabeçalho
st.title("GambáBot 🦨")  # Título da aplicação

# Memória do Langchain para o cachê da sessão
if 'memory' not in st.session_state:
    st.session_state.memory = cb.demo_memory()
    
# Adiciona o histórico da conversa ao cache da sessão
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    
# Renderização do histórico da conversa
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])
    
# Envio de detalhes para o input do usuário
input_text = st.chat_input("Faça sua pergunta ao GambáBot...")
if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)
        
    st.session_state.chat_history.append({"role": "user", "text": input_text})
    
    chat_response = cb.demo_chain(input_text=input_text, memory=st.session_state.memory)
    
    with st.chat_message("assistant"):
        st.markdown(chat_response)
    
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})
