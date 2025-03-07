# Gestão de Produtos 🖥️

### Sobre o projeto
#### Este projeto tem como objetivo criar um sistema de cadastro de produtos eletrônicos, utilizando Python para a lógica de programação e MySQL como sistema de gerenciamento de banco de dados (SGBD). O foco é desenvolver minhas habilidades e aprender mais sobre SGBD e SQL.
#### Projeto pessoal com a finalidade de praticar e obter conhecimento acerca do desenvolvimento de software.
#### As implementações que estão acontecendo podem ser encontradas na branch "feature/poo-cadastro-produtos".

## Tecnologias Utilizadas
- Python: Linguagem de programação utilizada para o desenvolvimento da aplicação.
- MySQL: Banco de dados utilizado para armazenar as informações dos produtos.
- SQL: Linguagem de consulta para interação com o banco de dados.
  
## Conexão com o Banco de Dados
#### Para conectar o banco de dados MySQL ao Python, foram utilizadas as seguintes bibliotecas:
- mysql-connector-python: Escolhida pela facilidade de uso e compatibilidade direta com MySQL.
- python-dotenv: Utilizada para proteger credenciais sensíveis do banco de dados, como usuário e senha, evitando que apareçam nos commits do Git. Mesmo em projetos simples, é importante sempre seguir boas práticas de segurança.

## Funcionalidades do Projeto
- Cadastro de novos produtos eletrônicos.
- Edição e remoção de produtos existentes.
- Consulta de produtos cadastrados.
- Armazenamento seguro das informações no banco de dados.
  
## Como Executar o Projeto
1. Clone o repositório para sua máquina local.
2. Instale as dependências _**pip install mysql-connector-python**_ e _**pip install python-dotenv**_ no terminal.
3. Crie um arquivo .env com suas credenciais de banco de dados, se necessário.
4. Execute o script Python.

## Melhorias Futuras
- Implementar interface gráfica (GUI) para o sistema.
- Adicionar testes automatizados.
- Expandir as funcionalidades para incluir categorias de produtos.
