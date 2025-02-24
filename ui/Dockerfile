# Dockerfile para a interface do usuário
FROM python:3.9

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da interface
COPY . .

# Expor a porta que o Streamlit irá rodar
EXPOSE 8501

# Comando para iniciar a interface do usuário
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]