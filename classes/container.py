from database import Database
from config import db_config
from classes import Produto, Categoria, Fornecedor, Venda

class Container:
  def __init__(self):
    self._db = Database(
    host=db_config["host"],
    user=db_config["user"],
    password=db_config["password"],
    database=db_config["database"]
    ) 
    self.categoria = Categoria(self._db)
    self.fornecedor = Fornecedor(self._db)
    self.produto = Produto(self._db)
    self.venda = Venda(self._db)

  def iniciar(self):
    return self._db.conectar()
  
  def fechar(self):
    return self._db.fechar()