import pandas as pd
import json
from google import generativeai as genai

# API KEY de Gemini
genai.configure(
    api_key="AIzaSyAZHoy7-oqfBouuco7_202GWjqkDfDtRo0"
)
embedding_model_name = "gemini-3.1-flash-lite-preview"

model = genai.GenerativeModel(embedding_model_name)

def sanitizar_producto(texto):

    prompt = f"""
Eres un clasificador de productos para el catálogo SUNAT.

Tu trabajo es convertir una descripción comercial
en palabras clave genéricas para búsqueda.

Reglas:
- No inventes códigos SUNAT.
- No inventes categorías nuevas.
- Usa lenguaje de catálogo.
- Devuelve SOLO JSON válido.

Formato obligatorio:

{{
 "categoria":"",
 "familia":"",
 "clase":"",
 "producto":"",
 "keywords":[]
}}

Consulta:

{texto}

"""


    respuesta = model.generate_content(
        prompt
    )


    contenido = respuesta.text


    # quitar posibles bloques markdown
    contenido = contenido.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    )


    return json.loads(
        contenido.strip()
    )



# prueba

resultado = sanitizar_producto(
    "inka cola 1/2L"
)


print(
    json.dumps(
        resultado,
        indent=4,
        ensure_ascii=False
    )
)
texto_busqueda=" ".join(
    resultado["keywords"]
)


print(texto_busqueda)