def entrada_texto(mensagem : str) -> str:
  while True:
    valor = input(mensagem).strip()
    if valor:
      return valor
    print("Entrada inválida. O campo não pode estar vazio.")


def entrada_float(mensagem : str) -> float:
  while True:
    entrada = input(mensagem).replace(",", ".").strip()
    try:
      valor = float(entrada)
      if valor > 0:
        return valor
      print("Entrada inválida. Digite um número maior que 0.")
    except ValueError:
      print(f"Entrada inválida. Digite um número.")
  

def entrada_inteiro(mensagem : str) -> int:
  while True:
    try:
      valor = int(input(mensagem))
      if valor > 0:
        if isinstance (valor, int):
          return valor
      print("Entrada inválida.")        
    except ValueError:
      print("Entrada inválida.")