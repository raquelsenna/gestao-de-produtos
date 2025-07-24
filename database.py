import mysql.connector

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
        return True
  
    except mysql.connector.Error as err:
      print(f"\nErro ao conectar ao banco de dados: {err}")
      return False


  def executar(self, query, valores):
    try:
      cursor = self.conexao.cursor()
      cursor.execute(query, valores) 
      self.conexao.commit()

    except mysql.connector.Error as err:
      print(f"\nErro ao executar query: {err}")

    finally:
      cursor.close()


  def buscar(self, query, valores=None):
    try:
      cursor = self.conexao.cursor()
      cursor.execute(query, valores or None)
      resultados = cursor.fetchall() # fetchall sempre retorna uma tupla
      return resultados
    
    except mysql.connector.Error as err:
      print(f"\nErro ao executar query: {err}")
      
    finally:
      cursor.close()
      
  # encerra a conexão com banco de dados
  def fechar(self): 
    if self.conexao and self.conexao.is_connected():
      self.conexao.close()
      print("\nConexão com o banco de dados encerrada.")