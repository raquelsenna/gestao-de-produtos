from database import Database
from config import db_config
from classes.produto import Produto
from classes.categoria import Categoria


def menu_principal():
  print("""---Sistema de Gestão---
        
  [1] Gerenciar Produtos
  [2] Gerenciar Vendas
  [3] Gerenciar Categorias
  [4] Gerenciar Fornecedores
  [5] Sair
  """)
  return input("-> ")


# def menu_produtos():
#   print("""---Gerenciar Produtos---
    
#   [1] Cadastrar Produto
#   [2] Listar Produto
#   [3] Atualizar Produto
#   [4] Excluir Produto    
#   """)
#   return input("-> ")


def menu_categorias():
  print("""---Gerenciar Categorias---
    
  [1] Cadastrar Categorias
  [2] Listar Categorias
  [3] Atualizar Categorias
  [4] Excluir Categorias    
  """)
  return input("-> ")


# def menu_fornecedores():
#   print("""---Gerenciar Fornecedores---
    
#   [1] Cadastrar Fornecedores
#   [2] Listar Fornecedores
#   [3] Atualizar Fornecedores
#   [4] Excluir Fornecedores    
#   """)
#   return input("-> ")


def main():
  db = Database(
    host=db_config["host"],
    user=db_config["user"],
    password=db_config["password"],
    database=db_config["database"]
  )

  try:
    opcao = menu_principal()

    # if opcao == "1":

    #   opcao_produto = menu_produtos()

    #   if opcao_produto == "1":
    #     print("\n---Cadastrar Produtos---")

    #     nome = input("\nNome: ")
    #     valor = float(input("Valor: R$"))
    #     quantidade = int(input("Quantidade: "))
    #     categoria = ("Categoria: ")
    #     fornecedor = ("Fornecedor: ")

    #     Produto.cadastrarProduto(nome, valor,quantidade, categoria, fornecedor)
          
    #     print("\nProduto inserido com sucesso!\n")

        # if opcao == "5": 
        #   Database.fechar()
        #   break

    if opcao == "3":
      opcao_categoria = menu_categorias()

      if opcao_categoria == "1":
        if db.conectar(): 
          nova_categoria = Categoria(db) # Cria instancia da classe Categoria
          
          nome = input("Nome: ")
          nova_categoria.cadastrarCategoria(nome) 
          db.fechar()
  
  except Exception as erro:
    print(f"Ocorreu um erro: {erro}")


main()
