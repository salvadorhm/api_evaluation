import fastapi
import sqlite3
from pydantic import BaseModel

# Crea la base de datos
conn = sqlite3.connect("contactos.db")

app = fastapi.FastAPI()

class Contacto(BaseModel):
    email : str
    nombre : str
    telefono : str

# Rutas para las operaciones CRUD

@app.post("/contactos")
async def crear_contacto(contacto: Contacto):
    """Crea un nuevo contacto."""
    # TODO Inserta el contacto en la base de datos y responde con un mensaje
    connection = conn.cursor()
    connection.execute('INSERT INTO contactos (email, nombre, telefono) VALUES (?, ?, ?)',
              (contacto.email, contacto.nombre, contacto.telefono))
    conn.commit()
    return contacto

@app.get("/contactos")
async def obtener_contactos():
    """Obtiene todos los contactos."""
    # TODO Consulta todos los contactos de la base de datos y los envia en un JSON
    connection = conn.cursor()
    connection.execute('SELECT * FROM contactos')
    response = []
    for row in connection:
        contacto = {"email":row[0],"nombre": row[1], "telefono" :row[2]}
        response.append(contacto)
    return response

@app.get("/contactos/{email}")
async def obtener_contacto(email: str):
    """Obtiene un contacto por su email."""
    # Consulta el contacto por su email
    connection = conn.cursor()
    connection.execute('SELECT * FROM contactos WHERE email = ?', (email,))
    contacto = None
    for row in connection:
        contacto = {"email":row[0],"nombre": row[1], "telefono" :row[2]}
    return contacto

@app.put("/contactos/{email}")
async def actualizar_contacto(email: str, contacto: Contacto):
    """Actualiza un contacto."""
    # TODO Actualiza el contacto en la base de datos
    connection = conn.cursor()
    connection.execute('UPDATE contactos SET nombre = ?, telefono = ? WHERE email = ?',
              (contacto.nombre, contacto.telefono, contacto.email))
    conn.commit()
    return contacto


@app.delete("/contactos/{email}")
async def eliminar_contacto(email: str):
    """Elimina un contacto."""
    # TODO Elimina el contacto de la base de datos
    connection = conn.cursor()
    connection.execute('DELETE FROM contactos WHERE email = ?', (email,))
    conn.commit()
    return  {"mensaje": "Contacto eliminado exitosamente"}
