# Controle de Níveis de Água

## Descrição do Projeto

Este projeto foi desenvolvido como atividade do curso Técnico em Análise e Desenvolvimento de Sistemas (ADS) da ETEC.

O programa simula o monitoramento dos níveis de água de um reservatório, exibindo uma mensagem de acordo com o nível atual. Para facilitar a identificação, cada nível possui uma cor específica no terminal.

## Tecnologias Utilizadas

- Python
- Biblioteca Colorama
- Visual Studio Code

## Níveis do Reservatório

- **Nível 1:** Muito baixo (CRÍTICO) — Vermelho
- **Nível 2:** Baixo — Amarelo
- **Nível 3:** Médio — Verde
- **Nível 4:** Alto — Ciano
- **Nível 5:** Muito alto (ALERTA) — Azul

## Funcionamento

O programa utiliza uma função para determinar a cor correspondente ao nível do reservatório e exibe a mensagem no terminal.

A biblioteca Colorama permite utilizar cores no terminal, e o estilo é restaurado após a exibição da mensagem.

## Como Executar

1. Instale o Python.
2. Instale a biblioteca Colorama com o comando `python -m pip install colorama`.
3. Execute o programa com o comando `python main.py`.

## Autora

Valéria Lopes do Couto

Estudante do curso Técnico em Análise e Desenvolvimento de Sistemas (ADS) — ETEC.
