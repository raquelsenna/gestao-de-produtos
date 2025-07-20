import mysql.connector
# from mysql.connector import Error

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
    cursor = self.conexao.cursor()
    print("cursor criado")
    print(f"Tipos dos valores: {[type(v) for v in valores]}")
    print("Valores:", valores)
    cursor.execute(query, valores) # ERRO
    print("query executada")
    self.conexao.commit()
    print("alteraçoes salvas")
    cursor.close()
    print("cursor fechado")


  def buscar(self, query, valores=None):
    cursor = self.conexao.cursor()
    cursor.execute(query, valores or ())
    resultados = cursor.fetchall() # fetchone sempre retorna uma tupla
    cursor.close()
    return resultados
      
  # encerra a conexão com banco de dados
  def fechar(self): 
    if self.conexao and self.conexao.is_connected:
      self.conexao.close()
      print("\nConexão com o banco de dados encerrada.")