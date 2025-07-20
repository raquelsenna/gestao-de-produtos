from database import Database
from config import db_config

from classes import Produto, Categoria, Fornecedor, Venda

class Container:
  def __init__(self):
    self.__db = Database(
    host=db_config["host"],
    user=db_config["user"],
    password=db_config["password"],
    database=db_config["database"]
    ) 
    self.categoria = Categoria(self.__db)
    self.fornecedor = Fornecedor(self.__db)
    self.produto = Produto(self.__db)
    self.venda = Venda(self.__db)
  
  def conectar(self):
    return self.__db.conectar()
  
  
  def fechar(self):
    self.__db.fechar()