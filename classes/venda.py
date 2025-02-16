from database import Database

class Venda():
  def __init__(self, db):
    self.db = db

  
  def cadastrarVenda(self, data_venda, id_produto, quantidade, valor_unitario):
    try:
      cursor = self.db.conexao.cursor() 

      valor_total = valor_unitario * quantidade

      query = """
      INSERT INTO vendas (data_venda, id_produto, quantidade, valor_total)
      VALUES (%s, %s, %s, %s)
      """

      valores = (data_venda, id_produto, quantidade, valor_total,)
      
      cursor.execute(query, valores)
      self.db.conexao.commit()

      print("\nVenda cadastrada com sucesso!\n")

    except Exception as error:
      print(f"Erro ao cadastrar venda: {error}")
      return None

    finally:
      cursor.close()


  def listarVenda(self):
    try:
      cursor = self.db.conexao.cursor()

      query = """
      SELECT * FROM vendas
      """
      
      cursor.execute(query)
      vendas = cursor.fetchall()

      if vendas:
        print("\n---Lista de Vendas---\n")

        for venda in vendas:
          print(f"ID: {venda[0]}, Data: {venda[1]}, ID Produto: {venda[2]}, Quantidade: {venda[3]}, Valor Total: {venda[4]}")
    
    except Exception as erro:
      print(f"Erro ao listar vendas: {erro}")

    finally:
      if cursor:
        cursor.close()


  def atualizarVenda(self):
    pass


  def excluirVenda(self):
    pass