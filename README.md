## 📌 Projeto 3 — Sistema de Atendimento FIFO

---

## 👥 Integrantes

- Ana Clara Miguel dos Santos
- Leonardo Franco de Almeida
- Vinicius Henrique de Souza Lima

---

## 🛠 Tecnologias Utilizadas

### Front-end
- HTML
- CSS
- JS

---

## ▶️ Instruções para Execução

Siga os passos abaixo na ordem correta para configurar e rodar o projeto localmente na sua máquina.

### 1. Inicializar o Banco de Dados (Docker)
O banco de dados PostgreSQL roda isolado dentro de um container Docker. Para iniciá-lo:
1. Certifique-se de que o **Docker Desktop** está aberto e rodando.
2. Abra o terminal na raiz do projeto (`SISTEMA_ATENDIMENTO_FIFO`).
3. Execute o comando para subir apenas o serviço do banco de dados em segundo plano:
   ```bash
   docker-compose up -d db

4. Acesse a pasta do backend:
    ```bash
   cd backend

5. Ative o seu ambiente virtual (caso já não esteja ativo):
    manual.txt

6. Instale as dependencias
    ```bash
    pip install -r requirements.txt

7. Inicie o servidor FastAPI local
    ```bash
    uvicorn main:app --reload --port 7000

8. Navegue até a pasta frontend/.

9. Abra o arquivo index.html e rode o codigo

---
## 📂 Estrutura de Pastas

```text
sistema-atendimento/
├── backend/
│   ├── main.py          # Ponto de entrada do FastAPI e inicialização do app
│   ├── controller.py    # Gerenciamento e lógica das rotas da API
│   ├── database.py      # Conexão com o banco de dados via SQLAlchemy
│   ├── model.py         # Modelos de tabela e Schemas do Banco de Dados
│   ├── node.py          # Implementação lógica dos Nós e da Fila (FIFO)
│   └── requirements.txt # Dependências do ecossistema Python
├── frontend/
│   ├── index.html       # Estrutura visual da interface do painel
│   ├── style.css        # Estilização e layout responsivo
│   └── app.js           # Consumo da API, manipulação do DOM e filtro de busca
├── docker-compose.yml   # Configuração do serviço de banco de dados PostgreSQL
└── README.md        