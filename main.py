from datetime import date
from config import login_acesso
from classes import Container, Usuario
from classes.usuario import EmailInvalidoError, SenhaInvalidaError
from erros.entrada_utils import entrada_texto, entrada_float, entrada_inteiro

def login():
  credenciais = Usuario(
    email=login_acesso["email"],
    senha=login_acesso["senha"]
  )

  email = input("Email: ")
  senha = input("senha: ") 

  try:
    mensagem = credenciais.autenticar(email, senha)
    print(mensagem)
    return True
  except EmailInvalidoError as e:
    print(e)
    False
  except SenhaInvalidaError as e:
    print(e)
    return False


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
  while True:
    if login():
      break

  try:
    opcao = menu_principal()
    container = Container()

    if opcao == "1":

      opcao_produto = menu_produtos()

      if opcao_produto == "1":
        print("\n---Cadastrar Produtos---\n")

        nome = entrada_texto("Nome: ")
        valor = entrada_float("Valor: R$ ")
        quantidade = entrada_inteiro("Quantidade: ")

        print("listando categoria")
        container.categoria.listar_categoria()
        id_categoria = entrada_inteiro("\nID da categoria do produto: ")

        container.fornecedor.listar_fornecedor()    
        id_fornecedor = entrada_inteiro("\nID do fornecedor do produto: ")

        container.produto.cadastrar_produto(nome, valor, quantidade, id_categoria, id_fornecedor)


      elif opcao_produto == "2":
        container.produto.listar_produto()


      elif opcao_produto == "3": 
        container.produto.listar_produto() 

        id_produto = entrada_inteiro("Qual ID do produto que deseja atualizar? ")

        print("\nO que nao for atualizar, deixe em branco!\n")

        nome = entrada_texto("Atualizar nome: ") or None
        valor = entrada_float("Atualizar valor: ") or None
        quantidade = entrada_inteiro("Atualizar quantidade: ") or None
        id_categoria = entrada_inteiro("Atualizar ID categoria: ") or None
        id_fornecedor = entrada_inteiro("Atualizar ID fornecedor: ") or None

        container.produto.atualizar_produto(id_produto, nome, valor, quantidade, id_categoria, id_fornecedor)


      elif opcao_produto == "4":

        container.produto.listar_produto()

        id_produto = entrada_inteiro("Qual ID do produto deseja excluir? ")

        container.produto.excluir_produto(id_produto)


    if opcao == "2":
      opcao_venda = menu_vendas()

      if opcao_venda == "1":

        data_venda = date.today()
        container.produto.listar_produto()
        id_produto = entrada_inteiro("ID do produto: ")
        quantidade = entrada_inteiro("Quantidade: ")

        if container.produto.consultar_estoque(id_produto, quantidade):
          valor_unitario = container.produto.pegar_valor(id_produto)
          container.venda.cadastrar_venda(data_venda, id_produto, quantidade, valor_unitario)
          container.produto.atualizar_estoque(id_produto, quantidade)
            
        else:
          print("Estoque insuficiente!")


      if opcao_venda == "2":
        container.venda.listar_venda()


    if opcao == "3":
      opcao_categoria = menu_categorias()

      if opcao_categoria == "1": 
          
        nome = entrada_texto("Nome: ")
        container.categoria.cadastrar_categoria(nome) 
      
      elif opcao_categoria == '2': 
        container.categoria.listar_categoria() 
      
      elif opcao_categoria == '3': 
        container.categoria.listar_categoria() 

        id_categoria = entrada_inteiro("Qual ID do produto que deseja atualizar? ") or None
        nome = entrada_texto("Atualizar para nome: ") or None
          
        container.categoria.atualizar_categoria(id_categoria, nome) 


      elif opcao_categoria == '4': 
        container.categoria.listar_categoria() 

        id_categoria = entrada_inteiro("\nQual ID do produto que deseja excluir? ")

        container.categoria.excluir_categoria(id_categoria) 


    if opcao == "4":
      opcao_fornecedor = menu_fornecedores()

      if opcao_fornecedor == "1":  
        nome = entrada_texto("Nome: ")
        email = entrada_texto("Email: ")
        telefone = entrada_texto("Telefone: ")

        container.fornecedor.cadastrar_fornecedor(nome, email, telefone) 


      elif opcao_fornecedor == "2":
        container.fornecedor.listar_fornecedor() 


      elif opcao_fornecedor == '3': 
        container.fornecedor.listar_fornecedor() 

        id_fornecedor = entrada_inteiro("Qual ID do fornecedor que deseja atualizar? ")

        print("\nO que nao for atualizar, deixe em branco!")

        nome = entrada_texto("Atualizar nome: ") or None
        email = entrada_texto("Atualizar email: ") or None
        telefone = entrada_texto("Atualizar telefone: ") or None
          
      
      elif opcao_fornecedor == '4': 
        container.fornecedor.listar_fornecedor() 

        id_fornecedor = entrada_inteiro("Qual ID do fornecedor que deseja excluir? ")

        container.fornecedor.excluir_fornecedor(id_fornecedor) 

        
  except Exception as erro:
    print(f"Ocorreu um erro: {erro}")

main()