import subprocess

async def execute_command(command: str) -> str:
    """Executa um comando no shell e retorna o resultado."""
    process = subprocess.Popen(
        command, 
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    return stdout.decode() if process.returncode == 0 else stderr.decode()