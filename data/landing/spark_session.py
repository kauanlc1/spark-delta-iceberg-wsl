from pyspark.sql import SparkSession


def create_spark_session():
    """
    Cria e retorna uma SparkSession configurada com suporte ao Delta Lake e Apache Iceberg.
    Essa função pode ser usada em qualquer notebook ou script.
    """

    spark = (
        SparkSession.builder
        .appName("Spark-Delta-Iceberg")  # Nome da aplicação (aparece no UI do Spark)
        # Extensões necessárias para habilitar Delta e Iceberg
        .config(
            "spark.sql.extensions",
            "io.delta.sql.DeltaSparkSessionExtension,org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
        )
        # Catálogo padrão para Delta
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        # Catálogo adicional para Iceberg (modo Hadoop)
        .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
        .config("spark.sql.catalog.local.type", "hadoop")
        .config("spark.sql.catalog.local.warehouse", "data/iceberg_warehouse")
        # Configurações de performance (opcionais)
        .config("spark.sql.shuffle.partitions", "4")
        .config("spark.sql.execution.arrow.pyspark.enabled", "true")
        .getOrCreate()
    )

    # Define o modo de log (INFO deixa limpo, DEBUG mostra tudo)
    spark.sparkContext.setLogLevel("INFO")

    print("✅ Spark Session inicializada com Delta e Iceberg!")
    print(f"Versão do Spark: {spark.version}")

    return spark


if __name__ == "__main__":
    # Permite testar o arquivo diretamente via terminal
    spark = create_spark_session()
    print("Sessão Spark criada com sucesso.")
    spark.stop()
