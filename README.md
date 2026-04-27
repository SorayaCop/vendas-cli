# vendas-cli

Ferramenta de linha de comando desenvolvida em Python para processar arquivos CSV de vendas e gerar relatórios consolidados, com foco em organização de código, boas práticas e qualidade de software.

---

## Funcionalidades

- Leitura de arquivos CSV
- Cálculo do faturamento total geral
- Total de vendas por produto
- Identificação do produto mais vendido
- Filtro por período (`--start` e `--end`)
- Saída em formato texto
- Saída em formato JSON
- Arquitetura modular
- Tipagem estática com `typing`
- Logs de execução com `logging`
- Testes automatizados com alta cobertura

---

## Estrutura do Projeto

src/vendas_cli/<br>
├── cli.py<br>
├── parser.py<br>
├── core.py<br>
└── output.py

---


## Instalação

pip install -e .


---


## Relatório em JSON

vendas-cli sample_vendas.csv --format json


---


## Filtro por período

vendas-cli sample_vendas.csv --start 2026-04-01 --end 2026-04-02

## JSON com filtro por período

vendas-cli sample_vendas.csv --format json --start 2026-04-01 --end 2026-04-02


---


## Exemplo de CSV

data,produto,quantidade,valor<br>
2026-04-01,Notebook Dell,2,4500.00<br>
2026-04-01,Monitor LG 27,1,1200.00<br>
2026-04-02,Teclado Mecânico,3,350.00<br>
2026-04-02,Mouse Logitech,4,180.00


---


## Testes

pytest


## Cobertura de Testes

pytest --cov=src/vendas_cli --cov-report=term-missing 
<br>
Cobertura atual: 95%


---


## Tecnologias Utilizadas

- Python 3.13
- Pytest
- Pytest-cov
- argparse
- csv
- logging
- decimal


---



## Objetivo

Projeto desenvolvido como solução técnica para processamento de dados via linha de comando, demonstrando capacidade de construção de ferramentas backend com código limpo, modular e testável.
