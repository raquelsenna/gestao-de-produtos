from database import Database
from erros.decoradores import gerenciar_conexao 

class Produto:
  def __init__(self, db):
    self._db = db


  @gerenciar_conexao
  def __buscar_estoque(self, id_produto): # encapsulado
    query = """
        SELECT quantidade 
        FROM produtos
        WHERE id_produto = %s
        """    
        
    resultado = self._db.buscar(query, (id_produto,)) 

    if not resultado:
      return None

  def __buscar_estoque(self, id_produto):
    query = """
      SELECT quantidade 
      FROM produtos
      WHERE id_produto = %s
      """    
        
    resultado = self._db.buscar(query, (id_produto,)) 

    if resultado is None:
      return False

    print(resultado[0][0])
    return resultado[0][0] # exemplo: resultado retorna [10,], ou seja, uma tupla, e resultado[0] retorna [10].

  @gerenciar_conexao
  def __buscar_valor(self, id_produto): # encapsulado
    try:
      query = """
        SELECT valor 
        FROM produtos
        WHERE id_produto = %s
        """

      resultado = self._db.buscar(query, (id_produto,))

      if resultado:
        return resultado[0][0]

      return None
  
    except Database.mysql.connector.Error as erro:
      print(f"Erro ao cadastrar produto: {erro}")


  def pegar_valor(self, id_produto):
    return self.__buscar_valor(id_produto)


  def consultar_estoque(self, id_produto, quantidade):
    try:
      quantidade_estoque = self.__buscar_estoque(id_produto)
      quantidade_simulada = quantidade_estoque - quantidade

      if quantidade_simulada < 0:
        return False 
        
      return True 

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao consultar quantidade no estoque: {erro}")

  @gerenciar_conexao
  def atualizar_estoque(self, id_produto, quantidade):
    try:
      query = f"""
        UPDATE produtos
        SET quantidade = %s
        WHERE id_produto = %s;
      """
      
      quantidade_estoque = self.__buscar_estoque(id_produto)
      quantidade_atualizada = quantidade_estoque - quantidade

      valores = (quantidade_atualizada, id_produto,)

      self._db.executar(query, valores)
      
      print("\nEstoque atualizado com sucesso!")

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao atualizar quantidade no estoque: {erro}")
      
  @gerenciar_conexao
  def cadastrar_produto(self, nome, valor, quantidade, id_categoria, id_fornecedor):
    try:
      query = """
      INSERT INTO produtos (nome, valor, quantidade, id_categoria, id_fornecedor)
      VALUES (%s, %s, %s, %s, %s)
      """

      valores = (nome, valor, quantidade, id_categoria, id_fornecedor,)

      self._db.executar(query, valores)

      print("\nProduto cadastrado com sucesso!\n")

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao cadastrar produto: {erro}")

  @gerenciar_conexao
  def listar_produto(self):
    try:
      query = """
      SELECT * FROM produtos; 
      """

      produtos = self._db.buscar(query)
      
      if produtos:
        print("\n--Lista de Produtos--\n")

        for produto in produtos:
          print(f"ID: {produto[0]}, Nome: {produto[1]}, Valor: {produto[2]}, Quantidade: {produto[3]}, Id_categoria: {produto[4]}, Id_fornecedor: {produto[5]}\n")
        
      else: 
        print("Não há produtos.")

    except Database.mysql.connector.Error as erro:
      print(f"\nErro ao listar produtos: {erro}\n")

  @gerenciar_conexao
  def atualizar_produto(self, id_produto, nome, valor, quantidade, id_categoria, id_fornecedor):
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

      self._db.executar(query, valores)
      
      print("\nProduto atualizado com sucesso!")

    except Exception as erro:
      print(f"Erro ao atualizar produto: {erro}")

  @gerenciar_conexao
  def excluir_produto(self, id_produto): 
    try:
      query = """
      DELETE FROM produtos
      WHERE id_produto = %s;
      """

      self._db.executar(query, (id_produto,))
      
      print("\nProduto excluído com sucesso!")
  
    except Database.mysql.connector.Error as erro:
      print(f"Erro ao excluir produto: {erro}")