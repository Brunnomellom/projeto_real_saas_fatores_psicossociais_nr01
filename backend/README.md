# 🧠 SaaS de Fatores Psicossociais

## 📌 Visão Geral

Este projeto consiste em um **SaaS para gestão, avaliação e monitoramento de fatores psicossociais no ambiente de trabalho**, alinhado às exigências legais e às boas práticas de Saúde e Segurança do Trabalho (SST).

A plataforma tem como objetivo auxiliar empresas e profissionais de SST a **identificar riscos psicossociais**, gerar relatórios técnicos e apoiar a tomada de decisão preventiva, promovendo ambientes de trabalho mais saudáveis e produtivos.

---

## 🎯 Objetivos do Projeto

* Automatizar a **avaliação de fatores psicossociais**
* Apoiar o cumprimento de normas e programas como **PGR**
* Centralizar dados e históricos de avaliações
* Gerar **relatórios claros e auditáveis**
* Facilitar a análise de riscos e planos de ação

---

## 🧩 Funcionalidades Principais

* Cadastro de empresas e setores
* Questionários de avaliação psicossocial
* Classificação de riscos (baixo, médio, alto)
* Geração de relatórios técnicos
* Histórico de avaliações
* Painel de indicadores (dashboards)
* Controle de usuários e permissões

---

## 🛠️ Tecnologias Utilizadas

### Backend

* **Python**
* **FastAPI**
* **Uvicorn**
* Arquitetura REST

### Banco de Dados

* Relacional (ex: PostgreSQL / SQLite em ambiente de desenvolvimento)

### Frontend *(em desenvolvimento / planejado)*

* Framework web moderno (ex: React)

### Outros

* Git & GitHub
* Docker *(planejado)*

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura baseada em **API REST**, separando responsabilidades e facilitando escalabilidade e manutenção.

* Camada de rotas (controllers)
* Camada de serviços (regras de negócio)
* Camada de dados (models e repositórios)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

* Python 3.10+
* Ambiente virtual (venv)

### Passos

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acessar o projeto
cd backend

# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar o servidor
uvicorn app.main:app --reload
```

---

## 📄 Documentação da API

Após iniciar o servidor, a documentação automática estará disponível em:

* **Swagger UI:** `http://localhost:8000/docs`
* **Redoc:** `http://localhost:8000/redoc`

---

## 📊 Contexto Legal

Este projeto está alinhado às diretrizes de **Saúde e Segurança do Trabalho**, especialmente no que se refere à gestão de riscos ocupacionais e fatores psicossociais previstos no **PGR**.

> ⚠️ *A plataforma é uma ferramenta de apoio e não substitui a atuação de profissionais legalmente habilitados.*

---

## 🧪 Status do Projeto

🚧 **Em desenvolvimento**

Funcionalidades estão sendo implementadas de forma incremental, seguindo boas práticas de versionamento e testes.

---

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas alterações
4. Abra um Pull Request

---

## 👨‍💻 Autor

**Bruno Melo**
Estudante de Engenharia de Software | Backend Python





ENGLISH

# 🧠 Psychosocial Factors SaaS

## 📌 Overview

This project is a **SaaS platform for managing, assessing, and monitoring psychosocial factors in the workplace**, aligned with legal requirements and best practices in Occupational Health and Safety (OHS).

The platform aims to support companies and OHS professionals in **identifying psychosocial risks**, generating technical reports, and supporting preventive decision-making, promoting healthier and more productive work environments.

---

## 🎯 Project Goals

* Automate **psychosocial risk assessments**
* Support compliance with regulations and programs such as **PGR**
* Centralize assessment data and historical records
* Generate **clear and auditable technical reports**
* Facilitate risk analysis and action planning

---

## 🧩 Main Features

* Company and department registration
* Psychosocial assessment questionnaires
* Risk classification (low, medium, high)
* Technical report generation
* Assessment history tracking
* Indicator dashboards
* User and permission management

---

## 🛠️ Technologies Used

### Backend

* **Python**
* **FastAPI**
* **Uvicorn**
* RESTful architecture

### Database

* Relational database (e.g., PostgreSQL / SQLite for development)

### Frontend *(in development / planned)*

* Modern web framework (e.g., React)

### Others

* Git & GitHub
* Docker *(planned)*

---

## 🏗️ Architecture

The project follows a **REST API–based architecture**, ensuring separation of concerns, scalability, and maintainability.

* Routing layer (controllers)
* Service layer (business rules)
* Data layer (models and repositories)

---

## 🚀 How to Run the Project

### Prerequisites

* Python 3.10+
* Virtual environment (venv)

### Steps

```bash
# Clone the repository
git clone https://github.com/your-username/your-repository.git

# Access the project directory
cd backend

# Create virtual environment
python -m venv venv

# Activate the environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

---

## 📄 API Documentation

After starting the server, the automatic API documentation will be available at:

* **Swagger UI:** `http://localhost:8000/docs`
* **Redoc:** `http://localhost:8000/redoc`

---

## 📊 Legal & Compliance Context

This project is aligned with **Occupational Health and Safety** guidelines, especially regarding occupational risk management and psychosocial factors addressed within the **PGR**.

> ⚠️ *This platform is a support tool and does not replace the work of legally qualified professionals.*

---

## 🧪 Project Status

🚧 **Under development**

Features are being implemented incrementally, following best practices for version control and testing.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the project
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes
4. Open a Pull Request

---

## 👨‍💻 Author

**Bruno Melo**
Software Engineering Student | Python Backend Developer

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more information.


---

## 📜 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.


