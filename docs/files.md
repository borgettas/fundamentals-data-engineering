# Types
## Parquet
Parquet é um formato de arquivo colunar utilizado para armazenar dados de forma eficiente, especialmente em ambientes de big data. Ele foi desenvolvido pela Apache Software Foundation e é amplamente utilizado em sistemas de processamento de dados como Apache Hadoop e Apache Spark.

As principais características do Parquet incluem:

1. **Armazenamento Colunar**: Os dados são armazenados em colunas em vez de linhas, o que permite uma leitura mais eficiente, especialmente para consultas que envolvem apenas algumas colunas de um grande conjunto de dados.

2. **Compressão**: O Parquet suporta várias técnicas de compressão, o que ajuda a reduzir o espaço de armazenamento e a melhorar a performance de leitura.

3. **Esquema Flexível**: O formato permite que os dados sejam armazenados com um esquema que pode ser evoluído ao longo do tempo, facilitando a adição de novas colunas sem a necessidade de reescrever todo o conjunto de dados.

4. **Compatibilidade**: O Parquet é compatível com várias linguagens de programação e ferramentas de análise de dados, tornando-o uma escolha popular para armazenamento de dados em ambientes de análise e machine learning.


# Compression

## Snappy

A compressão Snappy é um algoritmo de compressão desenvolvido pelo Google, projetado para ser rápido e eficiente em termos de desempenho, em vez de maximizar a taxa de compressão. Ele é especialmente útil em cenários onde a velocidade de leitura e escrita é mais crítica do que a redução máxima do tamanho do arquivo.

1. **Velocidade**: O Snappy é otimizado para compressão e descompressão rápidas, o que o torna ideal para aplicações que precisam processar grandes volumes de dados em tempo real.

2. **Taxa de Compressão**: Embora o Snappy não ofereça a melhor taxa de compressão em comparação com outros algoritmos (como Gzip ou LZ4), ele ainda consegue reduzir o tamanho dos dados de forma eficaz, mantendo um bom equilíbrio entre velocidade e eficiência.

3. **Uso em Big Data**: O Snappy é amplamente utilizado em sistemas de big data, como Apache Hadoop e Apache Parquet, onde a velocidade de processamento é crucial. Ele é frequentemente escolhido para compressão de dados em ambientes de análise e armazenamento.

4. **Simplicidade**: O algoritmo é relativamente simples de implementar e usar, o que contribui para sua popularidade em várias aplicações.

Em resumo, a compressão Snappy é uma escolha popular em cenários onde a velocidade de processamento é mais importante do que a compressão máxima, tornando-a ideal para aplicações de big data e análise de dados.