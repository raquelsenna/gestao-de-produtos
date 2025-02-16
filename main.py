# importar biblioteca padrão
from datetime import date

# importar módulos internos  
from database import Database
from config import db_config, login_acesso

# importar classes
from classes import Produto, Categoria, Fornecedor, Venda, Usuario

# função que acessa informações de login no arquivo config.py
def login():
  login = Usuario(
    email=login_acesso["email"],
    senha=login_acesso["senha"]
  )

  try:
    print("\n---Login---")

    while True:
      email = input("Email: ")
      senha = input("Senha: ")

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
  [3] Atualizar Vendas
  [4] Excluir Vendas   
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
          produto = Produto(db)
          categoria = Categoria(db)
          fornecedor = Fornecedor(db)
        
        print("\n---Cadastrar Produtos---\n")

        nome = input("Nome: ")
        valor = float(input("Valor: R$"))
        quantidade = int(input("Quantidade: "))

        categoria.listarCategoria()
        id_categoria = int(input("\nID da categoria do produto: "))

        fornecedor.listarFornecedor()    
        id_fornecedor = int(input("\nID do fornecedor do produto: "))

        produto.cadastrarProduto(nome, valor, quantidade, id_categoria, id_fornecedor)

        db.fechar()

      elif opcao_produto == "2":
        if db.conectar():
          produto = Produto(db)

        produto.listarProduto()

        db.fechar()

      elif opcao_produto == "3":
        if db.conectar(): 
          produto = Produto(db) # Cria instancia da classe produto

          produto.listarProduto() 

          id_produto = int(input("Qual ID do produto que deseja atualizar? "))

          print("\nO que nao for atualizar, deixe em branco!\n")

          nome = input("Atualizar nome: ").strip() or None
          valor = input("Atualizar valor: ").strip() or None
          quantidade = input("Atualizar quantidade: ").strip() or None
          id_categoria = input("Atualizar ID categoria: ").strip() or None
          id_fornecedor = input("Atualizar ID fornecedor: ").strip() or None

          produto.atualizarProduto(id_produto, nome, valor, quantidade, id_categoria, id_fornecedor)

          db.fechar()

      elif opcao_produto == "4":
        if db.conectar():
          produto = Produto(db)

        produto.listarProduto()

        id_produto = int(input("Qual ID do produto deseja excluir? "))

        produto.excluirProduto(id_produto)

        db.fechar()

    if opcao == "2":
      opcao_venda = menu_vendas()

      if opcao_venda == "1":
        if db.conectar():
          venda = Venda(db)
          produto = Produto(db)

        data_venda = date.today()
        produto.listarProduto()
        id_produto = int(input("ID do produto: "))
        quantidade = int(input("Quantidade: "))

        if produto.consultarEstoque(id_produto, quantidade):         
          valor_unitario = produto.buscarValor(id_produto)
          venda.cadastrarVenda(data_venda, id_produto, quantidade, valor_unitario)
          produto.atualizarEstoque(id_produto, quantidade)
        else:
          print("Estoque insuficiente!")

        db.fechar()

      if opcao_venda == "2":
        if db.conectar():
          venda = Venda(db)

        venda.listarVenda()

        db.fechar()

    if opcao == "3":
      opcao_categoria = menu_categorias()

      if opcao_categoria == "1":
        if db.conectar(): 
          categoria = Categoria(db) # Cria instancia da classe Categoria
          
          nome = input("Nome: ")
          categoria.cadastrarCategoria(nome) 
          db.fechar()
      
      elif opcao_categoria == '2':
        if db.conectar(): 
          categoria = Categoria(db) # Cria instancia da classe Categoria

          categoria.listarCategoria() 
          db.fechar()
      
      
      elif opcao_categoria == '3':
        if db.conectar(): 
          categoria = Categoria(db) # Cria instancia da classe Categoria

          categoria.listarCategoria() 

          id_categoria = int(input("Qual ID do produto que deseja atualizar? "))

          nome = input("Atualizar para nome: ")
          
          categoria.atualizarCategoria(id_categoria, nome) 

          db.fechar()

      elif opcao_categoria == '4':
        if db.conectar(): 
          categoria = Categoria(db) # Cria instancia da classe Categoria

          categoria.listarCategoria() 

          id_categoria = int(input("\nQual ID do produto que deseja excluir? "))

          categoria.excluirCategoria(id_categoria) 

          db.fechar()

    if opcao == "4":
      opcao_fornecedor = menu_fornecedores()

      if opcao_fornecedor == "1":
        if db.conectar(): 
          fornecedor = Fornecedor(db) # Cria instancia da classe Fornecedor
          
          nome = input("Nome: ")
          email = input("Email: ")
          telefone = input("Telefone: ")

          fornecedor.cadastrarFornecedor(nome, email, telefone) 

          db.fechar()

      elif opcao_fornecedor == "2":
        if db.conectar():
          fornecedor = Fornecedor(db)

          fornecedor.listarFornecedor() 

          db.fechar()

      elif opcao_fornecedor == '3':
        if db.conectar(): 
          fornecedor = Fornecedor(db) # Cria instancia da classe fornecedor

          fornecedor.listarFornecedor() 

          id_fornecedor = int(input("Qual ID do fornecedor que deseja atualizar? "))

          print("\nO que nao for atualizar, deixe em branco!")

          nome = input("Atualizar nome: ").strip() or None
          email = input("Atualizar email: ").strip() or None
          telefone = input("Atualizar telefone: ").strip() or None

          fornecedor.atualizarFornecedor(id_fornecedor, nome, email, telefone)

          db.fechar()
      
      elif opcao_fornecedor == '4':
        if db.conectar(): 
          fornecedor = Fornecedor(db) # Cria instancia da classe fornecedor

          fornecedor.listarFornecedor() 

          id_fornecedor = int(input("Qual ID do fornecedor que deseja excluir? "))

          fornecedor.excluirFornecedor(id_fornecedor) 

          db.fechar()
        
  except Exception as erro:
    print(f"Ocorreu um erro: {erro}")


main()
