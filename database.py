import mysql.connector
from mysql.connector import Error

class Database:
  def __init__(self, host, user, password, database):
    self.host = host
    self.user = user
    self.password = password
    self.database = database
    self.conexao = None

  # conexão com banco de dados
  def conectar(self):
    try: 
      self.conexao = mysql.connector.connect(  
      host=self.host,
      user=self.user,
      password=self.password,
      database=self.database
      )
      
      if self.conexao.is_connected(): # confirma se a conexão foi bem sucedida
        print("Conexão com o banco de dados estabelecida com sucesso!")
        return True
  
    except mysql.connector.Error as err:
      print(f"Erro ao conectar ao banco de dados: {err}")
      return False

  # Confirma as alterações no banco de dados
  def commit(self):
    if self.conexao:
      self.conexao.commit()
      print("Alterações confirmadas no banco de dados.")
      
  # encerra a conexão com banco de dados
  def fechar(self): 
    if self.conexao and self.conexao.is_connected:
      self.conexao.close()
      print("Conexão com o banco de dados encerrada.")