from database import Database
from config import db_config

from classes import Produto, Categoria, Fornecedor, Venda

class Container:
  def __init__(self):
    self.db = Database(
    host=db_config["host"],
    user=db_config["user"],
    password=db_config["password"],
    database=db_config["database"]
    ) 
    self.categoria = Categoria(self.db)
    self.fornecedor = Fornecedor(self.db)
    self.produto = Produto(self.db)
    self.venda = Venda(self.db)
  
  def conectar(self):
    return self.db.conectar()
  
  def fechar(self):
    self.db.fechar()

    