from flask import Blueprint, jsonify, request

descripcion_bp = Blueprint(
    "descripcion",
    __name__,
    url_prefix="/api/descripcion"
)

@descripcion_bp.post("/test")
def test():
    return jsonify([])

@descripcion_bp.post("/generar")
def generar():
    data:dict = request.json
    pais:str|None = None
    rubro:str|None = None
    contexto: dict|None = data.get("contexto")
    if contexto:
        pais = contexto.get("pais")
        rubro = contexto.get("rubro")
        
    articulos:list= data.get("articulos",[])
    response = []
    
    for i,articulo in enumerate(articulos):
        if articulo[0] == None or articulo[1] == None:
            return f"formato incorrecto en la posicion {i}",404
        response.append([articulo[0],"texto generico"])
    
    if len(articulos) == 0: return "no se encontro articulos",404
    return jsonify(response)