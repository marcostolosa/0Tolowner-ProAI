import pytest
from app.services.executor import execute_command

@pytest.mark.asyncio
async def test_execute_command():
    result = await execute_command("echo Hello, World!")
    assert result.strip() == "Hello, World!"

@pytest.mark.asyncio
async def test_execute_invalid_command():
    with pytest.raises(Exception):
        await execute_command("invalid_command")