class Usuario:
  def __init__(self, email, senha):
    self.__email = email
    self.__senha = senha

  def autenticar(self, email, senha):
    if email != self.__email:
        raise EmailInvalidoError("Email inválido")
    if senha != self.__senha:
        raise SenhaInvalidaError("Senha inválida")
    
    return "Login realizado com sucesso"
  
class EmailInvalidoError(Exception):
    pass

class SenhaInvalidaError(Exception):
    pass