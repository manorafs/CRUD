import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

def conecta_banco():
    try:
        conexao = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("Conexão bem sucedida!")
        return conexao
    except Exception as e:
        print("Erro inesperado com a conexão do banco de dados")
        return None
    
conn = conecta_banco()
cur = conn.cursor()

    