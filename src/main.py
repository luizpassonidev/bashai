import time
import os
from dotenv import load_dotenv
from groq import Groq

personality = """
Você é o Bash AI, um assistente de inteligência artificial executado no terminal.
Você responde sempre em português do Brasil.
Seja objetivo, mas explique quando necessário.
"""


# tela inicial
print("\t    Welcome to Bash AI!")
from funcoes import logo
logo()
time.sleep(2)

os.system("clear    ")


# carregar API
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

#personalidade
messages = [
    {
        "role": "system",
        "content": personality
    }
]


# chat
flag = 0
while True:
    while True:
        aux = 0

        if flag == 0:
            msg = input("Bash AI: O que deseja Luiz?\nR:")
            flag += 1
        else:
            msg = input("Bash AI: Mais alguma dúvida luiz?\nR:")

        if msg == "/exit":
            break

        if msg == "/clear":
            os.system("clear")
            aux += 1

        if msg == "/model":
            print("Bash AI: Utilizando o modelo Llama 3.1 8B Instant")
            aux += 1

        if msg == "/help":
            print("Bash AI: Lista de Comandos do Bash AI:\n/help - Mostra Lista de comandos.\n/clear - Limpa a tela do Bash AI.\n/exit - Sai da conversa atual.\n/model - Mostra o modelo que o Bash AI está utilizando para gerar texto.")
            aux += 1

        if msg == "/new":
            os.system("clear")

            messages = [
                {
                    "role": "system",
                    "content": personality
                }
            ]

            flag = 0
            aux += 1
            continue

        if aux == 0:

            messages.append({
                "role": "user",
                "content": msg
            })

            # chat com stream
            stream = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=messages,
                stream=True
            )

            resposta = ""
            print("Bash AI:", end="", flush=True)
            for chunk in stream:
                texto = chunk.choices[0].delta.content
                if texto:
                    print(texto, end="", flush=True)
                    resposta += texto
            print()
            messages.append({
                "role": "assistant",
                "content": resposta
            })
    dec = input("Deseja encerrar nossa conversa? (y/n)\nR:").lower()
    while dec not in ("y", "n"):
        print("Opção inválida! Digite apenas y ou n.")
        dec = input("Deseja encerrar nossa conversa? (y/n)\nR:").lower()
    if dec == "y":
        break