# Jogoteca

Bem-vindo à Jogoteca! Este é um projeto de aplicação web criado com o framework Flask, que demonstra um sistema CRUD completo para uma lista de jogos, incluindo o nome do jogo, a plataforma e o console aos quais ele pertence. Além disso, esta aplicação permite o cadastro de novos jogos e inclui funcionalidades de login para acesso restrito a certas páginas.

## Funcionalidades Principais

- **Lista de Jogos**: Exibe todos os jogos cadastrados, com informações sobre o nome, a plataforma e o console.
- **Cadastro de Jogos**: Permite a adição/edição de novos jogos ao sistema.
- **Login/Logout**: Usuários podem fazer login para acessar páginas restritas.
- **Restrição de Acesso**: As páginas de criação/edição de novos jogos são acessíveis apenas para usuários autenticados.
- **Integrado ao DB**: A aplicação está integrada a um banco de dados MySQL, utilizando o ORM SQLAlchemy.
- **Implementação de CRUD**: Implementação completa das operações de Create, Read, Update e Delete.
- **Suporte para Imagens**: A aplicação permite o upload e a exibição de imagens associadas aos jogos.
- **Validação de Formulários**: Com Flask WTForms, para garantir uma entrada de dados segura.
- **Criptografia de Senhas**: As senhas dos usuários são armazenadas de forma segura usando Bcrypt.

## Tecnologias Utilizadas

O projeto Jogoteca usa uma variedade de bibliotecas e ferramentas para funcionar corretamente. Aqui estão as principais tecnologias utilizadas:

- **Flask**: O principal framework web utilizado para criar a aplicação.
- **Flask-Bcrypt**: Fornece a capacidade de criptografar e verificar senhas para maior segurança.
- **Flask-SQLAlchemy**: Integração do Flask com o SQLAlchemy para operações ORM (Object-Relational Mapping).
- **Flask-WTF**: Fornece uma interface para usar o WTForms com Flask, permitindo validação de formulários.
- **SQLAlchemy**: Biblioteca para mapeamento objeto-relacional com suporte a bancos de dados relacionais como o MySQL.
- **MySQL Connector/Python**: Biblioteca para conectar-se ao banco de dados MySQL.
- **mysqlclient**: Outro cliente para MySQL, com suporte ao uso no SQLAlchemy.
- **Werkzeug**: Biblioteca que fornece utilidades para Flask, como roteamento e manipulação de solicitações.
- **WTForms**: Biblioteca para criar e validar formulários de forma simples e segura.
- **Jinja2**: Um mecanismo de templates usado para renderizar páginas HTML dinamicamente.
- **MarkupSafe**: Fornece funcionalidades para trabalhar com strings seguras em HTML.
- **itsdangerous**: Utilizada para criar assinaturas criptograficamente seguras para uso em tokens, cookies, entre outros.
- **greenlet**: Biblioteca que permite a criação de greenlets, úteis para tarefas assíncronas.
- **blinker**: Biblioteca de sinalização para enviar sinais e notificações entre componentes.
- **click**: Ferramenta para criar interfaces de linha de comando (CLI).
- **colorama**: Para adicionar cores e estilos ao terminal, facilitando a depuração e o uso do CLI.
- **typing_extensions**: Biblioteca que fornece extensões para anotações de tipo (type hinting) em Python.

## Estrutura do Projeto

- `jogoteca.py`: Arquivo principal que executa a aplicação Flask.
- `models.py`: Define os modelos de dados usando SQLAlchemy.
- `views_game.py`: Define as rotas da aplicação relacionadas aos jogos.
- `views_user.py`: Define as rotas da aplicação relacionadas aos usuários.
- `templates/`: Contém os templates HTML para renderização das páginas.
- `static/`: Contém arquivos estáticos, como CSS e imagens.

## Como Executar a Aplicação

1. Clone este repositório para a sua máquina local.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Configure a conexão com o banco de dados MySQL executando o arquivo `prepara_banco.py`.
4. Execute a aplicação com `flask run`.
5. Acesse a aplicação em `http://localhost:5000`.

## Aprendizado no Curso de Flask da Alura

Este projeto foi criado durante o curso de Flask da Alura, onde foram abordados os seguintes tópicos:

- Integração com banco de dados MySQL usando SQLAlchemy.
- Implementação de um CRUD completo.
- Adição de imagens na aplicação.
- Validação de formulários com Flask WTForms.
- Criptografia de senhas com Bcrypt.