class Usuario:
  def __init__(self, email, senha):
    self.email = email
    self.senha = senha

  def autenticar(self, email, senha):
    if email == self.email:
      if senha == self.senha:
        print("\nSistema iniciado!\n")
        return True
      else: 
        print("\nSenha inválida!\n")
        return False
    else: 
      print("\nEmail inválido!\n")
      return False