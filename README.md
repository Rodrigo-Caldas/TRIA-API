# TRIA-API
API para obtenção dos dados de precipitação diária.

![texto](https://img.shields.io/static/v1?label=3.13&message=python&color=green&style=flat-square "3.13")
![texto](https://img.shields.io/static/v1?label=ambiente&message=docker&color=blue&style=flat-square "ambiente")

## :world_map: Conteúdo
1. [O que o serviço faz?](#sparkles-O-que-o-serviço-faz)  
2. [Quais tecnologias posso usar?](#warning-Quais-tecnologias-posso-usar) 
3. [Como utilizar o serviço?](#pencil-Como-utilizar-o-serviço)

## :scroll: O que o serviço faz?

Repositório com a API do teste Técnico da Tria configurada. A API Lê os dados dos arquivos gerados e salvos da questão 1 na pasta ``src/chuva/arquivos``.

Possui endpoint para listar todos os dias disponíveis, a depender do código da estação.

As respostas de saída estão em json e a API possui um modelo de esquema de dados para lógica dos serviços.

## :warning: Quais tecnologias posso usar?

Há duas maneiras de executar este repositório, utilizando Python ou Docker.

- [Python](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)
- [Docker](https://docs.docker.com/engine/install/)

## :pencil: Como utilizar o serviço?

Execute o comando abaixo para clonar o repositório:

```bash  
git clone https://github.com/Rodrigo-Caldas/webhook-ons.git
```

É possível rodar a aplicação de duas formas: através da criação de ambiente python :snake: ou utilizando docker :whale:

### :snake: Via ``Python``

Crie um ambiente com o python 3.13 a partir do comando:

```bash 
python -m venv tria-api
```

Ative o ambiente a partir do comando:

```bash 
source tria-api/bin/activate
```

Instale as bibliotecas com:

```bash 
pip install -r requirements.txt
```

E por fim rode a aplicação com:

```bash
uvicorn src.main:app --reload
```

### :whale: Via ``Docker``

Para rodar a aplicação em um container, construa a imagem da aplicação a partir do comando:

```bash
docker build . -t tria-api
```

Com a imagem construída podemos criar o container onde a aplicação será rodada.

Execute o seguinte comando para executar o container:

```bash
docker run -t -p 8000:8000 tria-api
```