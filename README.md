# Projeto controle de estoque  
- Objetivo controlar estoque de diferentes produtos. Cadastro de produtos por categoria, isso nos dar a flexibilidade de cadastrar o mesmo produto com diferentes características.  
Exemplo estoque de roupas:
- Podemos cadastrar uma categoria roupas, e na descrição podemos adicionar (camiseta regata 100% algodão, manga cumprida 75% algodão, etc), lembrandro que está camiseta pode ter vários tipos de tamanho, cor, etc.

## Banco de dados  
MYSQL versão 5.7  
Obs: mysql está rodando no container docker, após baixar a imagem mysql e criar o container, basta criar database **estoque**. Quando rodar o flask, as tabelas serpa criada automaticamente no banco de dados.

## back_end_estoque  
Dependências para back-end  
obs: rodar os comandos dentro da pasta beck_end_estoque.   
- Instalar Flask   
`pip install Flask`   

- Instalar cors do flask   
`pip install Flask-Cors`  

- Instalar ORM sqlAchemy versão 1.4.17   
`pip install SQLAlchemy==1.4.17`  

- Intalar conector do python com mysql "pymysql"  
`pip install pymysql`  


## front_end_estoque  
Dependências para o front deve ter node instalado.  
Obs: rodar os comando dentro da pasta front_end_estoque.  

- Instalar as depedências front, basta rodar o comando abaixo:  
`npm install`  

### Rodando o projeto
**back-end**
- Na pasta back_end_estoque rodar o comando abaixo:  
`python routes.py`  

**front-end**
- Na pasta front_end_estoque/react-axios rodar o comando abaixo:  
`npm run dev`






