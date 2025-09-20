import streamlit as st # type: ignore # -> para rodar o streamlit basta dar o comando: streamlit run (nome do arquivo) no bash, hopedamento local assim como Flask e etc...
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("env/.env")
modelo = OpenAI()

st.write("### Chatbot do Saulo") # -> Steamlist utiliza Markdown, similar com Obsidian

if not "lista_mensagem" in st.session_state: # -> verifica memoria do Streamlist, caso não haja mensagens na memoria ele cria uma lista de mensagens para adicionar no session state
    st.session_state["lista_mensagem"] = []

historic = st.session_state["lista_mensagem"] # armazenando historico das mensagens em uma variavel 

user_text = st.chat_input("Escreva sua mensagem") # input do usuario

if user_text: 
    st.chat_message("user").write(user_text) # -> para exibir no chat que a mensagens pertence ao usuario deve-se usar o "user", para a AI é "assistant"
    text = {"role": "user", "content": user_text} # salvando uma mensagem do usuario
    historic.append(text) # salvando mensagem do usuario no session state "lista de mensagens"


    model_response = modelo.chat.completions.create( # aqui a ai recebe o historico de mensagens para ver a pergunta dos usuarios 
        messages=historic,
        model="gpt-4o"
    )

    ai_response = model_response.choices[0].message.content #Aqui serve pra pegar a mensagem de Ai que é gerada pelo model response (a resposta esta no indice 0 dentro da lista content)

    st.chat_message("assistant").write(ai_response)
    ai_text = {"role": "assistant", "content": ai_response} #Nesse bloco de codigo inteiro serve pra armazenar a resposa da ai no historico de mensagens e monstrar ela na tela
    historic.append(ai_text)
    
for msg in historic:
    role = msg["role"]
    content = msg["content"]
    st.chat_message(role).write(content)

