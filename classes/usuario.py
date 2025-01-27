class Usuario:
  def __init__(self, email, senha):
    self.email = "ADMIN"
    self.senha = "admin123"

  def login(self, email, senha):
    if self.email == email:
      if self.senha == senha:
        return True
      else: 
        print("Senha inválida!")
    else: 
      print("Email inválido!")