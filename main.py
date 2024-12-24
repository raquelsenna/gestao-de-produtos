from database import Database
from config import db_config
from classes.produto import Produto
from classes.categoria import Categoria
from classes.fornecedor import Fornecedor


def menu_principal():
  print("""\n---Sistema de Gestão---
        
  [1] Gerenciar Produtos
  [2] Gerenciar Vendas
  [3] Gerenciar Categorias
  [4] Gerenciar Fornecedores
  [5] Sair
  """)
  return input("-> ")


def menu_produtos():
  print("""\n---Gerenciar Produtos---
    
  [1] Cadastrar Produto
  [2] Listar Produto
  [3] Atualizar Produto
  [4] Excluir Produto    
  """)
  return input("-> ")


def menu_categorias():
  print("""\n---Gerenciar Categorias---
    
  [1] Cadastrar Categorias
  [2] Listar Categorias
  [3] Atualizar Categorias
  [4] Excluir Categorias    
  """)
  return input("-> ")


def menu_fornecedores():
  print("""\n---Gerenciar Fornecedores---
    
  [1] Cadastrar Fornecedores
  [2] Listar Fornecedores
  [3] Atualizar Fornecedores
  [4] Excluir Fornecedores    
  """)
  return input("-> ")


def main():
  db = Database(
    host=db_config["host"],
    user=db_config["user"],
    password=db_config["password"],
    database=db_config["database"]
  )

  try:
    opcao = menu_principal()


    if opcao == "1":

      opcao_produto = menu_produtos()

      if opcao_produto == "1":
        if db.conectar(): 
          novo_produto = Produto(db)
        
        print("\n---Cadastrar Produtos---\n")

        nome = input("Nome: ")
        valor = float(input("Valor: R$"))
        quantidade = int(input("Quantidade: "))
        categoria = ("Categoria: ")
        fornecedor = ("Fornecedor: ")

        novo_produto.cadastrarProduto(nome, valor,quantidade, categoria, fornecedor)
          
        print("\nProduto inserido com sucesso!\n")


    if opcao == "3":
      opcao_categoria = menu_categorias()

      if opcao_categoria == "1":
        if db.conectar(): 
          nova_categoria = Categoria(db) # Cria instancia da classe Categoria
          
          nome = input("Nome: ")
          nova_categoria.cadastrarCategoria(nome) 
          db.fechar()
      
      elif opcao_categoria == '2':
        if db.conectar(): 
          nova_categoria = Categoria(db) # Cria instancia da classe Categoria

          nova_categoria.listarCategoria() 
          db.fechar()
      
      
      elif opcao_categoria == '3':
        if db.conectar(): 
          nova_categoria = Categoria(db) # Cria instancia da classe Categoria

          nova_categoria.listarCategoria() 

          id_categoria = int(input("Qual ID do produto que deseja atualizar? "))

          nome = input("Atualizar para nome: ")
          
          nova_categoria.atualizarCategoria(id_categoria, nome) 

          db.fechar()

      elif opcao_categoria == '4':
        if db.conectar(): 
          nova_categoria = Categoria(db) # Cria instancia da classe Categoria

          nova_categoria.listarCategoria() 

          id_categoria = int(input("Qual ID do produto que deseja excluir? "))

          nova_categoria.excluirCategoria(id_categoria) 

          db.fechar()

  
    if opcao == "4":
      opcao_fornecedor = menu_fornecedores()

      if opcao_fornecedor == "1":
        if db.conectar(): 
          novo_fornecedor = Fornecedor(db) # Cria instancia da classe Fornecedor
          
          nome = input("Nome: ")
          email = input("Email: ")
          telefone = input("Telefone: ")

          novo_fornecedor.cadastrarFornecedor(nome, email, telefone) 

          db.fechar()

      elif opcao_fornecedor == "2":
        if db.conectar():
          novo_fornecedor = Fornecedor(db)

          novo_fornecedor.listarFornecedor() 

          db.fechar()

      elif opcao_fornecedor == '3':
        if db.conectar(): 
          novo_fornecedor = Fornecedor(db) # Cria instancia da classe fornecedor

          novo_fornecedor.listarFornecedor() 

          id_fornecedor = int(input("Qual ID do fornecedor que deseja atualizar? "))

          print("\nO que nao for atualizar, deixe em branco!")

          nome = input("Atualizar nome: ").strip() or None
          email = input("Atualizar email: ").strip() or None
          telefone = input("Atualizar telefone: ").strip() or None

          novo_fornecedor.atualizarFornecedor(id_fornecedor, nome, email, telefone)

          db.fechar()
      
      elif opcao_fornecedor == '4':
        if db.conectar(): 
          novo_fornecedor = Fornecedor(db) # Cria instancia da classe fornecedor

          novo_fornecedor.listarFornecedor() 

          id_fornecedor = int(input("Qual ID do fornecedor que deseja excluir? "))

          novo_fornecedor.excluirFornecedor(id_fornecedor) 

          db.fechar()
        
  except Exception as erro:
    print(f"Ocorreu um erro: {erro}")


main()
