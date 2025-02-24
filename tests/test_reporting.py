import os
from app.services.reporting import log_command
from app.database.session import SessionLocal
from app.database.models import CommandLog

def test_log_command():
    db = SessionLocal()
    log_command("echo test", "test result", 0)
    log_entry = db.query(CommandLog).filter(CommandLog.command == "echo test").first()
    assert log_entry is not None
    assert log_entry.result == "test result"
    db.delete(log_entry)
    db.commit()
    db.close()