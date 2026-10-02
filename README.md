# Customer Intelligence Analytics

Projeto de análise de dados desenvolvido para simular um cenário real de Customer Intelligence em uma empresa de assinatura digital.

O projeto integra engenharia de dados, análise exploratória, SQL, Python, PostgreSQL e Business Intelligence.

## Objetivo

Identificar padrões de comportamento dos clientes, analisar churn, receita, utilização da plataforma e características relacionadas ao valor dos clientes.

## Tecnologias

- Python
- Pandas
- NumPy
- PostgreSQL
- SQL
- Power BI
- Matplotlib
- Docker
- Git
- GitHub

## Arquitetura

CSV
↓
Python / Pandas
↓
ETL
↓
PostgreSQL
↓
SQL Analytics
↓
Power BI

## Dataset

O dataset foi gerado sinteticamente com Python para simular uma base de clientes.

Principais informações:

- Cliente
- Idade
- Plano
- Canal de aquisição
- Região
- Horas de utilização
- Tickets de suporte
- Tempo como cliente
- Receita mensal
- Churn
- Receita acumulada

## Análises

O projeto investiga:

- Taxa geral de churn
- Churn por plano
- Churn por canal de aquisição
- Churn por região
- Relação entre utilização e churn
- Receita por plano
- Lifetime Revenue
- Segmentação de clientes
- Perfil de clientes de maior valor

## ETL

O processo de ETL é realizado utilizando Python e Pandas.

### Extract

Leitura dos dados brutos em CSV.

### Transform

- Tratamento de tipos
- Remoção de duplicidades
- Padronização de categorias
- Validação dos dados
- Criação de métricas

### Load

Carga dos dados tratados no PostgreSQL.

## Banco de dados

O PostgreSQL armazena os dados tratados e disponibiliza uma VIEW analítica utilizada posteriormente pelo Power BI.

## Dashboard

O dashboard foi desenvolvido no Power BI com foco em:

- KPIs
- Receita
- Churn
- Perfil dos clientes
- Segmentação
- Comportamento de utilização

## Principais perguntas de negócio

1. Qual é a taxa de churn?
2. Quais planos apresentam maior churn?
3. Quais canais trazem clientes com maior retenção?
4. Clientes com baixa utilização apresentam maior churn?
5. Quais segmentos possuem maior valor?
6. Qual é a receita mensal por plano?
7. Quais clientes apresentam maior lifetime revenue?

## Estrutura

```text
customer-intelligence-analytics/
│
├── data/
├── database/
├── src/
├── notebooks/
├── dashboard/
├── tests/
├── requirements.txt
├── docker-compose.yml
├── .gitignore
└── README.md