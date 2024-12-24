class Categoria:
  def __init__(self, db):
    self.db = db

  def cadastrarCategoria(self, nome):
    try:
      cursor = self.db.conexao.cursor() #criação do cursor

      query = """
      INSERT INTO categorias (nome)
      VALUES (%s)
      """

      valores = (nome,)
      
      cursor.execute(query, valores)
      self.db.conexao.commit()
      print("\nCategoria cadastrada com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao cadastrar categoria: {erro}")
      
    finally:
      if cursor:
        cursor.close()

  def listarCategoria(self):
    try:
      cursor = self.db.conexao.cursor()

      query = """
        SELECT * FROM categorias;
      """
      
      cursor.execute(query)
      categorias = cursor.fetchall()
      
      if categorias:
        print("---Lista de Categorias---")
        for categoria in categorias:
          print(f"ID: {categoria[0]}, Nome: {categoria[1]}")

    finally:
      if cursor:
        cursor.close()


  def atualizarCategoria(self, id_categoria, nome):
    try:
      cursor = self.db.conexao.cursor()

      query = """
        UPDATE categorias
        SET nome = %s
        WHERE id_categoria = %s;
      """
      
      valores = (nome, id_categoria,)
      cursor.execute(query, valores)
      self.db.conexao.commit()
      print("\nCategoria atualizada com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao atualizar categoria: {erro}")

    finally:
      if cursor:
        cursor.close()

  def excluirCategoria(self, id_categoria):
    try:
      cursor = self.db.conexao.cursor()

      query = """
        DELETE FROM categorias 
        WHERE id_categoria = %s;
      """
      
      valores = (id_categoria,)
      cursor.execute(query, valores)
      self.db.conexao.commit()
      print("\nCategoria excluída com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao excluir categoria: {erro}")

    finally:
      if cursor:
        cursor.close()

