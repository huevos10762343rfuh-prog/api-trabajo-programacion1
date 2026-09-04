import sqlite3
def get_connection():
    conan = sqlite3.connect("./tienda.db")
    conan.row_factory = sqlite3.Row
    try:
        yield conan
    finally:
        conan.commit()
        conan.close()

def initdb():
    conan =  sqlite3.connect("tienda.db")
    cursor = conan.cursor()
    conan.execute("CREATE TABLE IF NOT EXISTS productos(id INTEGER PRIMARY KEY, nombre TEXT, stock INTEGER, precio REAL)")
    conan.commit()
    conan.close()