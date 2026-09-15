import psycopg2
import sqlite3

def create_connection():
    return psycopg2.connect(
        host="localhost",
        database="maindb",
        user="localuser",
        password="localuser"
    )
    
def create_connection_sqlite(uri:str):
    return sqlite3.connect(uri)