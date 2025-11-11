# 🧩 Projeto: Apache Spark com Delta Lake e Apache Iceberg

> **Trabalho de Engenharia de Dados** — UniSatc  
> **Professor:** Jorge Silva  
> **Alunos:** Kauan Laureano Cândido e Lucas Ribeiro Guidi  
> **Tema:** Implementação prática de um pipeline de dados com Apache Spark, Delta Lake e Apache Iceberg utilizando Arquitetura Medalhão.

---

## 🧠 Sumário

- [1️⃣ Objetivo](#1️⃣-objetivo)
- [2️⃣ Arquitetura Geral](#2️⃣-arquitetura-geral)
- [3️⃣ Tecnologias Utilizadas](#3️⃣-tecnologias-utilizadas)
- [4️⃣ Estrutura do Projeto](#4️⃣-estrutura-do-projeto)
- [5️⃣ Como Reproduzir o Ambiente no WSL](#5️⃣-como-reproduzir-o-ambiente-no-wsl)
- [6️⃣ Notebooks e Camadas](#6️⃣-notebooks-e-camadas)
- [7️⃣ Integração com o Databricks](#7️⃣-integração-com-o-databricks)
- [8️⃣ Documentação (MKDocs)](#8️⃣-documentação-mkdocs)
- [9️⃣ Referências](#9️⃣-referências)

---

## 1️⃣ Objetivo

O objetivo deste trabalho é **demonstrar o uso prático das tecnologias Apache Spark, Delta Lake e Apache Iceberg**, aplicadas a um pipeline de dados baseado na **Arquitetura Medalhão** (Landing → Bronze → Silver → Gold). Isso envolve a criação de um **pipeline ETL completo**, onde utilizamos o **Delta Lake** para garantir transações ACID e o **Iceberg** para otimização de leitura e evolução do esquema.

O projeto tem como foco:
- Criar um ambiente **local** no WSL com Spark configurado para Delta e Iceberg;
- Implementar um **pipeline ETL completo** com uma tabela de vendas;
- Integrar o ambiente ao **Databricks** via GitHub;
- Documentar todo o processo com **MKDocs** e **README detalhado**.

---

## 2️⃣ Arquitetura Geral

```text
+----------------+      +----------------+      +----------------+      +----------------+
|    Landing     | ---> |     Bronze     | ---> |     Silver     | ---> |      Gold      |
| Dados Brutos   |      | Dados Dedup.   |      | Dados Limpos   |      | Dados Agreg.   |
+----------------+      +----------------+      +----------------+      +----------------+
        |                       |                       |                       |
        ▼                       ▼                       ▼                       ▼
   CSV/JSON Local          Delta Lake (MinIO)       Delta Lake (MinIO)       Delta Lake (MinIO)
```
## 3️⃣ Tecnologias Utilizadas
Tecnologia	Função
Python 3.12	Linguagem principal (PySpark)
Apache Spark 3.5.1	Motor de processamento distribuído
Delta Lake 3.1.0	Formato de tabela ACID
Apache Iceberg 1.5.2	Formato de tabela otimizado e evolutivo
MinIO	Armazenamento local compatível com S3
Docker	Execução isolada do MinIO
JupyterLab	Execução interativa dos notebooks
MKDocs + Material Theme	Documentação técnica
Databricks	Execução orquestrada em cloud (Jobs e Pipelines)

## 4️⃣ Estrutura do Projeto
```
spark-delta-iceberg-wsl/
├── src/
│   └── spark_session.py
├── data/
│   └── landing/
│       └── vendas.csv
├── notebooks/
│   ├── 01_landing_to_bronze.ipynb
│   ├── 02_bronze_to_silver.ipynb
│   ├── 03_silver_to_gold.ipynb
│   └── 04_delta_vs_iceberg_dml.ipynb
├── docs/
│   ├── index.md
│   ├── delta.md
│   └── iceberg.md
├── mkdocs.yml
├── pyproject.toml
└── README.md
```
## 5️⃣ Como Reproduzir o Ambiente no WSL
🔹 Atualizar e instalar dependências básicas
```
sudo apt update && sudo apt -y upgrade
sudo apt -y install git curl unzip build-essential
```
🔹 Instalar Java 17
```
sudo apt -y install openjdk-17-jdk
java -version
```
🔹 Instalar Python 3 + Virtual Env
```
sudo apt install -y python3 python3-venv python3-pip
```
🔹 Criar ambiente virtual
```
mkdir -p ~/dev/spark-delta-iceberg-wsl
cd ~/dev/spark-delta-iceberg-wsl
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```
🔹 Instalar Docker e configurar
```
sudo apt install -y ca-certificates curl gnupg lsb-release
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
```
🔹 Subir o MinIO
```
export MINIO_ROOT_USER=admin
export MINIO_ROOT_PASSWORD=admin12345

docker run -d --name minio \
  -p 9000:9000 -p 9001:9001 \
  -e MINIO_ROOT_USER=${MINIO_ROOT_USER} \
  -e MINIO_ROOT_PASSWORD=${MINIO_ROOT_PASSWORD} \
  -v $(pwd)/data/minio:/data \
  quay.io/minio/minio server /data --console-address ":9001"
  ```
  
Acesse: http://127.0.0.1:9001
Usuário: admin | Senha: admin12345

🔹 Criar bucket datalake
```
docker run --rm -it --network host \
  -e MC_HOST_local="http://${MINIO_ROOT_USER}:${MINIO_ROOT_PASSWORD}@127.0.0.1:9000" \
  quay.io/minio/mc mb local/datalake
  ```
  
## 6️⃣ Notebooks e Camadas

| **Camada**      | **Notebook**                        | **Descrição**                                           |
|-----------------|-------------------------------------|---------------------------------------------------------|
| **Landing → Bronze**  | `01_landing_to_bronze.ipynb`      | Lê CSV bruto e grava em Delta Lake                     |
| **Bronze → Silver**   | `02_bronze_to_silver.ipynb`      | Limpeza e transformação (tipos e deduplicação)          |
| **Silver → Gold**     | `03_silver_to_gold.ipynb`        | Agregação por estado                                   |
| **DML Delta/Iceberg** | `04_delta_vs_iceberg_dml.ipynb` | Comandos INSERT, UPDATE e DELETE                        |


## 7️⃣ Integração com o Databricks
- No menu lateral do Databricks → Repos → Add Repo
- Selecione GitHub e cole a URL deste repositório.
- Autorize o acesso via OAuth.
- Crie um Cluster (DBR 14.x LTS).
- Execute cada notebook na seguinte ordem:

01_landing_to_bronze
02_bronze_to_silver
03_silver_to_gold

- Em Workflows → Jobs, crie um job com as 3 tarefas em sequência.
- (Opcional) Monte um Pipeline Delta Live Tables usando os mesmos notebooks.
- (Lembrete) Certifique-se de configurar o Databricks workspace corretamente e adicionar os notebooks a partir do repositório GitHub, antes de rodar os Jobs

## 8️⃣ Documentação (MKDocs)
🧩 Instalação e execução local
```
pip install mkdocs mkdocs-material
mkdocs serve
```
Acesse em http://127.0.0.1:8000.

## 9️⃣ Referências

- [Delta Lake Official Docs](https://delta.io/)
- [Apache Iceberg Docs](https://iceberg.apache.org/)
- [Apache Spark Docs](https://spark.apache.org/docs/latest/)
- [MinIO Documentation](https://min.io/docs/)
- [DataWay BR (YouTube)](https://www.youtube.com/@DataWayBR)
