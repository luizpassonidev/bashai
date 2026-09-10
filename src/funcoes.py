import subprocess
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
      comando, 
      capture_output=True,
      text=True)
  
  if resultado.returncode == 0:
    return resultado.stdout
  else:
    return resultado.stderr