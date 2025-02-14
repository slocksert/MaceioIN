# MaceioIN

Desafio para vaga de estágio FullStack

### O desafio está hospeado em [maceioin.slocksert.dev](https://maceioin.slocksert.dev).

    Usuário: admin
    Senha: admin

## Visão Geral

MaceioIN é uma aplicação FullStack composta por um frontend em Vue.js e um backend em Django. A aplicação permite gerenciar cadastros de pessoas da Secretaria da Fazenda, facilitando a atualização, consulta e manutenção dos registros.


## Screenshots

### Página Inicial
![Página Inicial](https://minio.slocksert.dev/images/landingpage.png)

### Login
![Login](https://minio.slocksert.dev/images/login.png)

### Gerenciamento de Usuários
![Gerenciamento de Usuários](https://minio.slocksert.dev/images/cadastro.png)

## Configuração do Ambiente

### Pré-requisitos

- Docker
- Docker Compose
- Node.js
- Python 3.12

### Configuração do Frontend (Vue.js)

1. Navegue até o diretório `maceioin_vue`:
    ```sh
    cd maceioin_vue
    ```

2. Instale as dependências do projeto:
    ```sh
    npm install
    ```

3. Para rodar o servidor de desenvolvimento:
    ```sh
    npm run serve
    ```

4. Para compilar e minificar para produção:
    ```sh
    npm run build
    ```

### Configuração do Backend (Django)

1. Navegue até o diretório `maceioin_django`:
    ```sh
    cd maceioin_django
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências do projeto:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente copiando o arquivo `.env_example` para `.env` e preenchendo os valores necessários:
    ```sh
    cp .env_example .env
    ```

5. Execute as migrações do banco de dados:
    ```sh
    python manage.py migrate
    ```

6. Para rodar o servidor de desenvolvimento:
    ```sh
    python manage.py runserver
    ```

7. Acesse a aplicação no navegador em `http://localhost:3307`.