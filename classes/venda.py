from classes.produto import Produto

class Venda(Produto):
  def __init__(self, db):
    self.db = db 
  
  def valorTotal(self, id_produto, quantidade):
    try:
      cursor = self.db.conexao.cursor()

      query = """
      SELECT valor 
      FROM produtos
      WHERE id_produto = %s
      """

      cursor.execute(query, (id_produto,))
      result = cursor.fetchone()

      if not result:
        raise ValueError(f"Produto com ID {id_produto} não encontrado.")

      valor_produto = result[0]

      return quantidade * valor_produto
    
    except Exception as e:
      print(f"Erro ao calcular o valor total: {e}")
      return None

    finally:
      cursor.close()


def atualizarQuantidade(self, id_produto, quantidade):
    try:
      if self.db.conecar:
        produto = Produto()

      cursor = self.db.conexao.cursor()

      query = """
      SELECET quantidade 
      FROM produto 
      WHERE id_produto = %s"""

      cursor.execute(query, (id_produto,))

      result = cursor.fetchone()

      if not result:
        raise ValueError(f"Produto com ID {id_produto} não encontrado.")

      atualização_estoque = quantidade - self.quantidade
      
      if quantidade < 0:
        print("Estoque indisponível!")
      else:
        produto.atualizarProduto(atualização_estoque)


  def cadastrarVenda(self, data_venda, id_produto, quantidade):
    try:
      cursor = self.db.conexao.cursor()

      valor_total = self.valorTotal(id_produto, quantidade)

      if valor_total is None:
            raise ValueError("Erro ao calcular o valor total.")

      query = """
      INSERT INTO vendas(data_venda, id_produto, quantidade, valor_total)
      VALUES (%s, %s, %s, %s)
      """

      valores = (data_venda, id_produto, quantidade, valor_total,)
      cursor.execute(query, valores)
      self.db.conexao.commit()
      print("\nVenda cadastrada com sucesso!")

    except Exception as erro:
      print(f"Erro ao cadastrar venda: {erro}")
      
    finally:
      if cursor:
        cursor.close()


  


  def listarVenda(self):
    pass

  def atualizarVenda(self):
    pass

  def excluirrVenda(self):
    pass