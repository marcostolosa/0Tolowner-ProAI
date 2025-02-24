from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Verifica se DATABASE_URL está definido, caso contrário usa um valor padrão
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:////app/data/database.db")

# Extrai o caminho do arquivo do banco de dados da URL
if DATABASE_URL.startswith('sqlite:///'):
    db_path = DATABASE_URL.replace('sqlite:///', '')
    
    # Cria o diretório se não existir
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    print(f"Diretório do banco de dados: {os.path.dirname(db_path)}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    """Inicializa o banco de dados."""
    print(f"Iniciando banco de dados em: {DATABASE_URL}")
    Base.metadata.create_all(bind=engine)
    print("Banco de dados inicializado com sucesso!")