import os
import pandas as pd
import sqlalchemy

BASE_DIR = 'C:\\Users\\SGG\\Desktop\\licitacon'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')

str_conn = "sqlite:///" + os.path.join(DATA_DIR, 'licitacon.db')
engine = sqlalchemy.create_engine(str_conn)
conn = engine.connect()

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = os.listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

arquivos = find_csv_filenames(DATA_DIR)

def store_banco(arquivo):
    nome = arquivo.replace(".csv", "")
    dados = pd.read_csv(    os.path.join(DATA_DIR, arquivo),
                            encoding= "utf-8")

    dados.to_sql(nome, conn)

for arquivo in arquivos:
    print("importando o arquivo {}").format(arquivo)
    try:
        store_banco(arquivo)
        print("aquivo {} importado com sucesso!").format(arquivo)
    except:
        print("Não foi possivel importar o aquivo {}").format(arquivo)