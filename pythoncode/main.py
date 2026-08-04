# %%
import pandas as pd
import pymysql
import re
from unidecode import unidecode


conexion = pymysql.connect(
    host="localhost",
    user="noroot",
    password="N@Root123",
    database="sunat",
    charset="utf8mb4"
)

cursor = conexion.cursor()

def limpiar(texto):

    if pd.isna(texto):
        return ""

    texto=str(texto).lower()

    texto=unidecode(texto)

    texto=re.sub(
        "[^a-z0-9 ]",
        " ",
        texto
    )

    texto=re.sub(
        "\s+",
        " ",
        texto
    )

    return texto.strip()



# -------------------------
# Crear keywords
# -------------------------

stopwords=[
    "de",
    "la",
    "el",
    "los",
    "las",
    "para",
    "con",
    "y"
]


def generar_keywords(texto):

    palabras=texto.split()

    resultado=[]

    for p in palabras:

        if len(p)>2 and p not in stopwords:
            resultado.append(p)


    return " ".join(
        sorted(set(resultado))
    )



# -------------------------
# Leer Excel
# -------------------------

df=pd.read_excel(
    "catalogo25.xlsx"
)


# -------------------------
# Insertar
# -------------------------

sql="""

INSERT INTO catalogo25
(
id_segmento,
segmento,

id_familia,
familia,

id_clase,
clase,

id_producto,
producto,

descripcion_busqueda,
keywords

)

VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

"""


contador=0


for _,fila in df.iterrows():


    descripcion=limpiar(

        f"{fila['SEGMENTO']} "
        f"{fila['FAMILIA']} "
        f"{fila['CLASE']} "
        f"{fila['PRODUCTO']}"

    )


    keywords=generar_keywords(
        descripcion
    )


    datos=(

        fila["ID SEGMENTO"],
        fila["SEGMENTO"],

        fila["ID FAMILIA"],
        fila["FAMILIA"],

        fila["ID CLASE"],
        fila["CLASE"],

        fila["ID PRODUCTO"],
        fila["PRODUCTO"],

        descripcion,
        keywords

    )


    cursor.execute(
        sql,
        datos
    )


    contador+=1


    if contador % 1000==0:
        conexion.commit()
        print(
            "Insertados:",
            contador
        )



conexion.commit()

cursor.close()
conexion.close()


print("Proceso terminado")
# %%
