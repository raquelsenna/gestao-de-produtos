# Gestão de Produtos 🖥️

### Projeto Pessoal com Python e MySQL
#### Esse projeto tem como objetivo desenvolver um sistema de gestão de produtos, focado em negócios de pequeno a grande porte que precisam de um sistema automatizado no qual permita otimizar o seu dia a dia, o tornando mais produtivo e eficiente.

## Tecnologias Utilizadas

- Linguagem de Programação: Python, SQL.
-	Banco de dados: MySQL.
-	Bibliotecas: MySql Connector Python

## Funcionalidades do Projeto
- Cadastro de novos produtos, vendas, categorias e fornecedores.
- Leitura, atualização e remoção das colunas acima.
- Gestão de estoque.
- Capacidade de analizar dados para tomada de decisão dentro do negócio.
  
## Como Executar o Projeto
1. Clone o repositório para sua máquina local.
2. Instale as dependências _**pip install mysql-connector-python**_ no terminal.
3. Banco de dados:
  - Copie o arquivo `config_template.py` para `config.py`.
  - Preencha as informações de banco de dados no arquivo `config.py`:
      db_config = {
        "host": "seu_localhost",
        "user": "seu_root",
        "password": "sua_senha",
        "database": "seu_banco"
      }

4. Execute o projeto no Python.

## Melhorias Futuras
- Implementar interface gráfica para o sistema.
- Adicionar testes automatizados.
- Expandir as funcionalidades de estoque para maior controle.