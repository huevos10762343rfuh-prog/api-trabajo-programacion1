import sqlite3

def get_connection():
    conan = sqlite3.connect("./tienda.db")
    conan.row_factory = sqlite3.Row
    return conan        


def initdb():
    conexion = get_connection()
    conexion.execute("CREATE TABLE IF NOT EXISTS productos(id INTEGER PRIMARY KEY, nombre TEXT, stock INTEGER, precio REAL)")
    conexion.commit()
    conexion.close()
