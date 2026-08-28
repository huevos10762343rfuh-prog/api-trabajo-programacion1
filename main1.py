from fastapi import FastAPI
from pydantic import BaseModel


class nombre(BaseModel):
    name : str

app = FastAPI()

@app.post("/nombre")
def recibirnombre(nombre : nombre):
    return nombre


@app.get("/")
def read_root():
    return"hola, esta es la api de juan"


@app.get("/otra")
def otracosa():
    return "bienvenido a la otra ruta" 

#actividad : hacer un endpoint de tipo get y uno de post que guarde en memoria y que tenga como minimo 

menu =   [{"titulo":"lista de objetos"},
            {"nombre":"tomate","precio":"1000'","utilidad":"fruta"},
            {"nombre":"queso","precio":"2500","utilidad":"cheddar"},
            {"nombre":"papas","precio":"15000 x kg","utilidad":"papa"},#no tengo papá
            {"nombre":"milanesa","precio":"13000 x kg","utilidad":"milanesa"},
]
class nvmn(BaseModel):
    nombre : str
    precio : float
    utilida : str

@app.get("/menu")
def menu():
    return menu

@app.post("/agregar al menu")
def recibircomida(comida:nvmn):
    menu.append(comida)
    return "el alimento se agrego al menu"