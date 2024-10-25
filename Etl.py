import requests
import pandas as pd
from sqlalchemy import create_engine


API_URL = "https://jsonplaceholder.typicode.com/posts"  
DB_NAME = "data_pipeline.db"  


def extract_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao acessar API: {response.status_code}")
        return None


def transform_data(data):
    df = pd.DataFrame(data)
    
 
    df['title_length'] = df['title'].apply(len)  
    return df


def load_data(df, db_name):
    engine = create_engine(f'sqlite:///{db_name}')
    with engine.connect() as conn:
        df.to_sql('api_data', conn, if_exists='replace', index=False)
    print("Dados carregados no banco de dados com sucesso!")


def run_pipeline():
 
    data = extract_data(API_URL)
    if data:
     
        transformed_data = transform_data(data)
        
 
        load_data(transformed_data, DB_NAME)
    else:
        print("Pipeline interrompido devido a erro na extração.")


if __name__ == "__main__":
    run_pipeline()
