import time
import os
from dotenv import load_dotenv
from google import genai

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
    model="gemini-3.5-flash-lite"
)
dec = 'n'
while dec!='y':
    msg = input("Bash AI: O que deseja Luiz?\nR:")
    while msg !="/sair":
        resp = chat.send_message(
            message= f"Bash AI:{msg}")
        print(f"Bash AI: {resp.text}")
        msg = input("Bash AI: Mais alguma dúvida luiz?\nR:")
    dec = input("Bash AI: Deseja encerrar nossa conversa? (y/n)\nR:")

