Pipeline de Ingestão e Transformação de Dados de API para SQL
Este projeto implementa um pipeline de dados que extrai dados de uma API pública, transforma os dados para atender a requisitos específicos e carrega os dados em um banco de dados SQLite. Ele é ideal para aqueles que estão interessados em aprender ou demonstrar um exemplo básico de ETL (Extração, Transformação e Carregamento) na prática.

Objetivos
Extração: Obter dados de uma API REST.
Transformação: Limpar e modificar dados com pandas.
Carregamento: Inserir os dados transformados em um banco de dados SQLite.
Estrutura do Código
extract_data(url): Extrai dados JSON de uma API REST.
transform_data(data): Converte os dados em um DataFrame e aplica transformações, como calcular o tamanho do título dos posts.
load_data(df, db_name): Carrega o DataFrame no banco de dados SQLite.
run_pipeline(): Função principal que executa as etapas de Extração, Transformação e Carregamento.
Tecnologias e Bibliotecas
Python 3
requests: Para realizar chamadas de API.
pandas: Para transformação de dados.
SQLAlchemy: Para conexão e manipulação de dados no SQLite.
