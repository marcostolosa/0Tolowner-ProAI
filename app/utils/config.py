import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações
HTB_TOKEN = os.getenv("HTB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")