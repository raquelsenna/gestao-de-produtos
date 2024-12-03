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