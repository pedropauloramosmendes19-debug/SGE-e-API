SGE-e-API (Sistema de Gestão de Estoque)
📖 Sobre o Projeto
O SGE (Sistema de Gestão de Estoque) é uma aplicação web completa construída em Python com o framework Django. O projeto permite o gerenciamento detalhado do inventário de uma empresa, incluindo o controle de produtos, marcas, categorias, fornecedores e o fluxo de entradas e saídas.

Além da interface web tradicional, o projeto também expõe uma API REST (construída com Django REST Framework) para permitir a integração com outros sistemas, aplicativos móveis ou serviços de front-end.

✨ Funcionalidades Principais
Este projeto implementa um sistema CRUD (Criar, Ler, Atualizar, Deletar) completo, além de funcionalidades de análise e segurança.

Autenticação e Permissões:

Sistema completo de login e logout para usuários.

Proteção de rotas (views) que exigem que o usuário esteja logado.

Sistema de permissões baseado em grupos (ex: um grupo "Visualizador" que só pode ver os dados, mas não criar ou deletar).

Dashboard Analítico:

Gráficos dinâmicos (criados com Chart.js) que exibem:

Valor total de vendas por dia.

Quantidade de vendas por dia.

Distribuição de produtos por categoria (Gráfico de Rosca).

Distribuição de produtos por marca (Gráfico de Rosca).

Gerenciamento de Entidades (CRUD Completo):

Gestão de Produtos.

Gestão de Categorias.

Gestão de Marcas.

Gestão de Fornecedores.

Controle de Estoque (Movimentações):

Registro de Entradas (Inflows) de produtos no estoque.

Registro de Saídas (Outflows) de produtos (vendas).

API RESTful:

Endpoints seguros que exigem autenticação via token (JWT).

Permite que sistemas externos acessem e manipulem os dados da aplicação.

🛠️ Tecnologias Utilizadas
O projeto foi construído utilizando as seguintes tecnologias:

Back-end:

Python 3

Django 5: O framework principal para a aplicação web.

Django REST Framework (DRF): Para a construção da API.

Simple JWT (DRF): Para autenticação da API baseada em JSON Web Tokens.

SQLite3: Banco de dados padrão do Django (pode ser facilmente trocado para PostgreSQL ou MySQL).

Front-end:

HTML5

Bootstrap 5: Para a criação de um layout responsivo e moderno.

JavaScript (ES6+): Para interatividade no lado do cliente.

Chart.js: Para a renderização dos gráficos no dashboard.

🚀 Como Executar o Projeto
Para executar este projeto localmente, siga os passos abaixo:

Clone o repositório:

Bash

git clone https://github.com/pedropauloramosmendes19-debug/SGE-e-API.git
cd SGE-e-API
Crie e ative um ambiente virtual (venv):

Bash

# Criar o ambiente
python -m venv venv

# Ativar no Windows (cmd/powershell)
.\venv\Scripts\activate
Instale as dependências: (Recomendação: Crie um arquivo requirements.txt no seu projeto com pip freeze > requirements.txt e então rode o comando abaixo)

Bash

pip install django djangorestframework djangorestframework-simplejwt
Aplique as migrações do banco de dados:

Bash

python manage.py migrate
Crie um superusuário (para acessar o Admin do Django):

Bash

python manage.py createsuperuser
(Siga as instruções para criar seu usuário e senha de administrador)

Execute o servidor de desenvolvimento:

Bash

python manage.py runserver
Acesse o projeto:

Site: Abra seu navegador em http://127.0.0.1:8000/

Admin: Acesse http://127.0.0.1:8000/admin/ e faça login com o superusuário.

📡 Endpoints da API
A API segue os padrões RESTful e está (ou estará) disponível nos seguintes endpoints:

/api/token/: Obter um token JWT (Autenticação).

/api/token/refresh/: Atualizar um token JWT.

/api/brands/: Listar ou criar novas marcas.

/api/categories/: Listar ou criar novas categorias.

(...e assim por diante para os outros modelos)
