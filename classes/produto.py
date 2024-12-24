from database import Database

class Produto:
  def __init__(self, db):
    self.db = db
  
  def cadastrarProduto(self, nome, valor, quantidade, idCategoria, idFornecedor):
    try:
      cursor = self.db.conexao.cursor()

      query = """
      INSERT INTO produtos (nome, valor, quantidade, id_categoria, id_fornecedor)
      VALUES (%s, %s, %s, %s, %s)
      """

      valores = (nome, valor, quantidade, idCategoria, idFornecedor,)

      cursor.execute(query, valores)
      self.db.conexao.commit()

      print("\nProduto cadastrado com sucesso!\n")

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao cadastrar produto: {erro}")
      
    finally:
      if cursor:
        cursor.close()

  def atualizarProduto():
    pass

  def atualizarQuantidade():
    pass