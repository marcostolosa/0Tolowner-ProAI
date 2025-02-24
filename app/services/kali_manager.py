import subprocess

async def run_command_in_kali(command: str) -> str:
    """Executa um comando no contêiner do Kali Linux."""
    process = subprocess.Popen(
        ["docker", "exec", "-it", "kali_container_name", "bash", "-c", command],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return stdout.decode() if process.returncode == 0 else stderr.decode()