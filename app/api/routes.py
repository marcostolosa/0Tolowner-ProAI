from fastapi import APIRouter
from services.executor import execute_command
from services.kali_manager import run_command_in_kali
from services.ai import generate_command_suggestion
from services.reporting import log_command

router = APIRouter()

@router.post("/execute/")
async def execute(command: str):
    result = await execute_command(command)
    log_command(command, result, 0, "local")
    return {"result": result}

@router.post("/kali/execute/")
async def execute_kali(command: str):
    result = await run_command_in_kali(command)
    log_command(command, result, 0, "kali")
    return {"result": result}

@router.post("/suggest/")
async def suggest(prompt: str):
    suggestion = await generate_command_suggestion(prompt)
    return {"suggestion": suggestion}