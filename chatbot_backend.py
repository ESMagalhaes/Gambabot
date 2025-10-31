# Importando as bibliotecas necessárias
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from langchain_aws import ChatBedrockConverse

# Função para criar e interagir com o chatbot


def demo_chatbot():
    demo_llm = ChatBedrockConverse(
        #credentials_profile_name='default',
        model="amazon.titan-text-express-v1",
        temperature=0.1,
        max_tokens=512
    )
    return demo_llm

# Criação de uma função para o ConverssationBufferMemory


def demo_memory():
    # llm_data = demo_chatbot(),
    memory = ConversationBufferMemory()
    return memory

# Criação da função para o ConversationChain


def demo_chain(input_text, memory):
    # obtenha a instância do LLM (não uma tupla)
    llm_instance = demo_chatbot()
    llm_convo = ConversationChain(
        llm=llm_instance,
        memory=memory,
        verbose=True
    )
# Obtenção da resposta do chatbot
    chat_reply = llm_convo.predict(input=input_text)
    return chat_reply
