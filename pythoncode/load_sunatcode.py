from src.basemodel import Capa, Clasificacion,Familia,Articulo,Segmento,Clase,Recomendacion
import os
import pandas as pd
from dotenv import load_dotenv
from google import genai
import psycopg2
from src.database import create_connection
from src.ai import generate_prompt,generar_familias_prompt, generar_clases_prompt, generar_productos_prompt
import json

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_IA_MODEL = os.getenv("GEMINI_IA_MODEL")

client = genai.Client(api_key=GEMINI_API_KEY)

segmentos:list[Segmento] = []
articulos: list[Articulo] = []
familias: list[Familia] = []
clases:list[Clase] = []

capa1_segmentos:dict[str,Capa[Segmento]] = {}
capa2_familias:dict[str,Capa[Familia]] = {}
capa3_clases:dict[str,Capa[Clase]] = {}
capa4_productos:dict[str,Capa[Articulo]] = {}

catalogo: dict[str,list[Familia]] = []

capa0_inputs = [
    Articulo("adajk","coca cola 1/2"),
    Articulo("calmkllwa","gaseosa kr 300 ml"),
    Articulo("aadac","cuarto de pollo"),
    Articulo("alwekmav","delivery domicilio"),
    Articulo("acmwakoi","chaufa + pollo"),
    Articulo("aaasdc","tallarin saltado")
]