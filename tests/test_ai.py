import pytest
from app.services.ai import generate_command_suggestion

@pytest.mark.asyncio
async def test_generate_command_suggestion():
    prompt = "Sugira um comando para listar arquivos."
    suggestion = await generate_command_suggestion(prompt)
    assert suggestion is not None
    assert "ls" in suggestion  # Verifica se a sugestão contém o comando 'ls'