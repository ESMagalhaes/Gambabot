# Importando as bibliotecas necessárias
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from langchain_aws import ChatBedrockConverse
from langchain_classic.prompts import PromptTemplate

# Função para criar e interagir com o chatbot
def demo_chatbot():
    demo_llm = ChatBedrockConverse(
        model="us.amazon.nova-lite-v1:0",
        temperature=0.1,
        max_tokens=600,
        stop_sequences=["Human:", "User:", "AI:"],
        region_name="us-east-1"
    )
    return demo_llm

# Criação de uma função para o ConverssationBufferMemory
def demo_memory():
    # llm_data = demo_chatbot(),
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    return memory

# Criação da função para limpar repetições na conversa
def demo_clear_repeats(text):
    lines = text.splitlines()
    unique_lines = []
    for line in lines:
        line = line.strip()
        if line and line not in unique_lines:
            unique_lines.append(line)
    return "\n".join(unique_lines)

# Criação da função para o ConversationChain
def demo_chain(input_text, memory):
    # obtenha a instância do LLM (não uma tupla)
    llm_instance = demo_chatbot()
    
    prompt = PromptTemplate(
        input_variables=["chat_history", "input"],
        template=(
            "Você é um assistente educado e objetivo. "
            "Responda com clareza e sem repetir informações já ditas.\n\n"
            "Histórico da conversa:\n{chat_history}\n\n"
            "Pergunta do usuário:\n{input}\n\n"
            "Resposta:"
        )
    )
    
    llm_convo = ConversationChain(
        llm=llm_instance,
        memory=memory,
        prompt=prompt,
        verbose=False
    )
# Obtenção da resposta do chatbot
    chat_reply = llm_convo.predict(input=input_text)
    chat_reply_cleared = demo_clear_repeats(chat_reply)
    return chat_reply_cleared
