class Fornecedor:
  def __init__(self, db):
    self.db = db


  def cadastrarFornecedor(self, nome, email, telefone):
    try:
      cursor = self.db.conexao.cursor()

      query = """
      INSERT INTO fornecedores (nome, email, telefone)
      VALUES(%s, %s, %s)
      """

      valores = (nome, email, telefone,)

      cursor.execute(query, valores)  
      self.db.conexao.commit()
      print("Fornecedor cadastrado com Sucesso!")
    
    except Exception as erro:
      print(f"Erro ao cadastrar fornecedor: {erro}")

    finally:
      if cursor:
        cursor.close()


  def listarFornecedor(self):
    try:
      cursor = self.db.conexao.cursor()

      query = """
        SELECT * FROM fornecedores;
      """
      
      cursor.execute(query)
      fornecedores = cursor.fetchall()
      
      if fornecedores:
        print("\n---Lista de Fornecedores---\n")
        for fornecedor in fornecedores:
          print(f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Email: {fornecedor[2]}, Telefone: {fornecedor[3]}")

    finally:
      if cursor:
        cursor.close()


  def atualizarFornecedor(self, id_fornecedor, nome, email, telefone):
    try:
      cursor = self.db.conexao.cursor()

      campos = []
      valores = []

      if nome:
        campos.append("nome = %s")
        valores.append(nome)

      if email:
        campos.append("email = %s")
        valores.append(email)

      if telefone:
        campos.append("telefone = %s")
        valores.append(telefone)

      query = f"""
        UPDATE fornecedores
        SET {", ".join(campos)}
        WHERE id_fornecedor = %s;
      """
      
      valores.append(id_fornecedor)

      cursor.execute(query, valores)
      self.db.conexao.commit()
      print("\nFornecedor atualizado com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao atualizar fornecedor: {erro}")

    finally:
      if cursor:
        cursor.close()


  def excluirFornecedor(self, id_fornecedor):
    try:
      cursor = self.db.conexao.cursor()

      query = """
        DELETE FROM fornecedores 
        WHERE id_fornecedor = %s;
      """
      
      cursor.execute(query, (id_fornecedor,))
      self.db.conexao.commit()
      print("\nFornecedor excluído com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao excluir fornecedor: {erro}")

    finally:
      if cursor:
        cursor.close()