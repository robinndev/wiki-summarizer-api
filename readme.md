# Wikipedia Summarizer LLM API

API para resumir artigos da Wikipedia usando LLM (Large Language Model).

## Tecnologias

- Python 3.11
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Docker / Docker Compose
- OpenAI API

---

## Pré-requisitos

- Docker e Docker Compose instalados na máquina

---

## Setup rápido

1. **Clonar o repositório**

```bash
git clone <URL_DO_REPO>
cd <NOME_DO_REPO>
```

2. **Criar arquivo `.env`**
   No diretório raiz, criar um arquivo `.env` com as variáveis:

```env
ENV=production
OPENAI_API_KEY=<SUA_CHAVE_OPENAI>
DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/summaries_db
```

> Importante: `db` é o nome do serviço PostgreSQL do Docker Compose. Não use `localhost` dentro do Docker.

3. **Rodar containers com Docker Compose**

```bash
docker-compose up --build
```

Isso vai subir:

- **PostgreSQL** em `db:5432`
- **API** em `http://localhost:8000`

4. **Testar a API**

```bash
curl http://localhost:8000/
```

Deve retornar algo como:

```json
{ "status": "ok" }
```

---

## Endpoints principais

### `POST /summaries/`

Cria ou retorna um resumo de uma URL da Wikipedia.

**Exemplo de requisição com `curl`:**

```bash
curl --location 'http://127.0.0.1:8000/summaries/' \
--header 'Content-Type: application/json' \
--data '{
    "url": "https://en.wikipedia.org/wiki/GitHub",
    "max_words": 400
}'
```

---

### `GET /summaries/cache`

Verifica se o resumo de uma URL já existe no cache/banco, sem gerar um novo.

**Exemplo de requisição com `curl`:**

```bash
curl --location 'http://127.0.0.1:8000/summaries/cache?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FGitHub' \
--header 'Accept: application/json'
```

---

### `GET /health`

Verifica se a API está funcionando corretamente.

**Exemplo de requisição com `curl`:**

```bash
curl --location 'http://127.0.0.1:8000/' \
--header 'Accept: application/json'
```

---

## Rodando localmente (sem Docker)

Se você quiser rodar a API diretamente no seu ambiente Python:

1. **Criar um virtualenv** (recomendado)

```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate
```

2. **Instalar dependências**

```bash
pip install -r requirements.txt
```

3. **Configurar variáveis de ambiente**

Crie um arquivo `.env` como no passo anterior:

```env
ENV=development
OPENAI_API_KEY=<SUA_CHAVE_OPENAI>
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/summaries_db
```

> Atenção: nesse caso o banco precisa estar rodando localmente em `localhost`.

4. **Rodar a aplicação**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

5. **Acessar a API**

Abra: `http://localhost:8000/`

---

## Testes

Para garantir que tudo está funcionando e evitar regressões, você pode rodar os testes automatizados:

1. **Instalar dependências de testes**

```bash
pip install -r requirements-test.txt
```

2. **Rodar os testes**

```bash
pytest -v
```

3. **Rodar testes específicos** (exemplo: apenas para `summaries`)

```bash
pytest tests/test_summaries.py -v
```

> Dica: Se estiver usando Docker, você também pode rodar testes dentro do container da API:

```bash
docker-compose run --rm api pytest -v
```
