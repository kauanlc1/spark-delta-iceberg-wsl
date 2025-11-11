# Bem-vindo ao Projeto Spark Delta Iceberg WSL

Este repositório contém a implementação de um pipeline de dados utilizando **Apache Spark**, **Delta Lake** e **Apache Iceberg**, sendo executado no ambiente **WSL (Windows Subsystem for Linux)** com **Ubuntu**. O pipeline segue a arquitetura medalhão, com as camadas **Landing**, **Bronze**, **Silver** e **Gold**.

## Sumário

- [Objetivo](#objetivo)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Delta Lake](delta.md)
- [Apache Iceberg](iceberg.md)
- [Referências](referencias.md)

## Objetivo

O objetivo deste projeto é implementar uma solução de pipeline de dados que utiliza o **Apache Spark** para processar grandes volumes de dados de maneira eficiente, enquanto aproveita as vantagens do **Delta Lake** e **Apache Iceberg** para garantir a integridade, performance e a confiabilidade das transações em ambientes de Big Data.

## Tecnologias Utilizadas

- **Apache Spark**: Framework de processamento distribuído para Big Data.
- **Delta Lake**: Formato de tabela ACID para garantir transações consistentes em grandes volumes de dados.
- **Apache Iceberg**: Formato de tabela projetado para Big Data com suporte a transações ACID e otimização de desempenho.
- **WSL**: Subsystem para Linux no Windows, utilizando **Ubuntu**.

## Estrutura do Projeto

O pipeline de dados é dividido em 4 camadas principais:

- **Landing**: Recebe os dados brutos, diretamente do ponto de origem.
- **Bronze**: Processamento inicial e limpeza dos dados.
- **Silver**: Refino dos dados para análise.
- **Gold**: Dados prontos para consumo por sistemas de análise e BI.

Cada camada pode ser consultada e verificada diretamente através dos arquivos Delta Lake e Iceberg.
