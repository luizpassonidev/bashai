
import subprocess
import os
import time
from faster_whisper import WhisperModel

ARQUIVO_AUDIO = "/home/passonidev/bashai/tests/audio_atual.wav"

print("Carregando o Whisper...")

modelo = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

print("Bash AI está escutando!")
print("Fale alguma coisa. Pressione Ctrl+C para sair.\n")

try:
    while True:
        comando = [
            "timeout", "5",
            "parecord",
            "--device=RDPSource",
            "--file-format=wav",
            ARQUIVO_AUDIO
        ]

        subprocess.run(
            comando,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if not os.path.exists(ARQUIVO_AUDIO):
            continue

        if os.path.getsize(ARQUIVO_AUDIO) < 10000:
            continue

        segmentos, info = modelo.transcribe(
            ARQUIVO_AUDIO,
            language="pt",
            vad_filter=True,
	    beam_size=5,
	    initial_prompt=(
		"Bash AI, Linux, terminal, Python, "
        "Firefox, listar arquivos, pasta atual, "
        "pwd, ls, cd, mkdir, sudo"
    )
        )

        texto = " ".join(
            segmento.text.strip()
            for segmento in segmentos
        ).strip()

        if texto:
            print(f"Você: {texto}")

        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nEscuta encerrada.")

