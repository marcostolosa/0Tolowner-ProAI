# Usar a imagem base do Kali Linux
FROM kalilinux/kali-rolling

# Atualizar o sistema e instalar o Python e Flask
RUN apt-get update && apt-get install -y python3 python3-pip python3-flask

# Copiar o servidor para o contêiner
COPY server.py /kali/server.py

# Expor a porta que o servidor Flask irá usar
EXPOSE 5000

# Comando para iniciar o servidor Flask
CMD ["python3", "/kali/server.py"]