from database import Database

class Fornecedor:
  def __init__(self, db):
    self.__db = db


  def cadastrar_fornecedor(self, nome, email, telefone):
    try:
      query = """
      INSERT INTO fornecedores (nome, email, telefone)
      VALUES(%s, %s, %s)
      """

      valores = (nome, email, telefone,)

      self.__db.executar(query, valores)

      print("Fornecedor cadastrado com Sucesso!")
    
    except Exception as erro:
      print(f"Erro ao cadastrar fornecedor: {erro}")


  def listar_fornecedor(self):
    try:
      query = """
        SELECT * FROM fornecedores;
      """
      
      fornecedores = self.__db.buscar(query)
      
      if fornecedores:
        print("\n---Lista de Fornecedores---\n")
        for fornecedor in fornecedores:
          print(f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Email: {fornecedor[2]}, Telefone: {fornecedor[3]}")
      else: 
        print("Não há produtos")

    except Database.mysql.connector.Error as erro:
      print(f"\nErro ao listar fornecedores: {erro}\n")


  def atualizar_fornecedor(self, id_fornecedor, nome, email, telefone):
    try:
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

      self.__db.executar(query, valores)

      print("\nFornecedor atualizado com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao atualizar fornecedor: {erro}")


  def excluir_fornecedor(self, id_fornecedor):
    try:
      query = """
        DELETE FROM fornecedores 
        WHERE id_fornecedor = %s;
      """

      self.__db.executar(query, (id_fornecedor,))

      print("\nFornecedor excluído com sucesso!\n")

    except Exception as erro:
      print(f"Erro ao excluir fornecedor: {erro}")