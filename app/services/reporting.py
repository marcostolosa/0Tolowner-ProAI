from database.session import SessionLocal
from database.models import CommandLog
from datetime import datetime

def log_command(command: str, result: str, status: int, source: str):
    """Registra um comando e seu resultado no banco de dados."""
    db = SessionLocal()
    log_entry = CommandLog(
        command=command,
        result=result,
        status=status,
        timestamp=datetime.utcnow(),
        source=source  # Adiciona a origem do comando (ex: 'local' ou 'kali')
    )
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    db.close()