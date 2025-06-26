# 📬 Estudo Flask

Projeto feito através de um curso do canal [Camp Code](https://www.youtube.com/@campcodebrasil), com foco em criar um sistema simples de autenticação, cadastro de contatos e publicações com fotos e comentários usando Flask. Ideal para praticar rotas e templates.

## 🚀 Funcionalidades

- Autenticação de usuários com login e cadastro
- Página de contato:
  - Enviar nome, e-mail, assunto e mensagem
- Lista de contatos:
  - Visualizar todos os contatos e seus detalhes
- Página de posts:
  - Criar um novo post com texto e imagem
  - Listar todos os posts
  - Visualizar post completo com possibilidade de comentar

## 🛠 Tecnologias Utilizadas

- Python
- Flask
- Jinja2
- SQLite
- HTML + CSS
- Bootstrap

## ⚙️ Variáveis de Ambiente

Antes de rodar a aplicação, crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
SECRET_KEY=sua_chave_secreta_aqui
DATABASE_URI=sqlite:///database.db
```

## 💻 Como Rodar Localmente

```bash
# clone o repositorio
git clone https://github.com/Ivysonin/Flask_exercise.git

# Crie o ambiente virtual
python -m venv venv

# Ative no Windows
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor
python main.py
```

## 🌐 Projeto Online

Acesse o sistema em: [https://estudo-flask-ivyson.onrender.com/](https://estudo-flask-ivyson.onrender.com/)
> ⚠️ Aviso: Este projeto está hospedado no Render (plano gratuito). Após 15 minutos de inatividade, o serviço pode ser temporariamente suspenso e levar alguns segundos para voltar ao ar.

## 📖 Aprendizados

Durante o desenvolvimento deste projeto, tive a oportunidade de praticar e consolidar diversos conceitos importantes do ecossistema Flask e do desenvolvimento web em geral, incluindo:

- Estruturação de aplicações Flask com múltiplas rotas e templates
- Manipulação de formulários e envio de dados via POST
- Integração com banco de dados usando SQLite
- Upload e tratamento de imagens no backend
- Conceitos de autenticação e controle de sessão
- Deploy de aplicações Flask na nuvem com Render
- Uso de variáveis de ambiente para manter configurações sensíveis fora do código

Esse projeto serviu como um ótimo laboratório para colocar a mão na massa e entender como várias peças do backend se conectam na prática.
