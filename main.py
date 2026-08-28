from fastapi import FastAPI
from pydantic import BaseModel
from conexion import get_connection,initdb
app = FastAPI()

class Producto(BaseModel):
    nombre : str
    stock : int
    precio : float

@app.on_event("startup")
def startup():
    print("iniciando base de datos")
    initdb()

@app.post("/agregar_producto")
def postproduct(producto : Producto):
    conexion = get_connection()
    conexion.execute("INSERT INTO productos(nombre, stock, precio) VALUES (?,?,?)",
    (producto.nombre, producto.stock, producto.precio))
    conexion.commit()
    conexion.close()
    return  f"dato subido{producto}"


@app.get("/leer_productos")
def getproductos():
    conexion = get_connection()
    res = conexion.execute("SELECT * FROM productos").fetchall()
    return ([dict(item)for item in res])


@app.delete("/elimar_producto /{id}")
def delete_prod(id : int):
    conexion = get_connection()
    conexion.execute("DELETE FROM productos WHERE id = ?",(id,))
    conexion.commit()
    conexion.close()
    return f"se elimmino el producto de id {id}"

@app.put("/actualizar_producto")
def update_product( id : int,producto : Producto):
    conexion = get_connection()
    conexion.Execute("UPDATE productos SET nombre = ?, stock = ?, precio = ? WHERE id = ?",
                        (producto.nombre, producto.stock, producto.precio, id))
    conexion.commit()
    conexion.close()
    return "dato actualizado"