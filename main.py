import streamlit as st # -> para rodar o streamlit basta dar o comando: streamlit run (nome do arquivo) no bash, hopedamento local assim como Flask e etc...

st.write("### Chatbot do Saulinho") # -> Steamlist utiliza Markdown, similar com Obsidian

if not "lista_mensagem" in st.session_state: # -> verifica memoria do Streamlist, caso não haja mensagens na memoria ele cria uma lista de mensagens para adicionar no session state
    st.session_state["lista_mensagem"] = []

user_text = st.chat_input("Escreva sua mensagem") # input do usuario

for msg in st.session_state["lista_mensagem"]:
    role = msg["role"]
    historic_text = msg["content"]
    st.chat_message(role).write(historic_text)

if user_text: 
    st.chat_message("user").write(user_text) # -> para exibir no chat que a mensagens pertence ao usuario deve-se usar o "user", para a AI é "assistant"
    text = {"role": "user", "content": user_text} # salvando uma mensagem do usuario
    st.session_state["lista_mensagem"].append(text) # salvando mensagem do usuario no session state "lista de mensagens"
    

