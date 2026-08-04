import psycopg2

def create_connection():
    return psycopg2.connect(
        host="localhost",
        database="maindb",
        user="localuser",
        password="localuser"
    )