# Projeto Animes Isekais

Este projeto coleta dados de animes e mangás utilizando a Jikan API. Os objetivos principais são:

- Obter os top 500 animes e mangás mais vistos.
- Coletar todos os dados disponíveis dos animes e mangás.
- Obter os animes lançados nos últimos 5 anos.

Após a coleta, serão realizadas análises dos dados.

## Estrutura do Projeto

- **data/**: Armazena os dados coletados.
- **src/**: Contém os módulos do projeto.
  - **config.py**: Configurações gerais.
  - **fetcher.py**: Funções para realizar requisições à API.
  - **main.py**: Orquestra a execução do projeto.
