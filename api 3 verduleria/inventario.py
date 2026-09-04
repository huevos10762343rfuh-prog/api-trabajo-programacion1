from modelos import Producto
import sqlite3


class inventario:
    def __init__(self):
        pass

    def agrega_producto(self, Producto: Producto, conexion: sqlite3.Connection) ->str:
        conexion.execute("INSERT INTO productos(nombre, stock, precio) VALUES (?,?,?)",
        (Producto.nombre, Producto.stock, Producto.precio))
        return  f"dato subido{Producto}"

    def leer_inventario(self,conexion : sqlite3.Connection) ->str:
        res = conexion.execute("SELECT * FROM productos").fetchall()
        return ([dict(item)for item in res])

    def eliminar_producto(self,id : int, conexion:sqlite3.Connection) ->str:
        conexion.execute("DELETE FROM productos WHERE id = ?",(id,))
        return f"se elimmino el producto de id {id}"

    def actualizar_producto(self, Producto: Producto, conexion: sqlite3.Connection) -> str:
        conexion.Execute("UPDATE productos SET nombre = ?, stock = ?, precio = ? WHERE id = ?",(Producto.nombre, Producto.stock, Producto.precio, id))
        return "dato actualizado"