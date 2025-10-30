# Projeto Spark + Delta Lake + Iceberg + MinIO

## Objetivo
Este projeto implementa uma arquitetura de dados utilizando Apache Spark, Delta Lake, Iceberg e MinIO, simulando um **Data Lakehouse** com tabelas gerenciadas e não gerenciadas.

### Tecnologias Utilizadas
- **Apache Spark**
- **Delta Lake** (para transações ACID)
- **Iceberg** (formato de tabela otimizado)
- **MinIO** (S3 local)
- **Python 3.12** (pyspark, delta-spark, pyiceberg)
- **Docker** (para rodar o MinIO)

## Configuração do Ambiente
1. **Instalar Docker**:
   - [Seguir os passos no Docker WSL](https://docs.docker.com/desktop/install/windows-install/)
2. **Instalar Python 3.12**:
   - `sudo apt install python3 python3-venv python3-pip`
3. **Criar e ativar o ambiente virtual**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
