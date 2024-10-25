# Pipeline de Ingestão e Transformação de Dados de API para SQL

Este projeto implementa um pipeline de dados que extrai dados de uma API pública, transforma os dados para atender a requisitos específicos e carrega os dados em um banco de dados SQLite. Ele é ideal para aqueles que estão interessados em aprender ou demonstrar um exemplo básico de ETL (Extração, Transformação e Carregamento) na prática.

## Objetivos

- **Extração**: Obter dados de uma API REST.
- **Transformação**: Limpar e modificar dados com `pandas`.
- **Carregamento**: Inserir os dados transformados em um banco de dados SQLite.

## Estrutura do Código

- `extract_data(url)`: Extrai dados JSON de uma API REST.
- `transform_data(data)`: Converte os dados em um DataFrame e aplica transformações, como calcular o tamanho do título dos posts.
- `load_data(df, db_name)`: Carrega o DataFrame no banco de dados SQLite.
- `run_pipeline()`: Função principal que executa as etapas de Extração, Transformação e Carregamento.

## Tecnologias e Bibliotecas

- **Python 3**
- **requests**: Para realizar chamadas de API.
- **pandas**: Para transformação de dados.
- **SQLAlchemy**: Para conexão e manipulação de dados no SQLite.

## Instalação

 Instale as dependências:
    ```bash
    pip install requests pandas sqlalchemy
    ```

## Como Executar o Projeto

1. Modifique o URL da API em `API_URL` caso deseje usar outra fonte de dados.
2. Execute o pipeline:
    ```bash
    python main.py
    ```

Os dados serão armazenados em um banco de dados SQLite chamado `data_pipeline.db` na pasta raiz do projeto, com uma tabela chamada `api_data`.

## Resultados

Após a execução, você verá a tabela `api_data` criada no banco de dados SQLite com os seguintes campos:
- **userId**: ID do usuário que criou o post.
- **id**: ID do post.
- **title**: Título do post.
- **body**: Conteúdo do post.
- **title_length**: Número de caracteres no título.

## Melhorias Futuras

- Adicionar tratamento de erros e logs.
- Implementar uma solução de agendamento (ex.: Airflow) para automatizar a execução.
- Utilizar um banco de dados em nuvem para armazenar os dados.

## Contribuições

Sinta-se à vontade para abrir um PR ou relatar problemas. Toda contribuição é bem-vinda!

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
