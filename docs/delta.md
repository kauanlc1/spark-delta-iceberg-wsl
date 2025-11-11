# Delta Lake

**Delta Lake** é um formato de armazenamento de dados otimizado para o **Apache Spark**. Ele adiciona garantias de **transações ACID** (Atomicidade, Consistência, Isolamento e Durabilidade) a sistemas de Big Data, possibilitando que as operações sobre grandes volumes de dados sejam mais seguras e eficientes. Com o **Delta Lake**, é possível criar Data Lakes robustos e com alta confiabilidade.

## Funcionalidades

### Transações ACID
O Delta Lake oferece transações de leitura e escrita em tempo real, garantindo que todas as operações de dados sigam os princípios ACID.

### Versionamento de Dados
Delta Lake mantém um histórico completo de todas as alterações de dados. Isso permite a execução de consultas em versões anteriores dos dados (conhecido como **Time Travel**) e oferece a capacidade de realizar rollback em transações.

### Schema Enforcement e Evolution
O Delta Lake permite validar o esquema dos dados para garantir que eles atendam a um formato pré-definido e, ao mesmo tempo, suporta a evolução do esquema ao longo do tempo, sem interromper os processos de ingestão de dados.

## Benefícios

- **Alta confiabilidade** com suporte a transações ACID.
- **Fácil integração** com Apache Spark.
- **Escalabilidade**: Suporta grandes volumes de dados distribuídos.
- **Ajuste dinâmico de esquemas**: Suporta mudanças nos dados com o tempo.
- **Capacidade de voltar no tempo** com o Time Travel.

Para mais detalhes sobre como utilizar o Delta Lake, veja a documentação oficial: [Delta Lake Documentation](https://docs.delta.io/latest/index.html).
