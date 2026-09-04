from fastapi import FastAPI, Depends
from conexion import get_connection,initdb
from sqlite3 import Connection
from inventario import inventario
from modelos import Producto

accionesDeInventario = inventario()

app = FastAPI()

@app.on_event("startup")
def startup():
    print("iniciando base de datos")
    initdb()

@app.post("/agregar_producto")
def agregar_al_inventario(producto: Producto, conan: Connection = Depends(get_connection)):
    return  inventario.agrega_producto(producto, conan)

@app.get("/leer_productos")
def getproductos(conan:Connection= Depends(get_connection)):
    return inventario.leer_inventario()

@app.delete("/elimar_producto /{id}")
def delete_prod(id : int, conan:Connection = Depends(get_connection)):
    return inventario.eliminar_producto()

@app.put("/actualizar_producto")
def update_product( id : int,producto : Producto, conan : Connection = Depends(get_connection)):
    return inventario.actualizar_producto()