### Descrição do Projeto

---

**Nome do Projeto:** Comunidade Flask

**Descrição:** Este é um projeto web desenvolvido com Flask, que é um micro framework para Python. O projeto possui funcionalidades típicas de uma aplicação de comunidade online, onde usuários podem criar contas, fazer login, criar posts, editar perfis, e interagir uns com os outros.

---

**Estrutura do Projeto:**

- **comunidade/**
  - **static/**: Diretório para arquivos estáticos (CSS, JavaScript, imagens).
  - **templates/**: Diretório para templates HTML.
    - `404.html`: Página de erro 404.
    - `base.html`: Template base para todas as páginas.
    - `contato.html`: Página de contato.
    - `criar_post.html`: Página para criação de posts.
    - `editarperfil.html`: Página para edição de perfil.
    - `home.html`: Página inicial.
    - `login.html`: Página de login.
    - `navbar.html`: Barra de navegação.
    - `perfil.html`: Página de perfil de usuário.
    - `post.html`: Página de visualização de post.
    - `usuarios.html`: Página de listagem de usuários.
  - `__init__.py`: Arquivo de inicialização do pacote.
  - `forms.py`: Formulários da aplicação.
  - `models.py`: Modelos do banco de dados.
  - `routes.py`: Rotas da aplicação.

- **env/**: Ambiente virtual para dependências do projeto.

- **images/**: Diretório para armazenamento de imagens.

- **instance/**
  - `createdatbase.py`: Script para criação do banco de dados.
  - `geradodepost.py`: Script para geração de posts.

- `main.py`: Arquivo principal para execução da aplicação.
- `Procfile`: Arquivo de configuração para deploy no Heroku.
- `requirements.txt`: Arquivo com as dependências do projeto.

---

**Tecnologias Utilizadas:**
- Flask (framework web)
- Jinja2 (template engine)
- SQLAlchemy (ORM)
- WTForms (formulários)
- HTML, CSS, JavaScript

**Funcionalidades:**
- Autenticação de usuários (registro, login, logout)
- Criação, edição e visualização de posts
- Edição de perfil de usuário
- Contato
- Listagem de usuários
- Página de erro personalizada

---

**Como Executar:**
1. Clone o repositório:
   ```sh
   git clone https://github.com/seuusuario/seurepositorio.git
   ```
2. Crie e ative o ambiente virtual:
   ```sh
   python -m venv env
   source env/bin/activate  # No Windows use `env\Scripts\activate`
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```sh
   python main.py
   ```


### Vídeo
Para uma visão mais detalhada, assista ao vídeo de demonstração:

<p align="center">
  <a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7212155396642267136/" target="_blank">
    Assista ao vídeo
  </a>
</p>
