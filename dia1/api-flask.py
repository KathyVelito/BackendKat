from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

productos = [{
    "nombre":"Palta fuerte",
    "precio":5.80
},{
    "nombre":"Albahaca 100 gr.",
    "precio":0.80
}

]

@app.route("/")
def inicio():
    return{
        "message":"Bienvenido a mi API",
        "content":""
    }

@app.route("/productos", methods=['POST','GET'])
def gestion_productos():
    print(request.method)
    if request.method == 'GET':
        return{
            "message": None,
            "content":productos
        }

    elif request.method == 'POST':

        producto =request.get_json()
        productos.append(producto)

        return {
            "message": "Producto creado exitosamente",
            "content": producto
        }, 201


@app.route("/producto/<int:id>", methods=['GET'])
def gestion_producto(id):
    total_productos = len(productos)
    if id < total_productos:
        return {
            "content": productos[id],
            "message": None
        }, 200
    else:
        return {
            "message": "Producto no encontrado",
            "content": None
        }, 404


if __name__ == "__main__":
    app.run(debug=True)