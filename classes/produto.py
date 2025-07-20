from database import Database

class Produto:
  def __init__(self, db):
    self.db = db
  

  def consultarEstoque(self, id_produto, quantidade_venda):
    try:  
      query = """
        SELECT quantidade 
        FROM produtos
        WHERE id_produto = %s
        """    

      resultado = self.db.buscar(query, (id_produto,)) 

      if resultado is None:
        return False
      
      quantidade_estoque = resultado[0][0] # exemplo: resultado retorna [10,], ou seja, uma tupla, e resultado[0] retorna [10].
      quantidade_atualizada = quantidade_estoque - quantidade_venda

      if quantidade_atualizada < 0:
        return False 
      
      print("Tudo certo")
      return True 

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao consultar quantidade no estoque: {erro}")
        

  def buscarValor(self, id_produto):
    try:
      query = """
        SELECT valor 
        FROM produtos
        WHERE id_produto = %s
        """

      resultado = self.db.buscar(query, (id_produto,))

      if resultado:
        print(resultado[0][0])
        return resultado[0][0]

      return None
  
    except Database.mysql.connector.Error as erro:
      print(f"Erro ao cadastrar produto: {erro}")


  def atualizarEstoque(self, id_produto, quantidade_venda):
    try:
      query = """
        SELECT quantidade 
        FROM produtos
        WHERE id_produto = %s
        """

      resultado = self.db.buscar(query, (id_produto,))

      if resultado is None:
        print("Erro ao encontrar quantidade no estoque.")
        return

      quantidade_estoque = resultado[0][0]
      print(quantidade_estoque)
      quantidade_atualizada = quantidade_estoque - quantidade_venda

      query = f"""
        UPDATE produtos
        SET quantidade = %s
        WHERE id_produto = %s;
      """
      
      valores = (quantidade_atualizada, id_produto,)

      self.db.executar(query, valores)
      
      print("\nQuantidade no estoque atualizado com sucesso!")

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao atualizar quantidade no estoque: {erro}")
      

  def cadastrarProduto(self, nome, valor, quantidade, id_categoria, id_fornecedor):
    try:
      query = """
      INSERT INTO produtos (nome, valor, quantidade, id_categoria, id_fornecedor)
      VALUES (%s, %s, %s, %s, %s)
      """

      valores = (nome, valor, quantidade, id_categoria, id_fornecedor,)

      self.db.executar(query, valores)

      print("\nProduto cadastrado com sucesso!\n")

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao cadastrar produto: {erro}")


  def listarProduto(self):
    try:
      query = """
      SELECT * FROM produtos; 
      """

      produtos = self.db.buscar(query)
      
      if produtos:
        print("\n--Lista de Produtos--\n")

        for produto in produtos:
          print(f"ID: {produto[0]}, Nome: {produto[1]}, Valor: {produto[2]}, Quantidade: {produto[3]}, Id_categoria: {produto[4]}, Id_fornecedor: {produto[5]}\n")
        
      else: 
        print("Não há produtos.")

    except Database.mysql.connector.Error as erro:
      print(f"\nErro ao listar produtos: {erro}\n")


  def atualizarProduto(self, id_produto, nome, valor, quantidade, id_categoria, id_fornecedor):
    try:
      campos = []
      valores = []

      if nome:
        campos.append("nome = %s")
        valores.append(nome)

      if valor:
        campos.append("valor = %s")
        valores.append(valor)

      if quantidade:
        campos.append("quantidade = %s")
        valores.append(quantidade)

      if id_categoria:
        campos.append("id_categoria = %s")
        valores.append(id_categoria)

      if id_fornecedor:
        campos.append("id_fornecedor = %s")
        valores.append(id_fornecedor)

      query = f"""
        UPDATE produtos
        SET {", ".join(campos)}
        WHERE id_produto = %s;
      """
      
      valores.append(id_produto)

      self.db.executar(query, valores)
      
      print("\nProduto atualizado com sucesso!")

    except Exception as erro:
      print(f"Erro ao atualizar produto: {erro}")


  def excluirProduto(self, id_produto): 
    try:
      query = """
      DELETE FROM produtos
      WHERE id_produto = %s;
      """

      self.db.executar(query, (id_produto,))
      
      print("\nProduto excluído com sucesso!")
  
    except Database.mysql.connector.Error as erro:
      print(f"Erro ao excluir produto: {erro}")
