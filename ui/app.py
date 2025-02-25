import streamlit as st
import requests

st.title("Tolowner ProAI")

# Inicializa uma lista para armazenar os resultados
output_log = []

# Função para adicionar output ao log
def add_to_log(text):
    output_log.append(text)
    # Limita o log a um tamanho máximo
    if len(output_log) > 100:  # Limite de 100 entradas
        output_log.pop(0)

# Executar Comando
st.header("Executar Comando")
command = st.text_input("Digite o comando:")
if st.button("Executar"):
    response = requests.post("http://app:8000/execute/", json={"command": command}) 
    if response.status_code == 200:
        result = response.json()
        output_text = f"**Resultado do comando:**\n```\n{result['result']}\n```"
        add_to_log(output_text)
    else:
        st.error(f"Erro: {response.status_code} - {response.text}")

# Executar Comando no Kali
st.header("Executar Comando no Kali")
kali_command = st.text_input("Digite o comando para Kali:")
if st.button("Executar no Kali"):
    response = requests.post("http://app:8000/kali/execute/", json={"command": kali_command}) 
    if response.status_code == 200:
        result = response.json()
        output_text = f"**Resultado do comando no Kali:**\n```\n{result['result']}\n```"
        add_to_log(output_text)
    else:
        st.error(f"Erro: {response.status_code} - {response.text}")

# Sugestão de Comando
st.header("Sugestão de Comando")
prompt = st.text_input("Digite o prompt para sugestão:")
if st.button("Sugerir"):
    response = requests.post("http://app:8000/suggest/", json={"prompt": prompt})  
    if response.status_code == 200:
        suggestion = response.json()
        output_text = f"**Sugestão do ChatGPT:**\n{suggestion['suggestion']}"
        st.markdown(output_text)
        add_to_log(output_text)
    else:
        st.error(f"Erro: {response.status_code} - {response.text}")

# Exibir o log de outputs
st.subheader("Log de Outputs")
for entry in output_log:
    st.markdown(entry)

# Opção para copiar o output
if st.button("Copiar Output"):
    output_to_copy = "\n".join(output_log)
    st.text_area("Output para copiar:", output_to_copy, height=200)

# Opção para salvar o output em um arquivo
if st.button("Salvar Output"):
    with open("output_log.txt", "w") as f:
        f.write("\n".join(output_log))
    st.success("Output salvo em output_log.txt")