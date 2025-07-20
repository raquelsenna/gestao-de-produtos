from database import Database

class Categoria:
  def __init__(self, db):
    self.__db = db


  def cadastrar_Categoria(self, nome):
    try:
      query = """
      INSERT INTO categorias (nome)
      VALUES (%s)
      """

      valores = (nome,)
      
      self.__db.executar(query, valores)
      
      print("\nCategoria cadastrada com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao cadastrar categoria: {erro}")


  def listar_categoria(self):
    try:
      query = """
        SELECT * FROM categorias;
      """
      
      categorias = self.__db.buscar(query)
      
      if categorias:
        print("\n---Lista de Categorias---\n")
        for categoria in categorias:
          print(f"ID: {categoria[0]}, Nome: {categoria[1]}")
    
    except Database.mysql.connector.Error as erro:
      print(f"\nErro ao listar produtos: {erro}\n")


  def atualizar_categoria(self, id_categoria, nome):
    try:
      query = """
        UPDATE categorias
        SET nome = %s
        WHERE id_categoria = %s;
      """
      
      valores = (nome, id_categoria,)
      
      self.__db.execute(query, valores)
    
      print("\nCategoria atualizada com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao atualizar categoria: {erro}")


  def excluir_categoria(self, id_categoria):
    try:
      query = """
        DELETE FROM categorias 
        WHERE id_categoria = %s;
      """
      
      self.__db.executar(query, (id_categoria,))

      print("\nCategoria excluída com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao excluir categoria: {erro}")