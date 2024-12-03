from database import Database

class Produto:
  def __init__(self, nome, valor, quantidade, idCategoria, idFornecedor):
    self.nome = nome
    self.valor = valor
    self.quantidade = quantidade
    self.idCategoria = idCategoria
    self.idFornecedor = idFornecedor
  
  def cadastrarProduto(self, conexao):
    try:
      cursor = conexao.cursor()
      query = """
      INSERT INTO produtos (nome, valor, quantidade, id_categoria, id_fornecedor)
      VALUES (%s, %s, %s, %s, %s)
      """

      valores = (self.nome, self.valor, self.quantidade, self.idCategoria, self.idFornecedor)

      cursor.execute(query, valores)

      conexao.commit()

      print("Produto cadastrado com sucesso!")

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao cadastrar produto: {erro}")
      
    finally:
      Database.fechar()

  def atualizarProduto():
    pass

  def atualizarQuantidade():
    pass