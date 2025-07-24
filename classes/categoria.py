from database import Database
from erros.decoradores import gerenciar_conexao 

class Categoria:
  def __init__(self, db):
    self._db = db

  @gerenciar_conexao
  def cadastrar_categoria(self, nome):
    try:
      query = """
      INSERT INTO categorias (nome)
      VALUES (%s)
      """

      valores = (nome,)
      
      self._db.executar(query, valores)
      
      print("\nCategoria cadastrada com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao cadastrar categoria: {erro}")

  @gerenciar_conexao
  def listar_categoria(self):
    try:
      query = """
        SELECT * FROM categorias;
      """

      print("\nquerry criada\n")
      print("\niniciando busca\n")
      
      categorias = self._db.buscar(query)

      print("\nbusca executada\n")
      
      if categorias:
        print("\n---Lista de Categorias---\n")

        for categoria in categorias:
          print(f"ID: {categoria[0]}, Nome: {categoria[1]}")

      else: 
        print("Não há categorias.")

    except Exception as erro:
      print(f"Erro ao listar categoria: {erro}")

  @gerenciar_conexao
  def atualizar_categoria(self, id_categoria, nome):
    try:
      query = """
        UPDATE categorias
        SET nome = %s
        WHERE id_categoria = %s;
      """
      
      valores = (nome, id_categoria,)
      
      self._db.executar(query, valores)
    
      print("\nCategoria atualizada com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao atualizar categoria: {erro}")

  @gerenciar_conexao
  def excluir_categoria(self, id_categoria):
    try:
      query = """
        DELETE FROM categorias 
        WHERE id_categoria = %s;
      """
      
      self._db.executar(query, (id_categoria,))

      print("\nCategoria excluída com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao excluir categoria: {erro}")