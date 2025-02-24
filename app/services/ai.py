import openai
import os

# Configurar a chave da API
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_command_suggestion(prompt: str) -> str:
    """Gera uma sugestão de comando usando um modelo de linguagem."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']