import time
import os
from dotenv import load_dotenv
from google import genai

personality = """
Você é o Bash AI, um assistente de inteligência artificial executado no terminal.

Seu nome é Bash AI.
Você responde sempre em português do Brasil.

Características:
- Seja amigável e natural.
- Seja objetivo, mas explique quando necessário.
- Quando explicar código, use exemplos simples e claros.
- Não invente informações. Quando não souber algo, diga que não sabe.
- Evite respostas excessivamente longas quando uma resposta curta for suficiente.
"""



#tela inicial
print("\t    Welcome to Bash AI!")
from funcoes import logo
logo()
time.sleep(2)

os.system("clear    ")



#carregar API
load_dotenv()
api=os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api)

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config={
        "system_instruction": personality
    }
)

#chat 
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
            aux +=1
        if msg == "/model":
            print("Bash AI: Utilizando o modelo Gemini 3.5 Flash-Lite")
            aux+=1
        if msg == "/help":
            print("Bash AI: Lista de Comandos do Bash AI:\n/help - Mostra Lista de comandos.\n/clear - Limpa a tela do Bash AI.\n/exit - Sai da conversa atual.\n/model - Mostra o modelo que o Bash AI está utilizando para gerar texto.")
            aux+=1
        if msg == "/new":
            os.system("clear")
            chat = client.chats.create(
                model="gemini-3.5-flash-lite",
                config={
                        "system_instruction": personality
                    }
            )
            flag = 0
            aux+=1
            continue
        if aux == 0:
            resp = chat.send_message(
                message= f"Bash AI:{msg}")
            print(f"Bash AI: {resp.text}")

    dec = input("Deseja encerrar nossa conversa? (y/n)\nR:").lower()
    while dec not in ("y", "n"):
        print("Opção inválida! Digite apenas y ou n.")
        dec = input("Deseja encerrar nossa conversa? (y/n)\nR:").lower()
    if dec == "y":
        break