import requests

async def run_command_in_kali(command: str) -> str:
    """Executa um comando no contêiner do Kali Linux."""
    response = requests.post("http://kali:5000/execute", json={"command": command})  # Chama o servidor do Kali
    if response.status_code == 200:
        return response.json().get("result")
    else:
        return response.json().get("error")