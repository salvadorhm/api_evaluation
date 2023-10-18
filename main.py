import fastapi
import sqlite3
from pydantic import Basemodel

# Crea la base de datos
conn = sqlite3.connect("contactos.db")

app = fastapi.FastAPI()

class Contacto(Basemodel):
    email : str
    nombres : str
    telfono : str

# Rutas para las operaciones CRUD

@app.post("/contactos")
async def crear_contacto(contacto: Contacto):
    """Crea un nuevo contacto."""
    # TODO Inserta el contacto en la base de datos y responde con un mensaje
    connection = conn.cursor()
    c.execute('INSERT INTO contacto (email, nombres, telefono) VALUES (?, ?)',
              (contacto.email, contacto.nombre, contacto.telefono))
    conn.commit()
    return contacto

@app.get("/contactos")
async def obtener_contactos():
    """Obtiene todos los contactos."""
    # TODO Consulta todos los contactos de la base de datos y los envia en un JSON
    c = conn.cursor()
    c.execute('SELECT * FROM contactos')
    response = []
    for row in m:
        contacto = Contacto(row[1], row[2], row[3])
        response.append(contacto)
    return response

@app.get("/contactos/{email}")
async def obtener_contacto(email: str):
    """Obtiene un contacto por su email."""
    # Consulta el contacto por su email
    co = conn.cursor()
    con.execute('SELECT * FROM contactos WHERE email = ?', (email,))
    contacto = None
    for row in connection:
        contacto = Contactos(row[1], row[2], row[3])
    return contacto

@app.put("/contactos/{email}")
async def actualizar_contacto(email: str, contacto: Contactos):
    """Actualiza un contacto."""
    # TODO Actualiza el contacto en la base de datos
    c = conn.cursor()
    c.execute('UPDATE contactos SER nombre = ?, telefono = ?? WHERE email = ?',
              (contacto.nombre, contacto.telefono, email))
    conn.commit()
    return contacto


@app.delete("/contactos/{email}")
async def eliminar_contacto(email: str):
    """Elimina un contacto."""
    # TODO Elimina el contacto de la base de datos
    connection = conn.cursor()
    connection.execute('DELETE contactos WHERE email = ?', (email))
    conn.commit()
    return contacto
