from flask import Flask, jsonify,request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/descripcion/generar", methods=["POST"])
def obtener_usuario():
    data:dict = request.json
    contexto = data.get("contexto","")
    pais = data.get("pais","")
    articulos:list= data.get("articulos",[])
    response = []
    print(articulos)
    for i,articulo in enumerate(articulos):
        if articulo[0] == None or articulo[1] == None:
            return f"formato incorrecto en la posicion {i}",404
        
        response.append([articulo[0],"texto generico"])
    if len(articulos) == 0: return "no se encontro articulos",404
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
