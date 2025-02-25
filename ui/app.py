import streamlit as st
import requests

st.title("Tolowner ProAI")

# Executar Comando
st.header("Executar Comando")
command = st.text_input("Digite o comando:")
if st.button("Executar"):
    response = requests.post("http://app:8000/execute/", json={"command": command})  # Alterado para 'app'
    if response.status_code == 200:
        result = response.json()
        st.write("Resultado:", result)
    else:
        st.error(f"Erro: {response.status_code} - {response.text}")

# Executar Comando no Kali
st.header("Executar Comando no Kali")
kali_command = st.text_input("Digite o comando para Kali:")
if st.button("Executar no Kali"):
    response = requests.post("http://app:8000/kali/execute/", json={"command": kali_command})  # Alterado para 'app'
    if response.status_code == 200:
        result = response.json()
        st.write("Resultado:", result)
    else:
        st.error(f"Erro: {response.status_code} - {response.text}")

# Sugestão de Comando
st.header("Sugestão de Comando")
prompt = st.text_input("Digite o prompt para sugestão:")
if st.button("Sugerir"):
    response = requests.post("http://app:8000/suggest/", json={"prompt": prompt})  # Alterado para 'app'
    if response.status_code == 200:
        suggestion = response.json()
        st.write("Sugestão:", suggestion)
    else:
        st.error(f"Erro: {response.status_code} - {response.text}")