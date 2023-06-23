from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Pelicula(BaseModel):
    titulo: str
    año: int
    descripcion: str
    director: str


peliculas = [
    Pelicula(titulo="El Padrino", año=1972,
             descripcion="Una historia sobre la familia criminal Corleone en 1940s Nueva York.",
             director="Francis Ford Coppola"),
    Pelicula(titulo="Pulp Fiction", año=1994,
             descripcion="Las vidas de dos matones de la mafia, un boxeador, la esposa de un gángster y un par de ladrones se entrelazan en cuatro cuentos de violencia y redención.",
             director="Quentin Tarantino"),
    Pelicula(titulo="El caballero de la noche", año=2008,
             descripcion="Cuando el Joker emerge de su misterioso pasado, siembra el caos y la destrucción en Gotham.",
             director="Christopher Nolan"),
    Pelicula(titulo="Forrest Gump", año=1994,
             descripcion="La vida de Forrest Gump, desde su infancia hasta convertirse en un héroe de guerra y un hombre de negocios.",
             director="Robert Zemeckis"),
    Pelicula(titulo="Origen", año=2010,
             descripcion="Un ladrón experto en el arte de extraer información valiosa de la mente de las personas mientras duermen es contratado para realizar una tarea aparentemente imposible.",
             director="Christopher Nolan"),
    Pelicula(titulo="El club de la pelea", año=1999,
             descripcion="Un empleado de oficina insomne y un jabonero carismático forman un club de lucha clandestino que se convierte en mucho más.",
             director="David Fincher"),
    Pelicula(titulo="Matrix", año=1999,
             descripcion="Un programador informático descubre que el mundo en el que vive es una simulación controlada por una inteligencia artificial.",
             director="Lana y Lilly Wachowski"),
    Pelicula(titulo="Gladiador", año=2000,
             descripcion="Un general romano traicionado es condenado a la esclavitud y se convierte en gladiador para vengarse de los que lo traicionaron.",
             director="Ridley Scott"),
    Pelicula(titulo="El señor de los anillos: El retorno del rey", año=2003,
             descripcion="Gandalf y Aragorn lideran al Mundo de los Hombres contra el ejército de Sauron, mientras Frodo y Sam se acercan al Monte del Destino con el Anillo Único.",
             director="Peter Jackson"),
    Pelicula(titulo="La lista de Schindler", año=1993,
             descripcion="El empresario Oskar Schindler salva a más de mil refugiados judíos del Holocausto empleándolos en su fábrica.",
             director="Steven Spielberg")
]


@app.get("/", response_model=List[Pelicula])
async def listar_peliculas():
    return peliculas


@app.get("/peliculas/{pelicula_id}", response_model=Pelicula)
async def obtener_pelicula(pelicula_id: int):
    if pelicula_id < 0 or pelicula_id >= len(peliculas):
        return None
    return peliculas[pelicula_id]


@app.post("/peliculas", response_model=Pelicula)
async def crear_pelicula(pelicula: Pelicula):
    peliculas.append(pelicula)
    return pelicula


@app.put("/peliculas/{pelicula_id}", response_model=Pelicula)
async def actualizar_pelicula(pelicula_id: int, pelicula: Pelicula):
    if pelicula_id < 0 or pelicula_id >= len(peliculas):
        return None
    peliculas[pelicula_id] = pelicula
    return pelicula


@app.delete("/peliculas/{pelicula_id}", response_model=Pelicula)
async def eliminar_pelicula(pelicula_id: int):
    if pelicula_id < 0 or pelicula_id >= len(peliculas):
        return None
    pelicula_eliminada = peliculas.pop(pelicula_id)
    return pelicula_eliminada
