from __future__ import annotations
from pydantic import BaseModel
from typing import Generic, TypeVar
import psycopg2


class Clasificacion(BaseModel):
    id_articulo: int
    id_grupo: int
    confianza: float
    
class basicIdentificated():
    def __init__(self,id:str,nombre:str):
        self.id = id
        self.nombre = nombre
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.id})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"

V = TypeVar("V")
S = TypeVar("S")

class Capa(Generic[V]):
    items:list[Articulo] = []
    subcapas:dict = {}
    def __init__(self,value:V|None = None,index:int|None = None):
        self.value = value
        self.index = index
        
    def __repr__(self):
        return f"Capa<{V.__name__}>(index:{self.index},items:{self.items},sub:{self.subcapas})"

class Segmento(basicIdentificated):
    familias:list[Familia]=[]
class Familia(basicIdentificated): pass
class Clase(basicIdentificated): pass
class Articulo(basicIdentificated): pass

