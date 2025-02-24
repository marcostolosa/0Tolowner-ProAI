# Usar uma imagem base do Python
FROM python:3.9

# Definir o diretório de trabalho e permissões
WORKDIR /app
RUN mkdir -p /app/data && chmod -R 777 /app/data

# Copiar os arquivos de requisitos
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Adicionar o diretório /app ao PYTHONPATH
ENV PYTHONPATH=/app

# Expor a porta que a aplicação irá rodar
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]