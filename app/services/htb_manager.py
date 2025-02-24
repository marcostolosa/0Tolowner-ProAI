import requests
import os

HTB_API_URL = "https://api.hackthebox.com"

def start_machine(machine_name: str):
    """Inicia uma máquina no Hack The Box."""
    token = os.getenv("HTB_TOKEN")
    response = requests.post(f"{HTB_API_URL}/machines/{machine_name}/start", headers={"Authorization": f"Bearer {token}"})
    return response.json()