
from faster_whisper import WhisperModel

print("Carregando o Whisper...")

modelo = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Transcrevendo o áudio...")

segmentos, info = modelo.transcribe(
    "/home/passonidev/bashai/tests/teste_microfone.wav",
    language="pt",
    vad_filter=True
)

for segmento in segmentos:
    print(segmento.text)

