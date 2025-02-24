from sqlalchemy import Column, Integer, String, DateTime
from database.session import Base
from datetime import datetime

class CommandLog(Base):
    __tablename__ = 'command_logs'
    __table_args__ = {'extend_existing': True}  

    id = Column(Integer, primary_key=True, index=True)
    command = Column(String, index=True)
    result = Column(String)
    status = Column(Integer)  # Status do comando (0 para sucesso, 1 para erro)
    timestamp = Column(DateTime, default=datetime.utcnow)  # Timestamp da execução
    source = Column(String)  # Origem do comando (local ou kali)