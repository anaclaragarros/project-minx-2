# project-minx - back-end
<br><br> 
 
**</u>Minx - Projeto de Rede Social</u>**<br>
Minx é um projeto de rede social desenvolvido para permitir que usuários se conectem, compartilhem postagens, curtam, comentem, e visualizem feeds com postagens de amigos. Este projeto foi desenvolvido com Django para a API backend, utilizando um banco de dados para armazenar informações dos usuários e interações, como curtidas e comentários.
<br>
Funcionalidades
Login de Usuário: Os usuários podem se registrar e fazer login.
Postagens: Os usuários podem criar postagens com título e conteúdo.
Curtidas: Os usuários podem curtir postagens feitas por outros usuários.
Comentários: Os usuários podem comentar nas postagens.
Feed: O feed exibe as postagens do usuário e suas postagens de amigos.
Amizade: Os usuários podem adicionar amigos e interagir com postagens no feed de amigos.


**</u>Tecnologias Usadas</u>**<br>
Backend: Django (com Django REST Framework)<br>
Banco de Dados: SQLite (padrão do Django, pode ser alterado para PostgreSQL ou outro banco)<br>
Autenticação: JWT (JSON Web Tokens)<br>
Frontend: A interface do frontend pode ser construída em qualquer framework (por exemplo, React, Flutter, etc.).<br>
<br>
**Requisitos**<br>
Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:
<br>
Python (versão 3.8 ou superior)<br>
Django (versão 5.x ou superior)<br>
Django REST Framework<br>
Django-cors-headers<br>
SQLite3 (padrão no Django)<br>
<br>
Passo 1: Clonar o Repositório<br>
Primeiro, clone o repositório para sua máquina local:<br>

bash<br>
Copiar <br>
git clone https://github.com/seu-usuario/minx.git<br>
cd minx<br>
Passo 2: Criar um Ambiente Virtual<br>
Crie um ambiente virtual para isolar as dependências do projeto.<br>

bash<br>
Copiar código<br>
python -m venv venv<br>
Passo 3: Ativar o Ambiente Virtual<br>
Ative o ambiente virtual. Dependendo do seu sistema operacional, use um dos seguintes comandos:<br>

**Windows**:<br>
<br>
bash<br>
Copiar código<br>
.\venv\Scripts\activate<br>


bash<br>
Copiar código<br>
source venv/bin/activate<br>
Passo 4: Instalar Dependências<br> 
Instale as dependências do projeto listadas no arquivo requirements.txt.<br> 
bash <br>
Copiar código <br>
pip install -r requirements.txt<br>
Passo 5: Configurar o Banco de Dados<br>
Após instalar as dependências, execute as migrações para configurar o banco de dados:<br> 

bash<br>
Copiar código<br>
python manage.py migrate <br>
Passo 6: Criar um Superusuário (Opcional)<br>
Se desejar acessar o painel administrativo do Django (para gerenciar os usuários, postagens, etc.), crie um superusuário:<br>

bash<br>
Copiar código<br>
python manage.py createsuperuser<br>
Siga as instruções para criar o superusuário.<br>
Passo 7: Rodar o Servidor<br>
Agora, você pode rodar o servidor de desenvolvimento do Django:<br>
bash<br>
Copiar código <br>
python manage.py runserver <br>
O servidor estará rodando em http://127.0.0.1:8000. Você pode acessar a API por meio de endpoints como http://127.0.0.1:8000/api/.<br>
<br>
Passo 8: Testar a API <br>
Com o servidor em execução, você pode interagir com os seguintes endpoints:<br>
<br>
POST [/api/auth/login/](http://127.0.0.1:8000/api/login): Realizar o login do usuário.<br> 
POST [/api/auth/register/](http://127.0.0.1:8000/api/create/usuario): Registrar um novo usuário.<br> 
GET /api/feed/: Ver o feed de postagens (inclui postagens próprias e de amigos). <br> 
POST [/api/postagem/](http://127.0.0.1:8000/api/criar/postagem/): Criar uma nova postagem.<br> 
POST [ [http://127.0.0.1:8000/api/curtida/postagem/](http://127.0.0.1:8000/api/curtida/postagem/): Curtir uma postagem.<br> 
POST [/api/postagem/comentario/](http://127.0.0.1:8000/api/postagem/comentario/): Comentar em uma postagem.<br> 
Passo 9: http://127.0.0.1:8000/api/login - Acessar o Admin (Opcional)<br> 
<br>
Se você criou um superusuário, pode acessar o painel administrativo em:arduino<br>
Copiar código <br>
http://127.0.0.1:8000/admin/ <br>
Faça login com o usuário e senha do superusuário para gerenciar as entidades do Django (Usuários, Postagens, Curtidas, etc.).<br>
<br> 
**Estrutura do Projeto</u>** 
Aqui está uma visão geral de como o projeto está estruturado:<br>

minx/
│
├── api_rest/                # Aplicativo Django onde estão as APIs<br> 
│   ├── migrations/          # Migrations do banco de dados<br>
│   ├── models.py            # Definição dos modelos (Postagem, Curtida, Comentario, etc.)<br>
│   ├── serializers.py       # Serializadores para transformar modelos em JSON<br>
│   ├── views.py             # Lógica das views e APIs<br>
│   ├── urls.py              # Configuração das rotas de URL<br>
│   └── tests.py             # Testes unitários<br>
│
├── api_root/                # Projeto Django raiz<br>
│   ├── settings.py          # Configurações do Django<br>
│   ├── urls.py              # Configuração das rotas principais<br>
│   └── wsgi.py              # Configuração WSGI para produção<br>
│
├── manage.py                # Script de gerenciamento do Django<br>
└── requirements.txt         # Dependências do projeto<br>

<br><br> 
