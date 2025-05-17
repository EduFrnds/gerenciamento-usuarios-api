# API de Gerenciamento de Usuários

API REST para gerenciamento de usuários construída com FastAPI, SQLite e Arquitetura Hexagonal.

## Características

- Framework web: FastAPI
- Banco de dados: SQLite
- Arquitetura: Hexagonal (Ports and Adapters)
- Autenticação: JWT - *Não implementado*
- Testes unitários - *Não implementado*
- Documentação automática da API

## Requisitos

- Python 3.10+
- SQLite 3

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/api-gerenciamento-usuarios.git
cd api-gerenciamento-usuarios
```

2. Configure o ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
DEBUG=True
SECRET_KEY=sua_chave_secreta_aqui
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./app.db
DEFAULT_PAGE_SIZE=10
MAX_PAGE_SIZE=100
```

## Execução

Para iniciar o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://localhost:8000`.

## Documentação da API

A documentação da API estará disponível em:

- Swagger UI: `http://localhost:8000/docs`
- OpenAPI JSON: `http://localhost:8000/api/v1/openapi.json`

## Estrutura do Projeto

```
gerenciamento-usuarios-api/
│
├── .venv/                                          # Ambiente virtual
│
├── app/                                            # Código do aplicativo
│ ├── adapters/                                     # Adaptadores para repositórios e interfaces
  │ ├── configs/                                    # Configurações do projeto
│ │ └── settings.py                                 # Configurações principais
│ ├── domain/                                       # Lógica de domínio
│ │ └── models.py                                   # Modelos de domínio
│ ├── infra/                                        # Infraestrutura do projeto
│ │ └── ports/                                      # Portas de comunicação
│ ├── interface/                                    # Interfaces de entrada
│ │ └── routers/                                    # Roteadores da API
│ │ └── init.py                                     # Inicialização do módulo
│ ├── logs/                                         # Logs do aplicativo
│ │ ├── init.py                                     # Inicialização do módulo de logs
│ │ └── main.db                                     # Banco de dados principal
│ └── main.py                                       # Ponto de entrada do aplicativo
└── .env                                            # Variáveis de ambiente
```

## Arquitetura Hexagonal

Este projeto segue a Arquitetura Hexagonal (também conhecida como Ports and Adapters), que separa o domínio da aplicação de suas dependências externas. A estrutura é organizada em:

- **Domínio**: Contém as regras de negócio, entidades e serviços.
- **Portas**: Interfaces que definem como o domínio se comunica com o mundo externo.
- **Adaptadores**: Implementações concretas das portas, conectando o domínio com tecnologias específicas.

## Endpoints da API

### Usuários

- `GET /api/v1/users` - Listar usuários (paginado)
- `POST /api/v1/users` - Criar um novo usuário
- `GET /api/v1/users/{user_id}` - Obter usuário por ID
- `PUT /api/v1/users/{user_id}` - Atualizar usuário
- `DELETE /api/v1/users/{user_id}` - Remover usuário

## Testes - Não implementados

Para executar os testes unitários:

```bash
pytest
```
