import subprocess
import subprocess
import os
import time
from faster_whisper import WhisperModel

def logo():
  bai = """
                    ``
                    :+.
                    :o+
                  . :++-
                  -- :+++-
                -++.:++++-
              .-+++:-++++++.
              .+++++--+++++++.
            .+-:-++--++++++++`
            `+-  `++--+++`.++++`
          :++...-++`-+++   -+++:
          -++++++++-.-+++:``:++++-
        .-o-....`+++--+++--+++++++-.
      .++-     .+++:-+++   .-+++++-.
      `-+-...``:+++-.`+++     -++++-:.
    :++++++++--::.    .`     `+++++++:
    -o++-:`.                    .`:-++o-
  .-:`.                              .`:-.

                  BASH AI                 
  \n"""

  print(bai)

def exec(comando):
  resultado = subprocess.run(
      comando,shell=True,
      capture_output=True,
      text=True)
  
  if resultado.returncode == 0:
    return resultado.stdout
  else:
    return resultado.stderr

def cmd_voz():
  path = "/home/passonidev/bashai/data/audio.wav"

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
              path
          ]

          subprocess.run(
              comando,
              stdout=subprocess.DEVNULL,
              stderr=subprocess.DEVNULL
          )

          if not os.path.exists(path):
              continue

          if os.path.getsize(path) < 10000:
              continue

          segmentos, info = modelo.transcribe(
              path,
              language="pt",
              vad_filter=True,
              beam_size=5,
              initial_prompt=(
          "Bash AI, Linux, terminal, Python, "
          "Firefox, listar arquivos, pasta atual, "
          "pwd, ls, cd, mkdir, sudo"
            )
          )

          textos = []

          for segmento in segmentos:
            textos.append(segmento.text.strip())

          texto = " ".join(textos)
          if texto:
              print(f"Você: {texto}")

          time.sleep(0.2)

  except KeyboardInterrupt:
      print("\nEscuta encerrada.")
  return texto