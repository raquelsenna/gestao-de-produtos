from datetime import date
from config import login_acesso

from classes import Container, Usuario

def login():
  login = Usuario(
    email=login_acesso["email"],
    senha=login_acesso["senha"]
  )

  try:
    print("\n---Login---")

    while True:
      email = input("Email: ")
      senha = input("senha: ")

      if login.autenticar(email, senha) == True:
        break
      else:
        continue

  except Exception as erro:
    print(f"Ocorreu um erro: {erro}")


def menu_principal():
  print("""---Sistema de Gestão---
        
  [1] Gerenciar Produtos
  [2] Gerenciar Vendas
  [3] Gerenciar Categorias
  [4] Gerenciar Fornecedores
  [5] Sair
  """)
  return input("-> ")


def menu_produtos():
  print("""\n---Gerenciar Produtos---
    
  [1] Cadastrar Produtos
  [2] Listar Produtos
  [3] Atualizar Produtos
  [4] Excluir Produtos   
  """)
  return input("-> ")


def menu_vendas():
  print("""\n---Gerenciar Vendas---
    
  [1] Cadastrar Vendas
  [2] Listar Vendas  
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
  login()

  try:
    opcao = menu_principal()
    container = Container()

    if opcao == "1":

      opcao_produto = menu_produtos()

      if opcao_produto == "1":
        if container.conectar(): 
        
          print("\n---Cadastrar Produtos---\n")

          nome = input("Nome: ")
          valor = float(input("Valor: R$"))
          quantidade = int(input("Quantidade: "))

          container.categoria.listarCategoria()
          id_categoria = int(input("\nID da categoria do produto: "))

          container.fornecedor.listarFornecedor()    
          id_fornecedor = int(input("\nID do fornecedor do produto: "))

          container.produto.cadastrarProduto(nome, valor, quantidade, id_categoria, id_fornecedor)

          container.fechar()

      elif opcao_produto == "2":
        if container.conectar():
          container.produto.listarProduto()

          container.fechar()

      elif opcao_produto == "3":
        if container.conectar(): 
          container.produto.listarProduto() 

          id_produto = int(input("Qual ID do produto que deseja atualizar? "))

          print("\nO que nao for atualizar, deixe em branco!\n")

          nome = input("Atualizar nome: ").strip() or None
          valor = input("Atualizar valor: ").strip() or None
          quantidade = input("Atualizar quantidade: ").strip() or None
          id_categoria = input("Atualizar ID categoria: ").strip() or None
          id_fornecedor = input("Atualizar ID fornecedor: ").strip() or None

          container.produto.atualizarProduto(id_produto, nome, valor, quantidade, id_categoria, id_fornecedor)

          container.fechar()

      elif opcao_produto == "4":
        if container.conectar():

          container.produto.listarProduto()

          id_produto = int(input("Qual ID do produto deseja excluir? "))

          container.produto.excluirProduto(id_produto)

          container.fechar()

    if opcao == "2":
      opcao_venda = menu_vendas()

      if opcao_venda == "1":
        if container.conectar():

          data_venda = date.today()
          container.produto.listarProduto()
          id_produto = int(input("ID do produto: "))
          quantidade = int(input("Quantidade: "))

          if container.produto.consultarEstoque(id_produto, quantidade):         
            valor_unitario = container.produto.buscarValor(id_produto)
            container.venda.cadastrarVenda(data_venda, id_produto, quantidade, valor_unitario)
            container.produto.atualizarEstoque(id_produto, quantidade)
          else:
            print("Estoque insuficiente!")

          container.fechar()

      if opcao_venda == "2":
        if container.conectar():
          container.venda.listarVenda()

          container.fechar()

    if opcao == "3":
      opcao_categoria = menu_categorias()

      if opcao_categoria == "1":
        if container.conectar(): 
          
          nome = input("Nome: ")
          container.categoria.cadastrarCategoria(nome) 
          container.fechar()
      
      elif opcao_categoria == '2':
        if container.conectar(): 
          container.categoria.listarCategoria() 
          container.fechar()
      
      
      elif opcao_categoria == '3':
        if container.conectar(): 
          container.categoria.listarCategoria() 

          id_categoria = int(input("Qual ID do produto que deseja atualizar? "))

          nome = input("Atualizar para nome: ")
          
          container.categoria.atualizarCategoria(id_categoria, nome) 

          container.fechar()

      elif opcao_categoria == '4':
        if container.conectar(): 
          container.categoria.listarCategoria() 

          id_categoria = int(input("\nQual ID do produto que deseja excluir? "))

          container.categoria.excluirCategoria(id_categoria) 

          container.fechar()

    if opcao == "4":
      opcao_fornecedor = menu_fornecedores()

      if opcao_fornecedor == "1":
        if container.conectar():  
          nome = input("Nome: ")
          email = input("Email: ")
          telefone = input("Telefone: ")

          container.fornecedor.cadastrarFornecedor(nome, email, telefone) 

          container.fechar()

      elif opcao_fornecedor == "2":
        if container.conectar():
          container.fornecedor.listarFornecedor() 

          container.fechar()

      elif opcao_fornecedor == '3':
        if container.conectar(): 
          container.fornecedor.listarFornecedor() 

          id_fornecedor = int(input("Qual ID do fornecedor que deseja atualizar? "))

          print("\nO que nao for atualizar, deixe em branco!")

          nome = input("Atualizar nome: ").strip() or None
          email = input("Atualizar email: ").strip() or None
          telefone = input("Atualizar telefone: ").strip() or None

          container.fornecedor.atualizarFornecedor(id_fornecedor, nome, email, telefone)

          container.fechar()
      
      elif opcao_fornecedor == '4':
        if container.conectar(): 
          container.fornecedor.listarFornecedor() 

          id_fornecedor = int(input("Qual ID do fornecedor que deseja excluir? "))

          container.fornecedor.excluirFornecedor(id_fornecedor) 

          container.fechar()
        
  except Exception as erro:
    print(f"Ocorreu um erro: {erro}")


main()
