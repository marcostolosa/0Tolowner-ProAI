import streamlit as st
import requests

st.title("Tolowner ProAI")

# Executar Comando
st.header("Executar Comando")
command = st.text_input("Digite o comando:")
if st.button("Executar"):
    response = requests.post("http://localhost:8000/execute/", json={"command": command})
    result = response.json()
    st.write("Resultado:", result)

# Executar Comando no Kali
st.header("Executar Comando no Kali")
kali_command = st.text_input("Digite o comando para Kali:")
if st.button("Executar no Kali"):
    response = requests.post("http://localhost:8000/kali/execute/", json={"command": kali_command})
    result = response.json()
    st.write("Resultado:", result)

# Sugestão de Comando
st.header("Sugestão de Comando")
prompt = st.text_input("Digite o prompt para sugestão:")
if st.button("Sugerir"):
    response = requests.post("http://localhost:8000/suggest/", json={"prompt": prompt})
    suggestion = response.json()
    st.write("Sugestão:", suggestion)