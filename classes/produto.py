from database import Database

class Produto:
  def __init__(self, db):
    self.db = db
  

  def consultarEstoque(self, id_produto, quantidade_venda):
    try:
      cursor = self.db.conexao.cursor()
      
      query = """
        SELECT quantidade 
        FROM produtos
        WHERE id_produto = %s
        """

      cursor.execute(query, (id_produto,))

      resultado = cursor.fetchone() # fetchone sempre retorna uma tupla

      if resultado is None:
        print("Erro ao encontrar quantidade")
        return False
      
      quantidade_estoque = resultado[0] # exemplo: resultado retorna [10,], ou seja, uma tupla, e resultado[0] retorna [10].
      quantidade_atualizada = quantidade_estoque - quantidade_venda

      if quantidade_atualizada < 0:
        return False
      
      return True

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao consultar quantidade no estoque: {erro}")
        
    finally:
      if cursor:
        cursor.close()


  def buscarValor(self, id_produto):
    try:
      cursor = self.db.conexao.cursor()
      
      query = """
        SELECT valor 
        FROM produtos
        WHERE id_produto = %s
        """

      cursor.execute(query, (id_produto,))
      valor = cursor.fetchone()
      cursor.close()

      return valor[0] if valor else 0 
  
    except Database.mysql.connector.Error as erro:
      print(f"Erro ao cadastrar produto: {erro}")
        
    finally:
      if cursor:
        cursor.close()


  def atualizarEstoque(self, id_produto, quantidade_venda):
    try:
      cursor = self.db.conexao.cursor()
      
      query = """
        SELECT quantidade 
        FROM produtos
        WHERE id_produto = %s
        """

      cursor.execute(query, (id_produto,))

      resultado = cursor.fetchone()

      if resultado is None:
        print("Erro ao encontrar quantidade no estoque.")
        return

      quantidade_estoque = resultado[0]
      quantidade_atualizada = quantidade_estoque - quantidade_venda

      query = f"""
        UPDATE produtos
        SET quantidade = %s
        WHERE id_produto = %s;
      """
      
      valores = (quantidade_atualizada, id_produto)

      cursor.execute(query, valores)
      self.db.conexao.commit()
      print("\nQuantidade no estoque atualizado com sucesso!")

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao atualizar quantidade no estoque: {erro}")
      
    finally:
      if cursor:
        cursor.close()


  def cadastrarProduto(self, nome, valor, quantidade, id_categoria, id_fornecedor):
    try:
      cursor = self.db.conexao.cursor()

      query = """
      INSERT INTO produtos (nome, valor, quantidade, id_categoria, id_fornecedor)
      VALUES (%s, %s, %s, %s, %s)
      """

      valores = (nome, valor, quantidade, id_categoria, id_fornecedor,)

      cursor.execute(query, valores)
      self.db.conexao.commit()

      print("\nProduto cadastrado com sucesso!\n")

    except Database.mysql.connector.Error as erro:
      print(f"Erro ao cadastrar produto: {erro}")
      
    finally:
      if cursor:
        cursor.close()


  def listarProduto(self):
    try:
      cursor = self.db.conexao.cursor()
      
      query = """
      SELECT * FROM produtos; 
      """

      cursor.execute(query)
      produtos = cursor.fetchall()

      if produtos:
        print("\n--Lista de Produtos--\n")

        for produto in produtos:
          print(f"ID: {produto[0]}, Nome: {produto[1]}, Valor: {produto[2]}, Quantidade: {produto[3]}, Id_categoria: {produto[4]}, Id_fornecedor: {produto[5]}\n")
      
      else: 
        print("Não há produtos.")

    except Database.mysql.connector.Error as erro:
      print(f"\nErro ao cadastrar produto: {erro}\n")
      
    finally:
      if cursor:
        cursor.close()


  def atualizarProduto(self, id_produto, nome, valor, quantidade, id_categoria, id_fornecedor):
    try:
      cursor = self.db.conexao.cursor()

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

      cursor.execute(query, valores)
      self.db.conexao.commit()
      print("\nProduto atualizado com sucesso!")

    except Exception as erro:
      print(f"Erro ao atualizar produto: {erro}")

    finally:
      if cursor:
        cursor.close()


  def excluirProduto(self, id_produto): 
    try:
      cursor = self.db.conexao.cursor()

      query = """
      DELETE FROM produtos
      WHERE id_produto = %s;
      """

      cursor.execute(query, (id_produto,))
      self.db.conexao.commit()
      print("\nProduto excluído com sucesso!")
  
    except Exception as erro:
      print(f"Erro ao excluir produto: {erro}")

    finally:
      if cursor:
        cursor.close()
