import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

def create_connection():
    return psycopg2.connect(
        host="localhost",
        database="maindb",
        user="localuser",
        password="localuser"
    )

df = pd.read_excel("./catalogo25.xlsx")


## INSERTAR SEGMENTOS

sub_df = df.drop_duplicates(subset=["ID SEGMENTO"])

conn = create_connection()
cur = conn.cursor()

query = """
INSERT INTO segmento (id,descripcion)
VALUES %s
"""
datos = list(sub_df[["ID SEGMENTO","SEGMENTO"]].itertuples(index=False, name=None))

try: 
    execute_values(cur,query,datos)
    conn.commit()
except Exception as e: print(e)

cur.close()
conn.close()

## INSERTAR FAMILIA

sub_df = df.drop_duplicates(subset=["ID FAMILIA"])

conn = create_connection()
cur = conn.cursor()

query = """
INSERT INTO familia (id,segmento_id,descripcion)
VALUES %s
"""
datos = list(sub_df[["ID FAMILIA","ID SEGMENTO","FAMILIA"]].itertuples(index=False, name=None))

try: 
    execute_values(cur,query,datos)
    conn.commit()
except Exception as e: print(e)

cur.close()
conn.close()

## INSERTAR CLASE

sub_df = df.drop_duplicates(subset=["ID CLASE"])

conn = create_connection()
cur = conn.cursor()

query = """
INSERT INTO clase (id,familia_id,descripcion)
VALUES %s
"""
datos = list(sub_df[["ID CLASE","ID FAMILIA","CLASE"]].itertuples(index=False, name=None))

try:
    execute_values(cur,query,datos)
    conn.commit()
except Exception as e: print(e)

cur.close()
conn.close()

## INSERTAR ARTICULOS

sub_df = df.drop_duplicates(subset=["ID PRODUCTO"])

conn = create_connection()
cur = conn.cursor()

query = """
INSERT INTO producto (id,clase_id,descripcion)
VALUES %s
"""
datos = list(sub_df[["ID PRODUCTO","ID CLASE","PRODUCTO"]].itertuples(index=False, name=None))

try:
    execute_values(cur,query,datos)
    conn.commit()
except Exception as e: print(e)

cur.close()
conn.close()