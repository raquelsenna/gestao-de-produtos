from database import Database

class Venda():
  def __init__(self, db):
    self.__db = db

  def cadastrar_venda(self, data_venda, id_produto, quantidade, valor_unitario):
    try:
      valor_total = valor_unitario * quantidade

      query = """
        INSERT INTO vendas (data_venda, id_produto, quantidade, valor_total)
        VALUES (%s, %s, %s, %s)
        """
      
      valores = (data_venda, id_produto, quantidade, valor_total,)
      
      self.__db.executar(query, valores)

      print("\nVenda cadastrada com sucesso!\n")

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao cadastrar venda: {erro}")


  def listar_venda(self):
    try:
      query = """
      SELECT * FROM vendas
      """
      
      vendas = self.__db.buscar(query)

      if vendas:
        print("\n---Lista de Vendas---\n")

        for venda in vendas:
          print(f"ID: {venda[0]}, Data: {venda[1]}, ID Produto: {venda[2]}, Quantidade: {venda[3]}, Valor Total: {venda[4]}")
    
    except Database.mysql.connector.Error as erro:
      print(f"Erro ao listar venda: {erro}")

