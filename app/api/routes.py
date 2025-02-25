from fastapi import APIRouter
from pydantic import BaseModel
from services.executor import execute_command
from services.kali_manager import run_command_in_kali
from services.ai import generate_command_suggestion
from services.reporting import log_command

router = APIRouter()

class CommandRequest(BaseModel):
    command: str

class SuggestionRequest(BaseModel):
    prompt: str

@router.post("/execute/")
async def execute(request: CommandRequest):
    result = await execute_command(request.command)
    log_command(request.command, result, 0, "local")
    return {"result": result}

@router.post("/kali/execute/")
async def execute_kali(request: CommandRequest):
    result = await run_command_in_kali(request.command)
    log_command(request.command, result, 0, "kali")
    return {"result": result}

@router.post("/suggest/")
async def suggest(request: SuggestionRequest):
    suggestion = await generate_command_suggestion(request.prompt)
    return {"suggestion": suggestion}