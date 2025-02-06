# Gestão de Produtos 🖥️
#### Projeto pessoal com a finalidade de praticar e obter conhecimento acerca do desenvolvimento de software.

## Tecnologias utilizadas 
- Linguagens de programação: Python, SQL.
- SGBD: MySQL.
- biliotetecaS: Mysql Connector.

## Funcionalidades do Projeto
- Cadastro de novos produtos, vendas, categorias e fornecedores.
- Leitura, atualização e remoção das colunas acima.
- Gestão de estoque.
- Capacidade de analizar dados para tomada de decisão dentro do negócio.

## Sobre
### O projeto "Gestão de Produtos" tem como foco pequenos comércios e lojas que precisam de um sistema de software para auxiliar na produtividade e estabilidade do dia a dia.
#### O projeto surgiu como uma ideia para a conclusão do curso "UML para Desenvolvimento de Software" no SENAC. Como projeto de conclusão do curso foi exigido apenas o UML, porém posteriormente, através da curiosidade e necessidade de praticar e entender como funcionam os sistemas, resolvi começar o desenvolvê-lo. O desenvolvimento é acontece desde o planejamento, isso é, UML e documentação, até a implentação do back-end, front-end e banco de dados.
#### Atualmente está sendo desenvolvido as classes e suas relações. 

## Banco de Dados
#### Como Sistema de Gerenciamento de Banco de Dados foi utilizado o MySQL. Foi criado um banco de dados chamado gestao_produtos, no qual contém as tabelas "vendas", "produtos", "categorias" e "fornecedores".
#### As tabelas "vendas", "categorias" e "rnecedofores" mantém relacionamento com a tabela "produtos".

## Desenvolvimento
#### Python foi a linguagem de programação principal escolhida, juntamente com POO como paradigma de programação. A estrutura de classes no python segue a mesma estrutura e relacionamento do banco de dados, tendo como acréscimo a tabela "Usuario" para fazer a autenticação do sistema.

## Como rodar o sistema
#### Na versão atual, o sistema pode ser rodado facilmente no terminal. 
#### 1. No SGBD crie um banco de dados e siga o esquema do UML disponível na pasta de documentação para construir as tabelas e atributos.
#### 2. Clone o repositório para sua máquina local.
#### 3. Ao abrir o projeto, crie 1 aquivo chamado "config.py" e utilize o "config_tamplate.py" como base de código. Substitua os valores de "db_config" para o valor correspondente ao seu banco de dados e "login_acesso" para o email e senha que desejar.
#### 4. Após isso, é possível rodar o sistema no terminal e ver as alterações acontecendo no banco de dados.

