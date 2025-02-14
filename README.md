# MaceioIN

Desafio para vaga de estágio FullStack

### O desafio também está hospeado em [maceioin.slocksert.dev](https://maceioin.slocksert.dev).

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

### Usando MySQL com Docker Compose

1. Certifique-se de que o Docker e o Docker Compose estão instalados.

2. No diretório raiz do projeto, execute o comando:
    ```sh
    docker-compose up -d
    ```

3. Configure as variáveis de ambiente no arquivo `.env` para usar o MySQL:
    ```env
    USE_MYSQL=True
    NAME=MaceioIN
    USER=root
    PASSWORD=root
    HOST=mysql_db
    PORT=3306
    ```

4. Execute as migrações do banco de dados:
    ```sh
    python manage.py migrate
    ```

5. Acesse a aplicação no navegador em `http://localhost:3307`.