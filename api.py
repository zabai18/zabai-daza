from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/libros/", response_model=schemas.Libro)
async def create_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    query = text("INSERT INTO libros (autor, titulo, estado) VALUES (:autor, :titulo, :estado)")
    db.execute(query, {"autor": libro.autor, "titulo": libro.titulo, "estado": libro.estado})
    db.commit()
    last_id_query = text(from fastapi import FastAPI
from pydantic import BaseModel,constr, field_validator
from typing import List, Any

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}

libros = []
usuarios = []
libros_usuarios = []

class Usuario(BaseModel):
    nombre: str
    id: int

    def crear(self):
        if self.id is None:
            self.id = len(libros) + 1
            usuarios.append(self)
            return self

class Libro(BaseModel):
    titulo: str
    autor: str
    estado: int = 0
    id: int = None

    def tomar_libro(self, libro_id, usuario_id, tiempo_prestado):
        for usuario in usuarios:
            if usuario.id == usuario.id:
                for libro in libros:
                    if libro_id == libro_id:
                        libro_user = LibroUsuario(
                            tiempo_prestado=tiempo_prestado,
                            usuario_id=usuario_id,
                            libro_id=libro_id
                        )
                    libros_usuarios.append(libro_user)
                    libro.estado = 1
                    return True
                return False
@classmethod
def tomar_libro(self,libro_id, usuario_id,tiempo_prestado):
    for usuario  in usuarios:
        if usuario.id == usuario.id:
            for libro in libros:
                if libro_id == libro_id:
                    for libros_usuario in libros_usuarios:
                        if libros_usuarios.usuariosid==usuario_id and libros_usuario.libro.id:
                            libros_usuarios.remove(libros_usuarios)
                            libro.estado= 0
                            return True
    return False


    @field_validator("autor")
    def check_autor(cls, v: str):
        if len(v) < 3 or len(v) > 20:
            raise ValueError("el autor debe tener " "minumo 3 caracteres "
                             "y maximo 3 caracteres")



    def guardar(self):
        if self.id is None:
            self.id = len(libros) + 1
            libros.append(self)
        else:
            for libro in libros:
                if libro.id == self.id:
                    libro.autor = self.autor
                    libro.titulo= self.titulo
                    libro.estado = self.estado
        return self

    @classmethod
    def actualizar(self):
        for i in range(len(usuarios) - 1):
            if self.id == usuarios[i].id:
                usuarios[i].documento = self.documento
                usuarios[i].nombre = self.nombre
                return self
        return None

    @classmethod
    def consultar(cls, libro_id):
        for libro in libros:
            if libro.id == libro_id:
                return libro
        return None

    @classmethod
    def eliminar(cls,libro_id):
        for libro in libros:
            if  libro.id == libro_id:
                libro.remove(libro)
                return True
            return False

    @classmethod
    def consultar_todos(cls):
        return libros



class LibroUsuario():
    usuario_id : int
    libro_id : int
    tiempo_prestamo : int

    def init(self):
        pass

    def __init__(self,
                 usuario_id: int,
                 libro_id: int,
                 tiempo_prestamo: int):
        self.libro_id = libro_id
        self.usuario_id = usuario_id


@app.post("/libro")
async def crear_libro(libro: Libro):
    return libro.guardar()

@app.put("/libro")
async def editar_libro(libro:libros):
     return Libro.editar()



@app.get("/libros")
async def consultar_libro():
    return Libro.consultar_todos()


@app.get("/libro/{libro_id}")
async def consultar(libro_id : int):
    return Libro.consultar(libro_id)

@app.delete("/libro/{libro_id}")
async def eliminar_libro(libro_id : int):
    return Libro.eliminar(libro_id)



if __name__ == "_main_":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    last_id = db.execute(last_id_query).scalar()
    return {**libro.dict(), "id": last_id}

@app.get("/libros/", response_model=List[schemas.Libro])
async def read_libros(db: Session = Depends(get_db)):
    query = text("SELECT * FROM libros")
    result = db.execute(query).fetchall()
    return [schemas.Libro(id=row.id, autor=row.autor, titulo=row.titulo, estado=row.estado) for row in result]

@app.post("/usuarios/", response_model=schemas.Usuario)
async def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    query = text("INSERT INTO usuarios (nombre, documento) VALUES (:nombre, :documento)")
    db.execute(query, {"nombre": usuario.nombre, "documento": usuario.documento})
    db.commit()
    last_id_query = text("SELECT LAST_INSERT_ID()")
    last_id = db.execute(last_id_query).scalar()
    return {**usuario.dict(), "id": last_id}

@app.get("/usuarios/", response_model=List[schemas.Usuario])
async def read_usuarios(db: Session = Depends(get_db)):
    query = text("SELECT * FROM usuarios")
    result = db.execute(query).fetchall()
    return [schemas.Usuario(id=row.id, nombre=row.nombre, documento=row.documento) for row in result]

@app.post("/libros_usuarios/", response_model=schemas.LibroUsuario)
async def create_libro_usuario(libro_usuario: schemas.LibroUsuarioCreate, db: Session = Depends(get_db)):
    query = text("""
        INSERT INTO libros_usuarios (usuario_id, libro_id, tiempo_prestamo) 
        VALUES (:usuario_id, :libro_id, :tiempo_prestamo)
    """)
    db.execute(query, {
        "usuario_id": libro_usuario.usuario_id,
        "libro_id": libro_usuario.libro_id,
        "tiempo_prestamo": libro_usuario.tiempo_prestamo,
    })
    db.commit()
    last_id_query = text("SELECT LAST_INSERT_ID()")
    last_id = db.execute(last_id_query).scalar()
    return {**libro_usuario.dict(), "id": last_id}

@app.get("/libro/{libro_id}", response_model=schemas.Libro)
async def read_libro(libro_id: int, db: Session = Depends(get_db)):
    query = text("SELECT * FROM libros WHERE id = :libro_id")
    libro = db.execute(query, {"libro_id": libro_id}).fetchone()
    if not libro:
        raise HTTPException(status_code=404, detail="Libro not found")
    return schemas.Libro(id=libro.id, autor=libro.autor, titulo=libro.titulo, estado=libro.estado)


@app.get("/libros/search/", response_model=List[schemas.Libro])
async def search_libros(query: str, db: Session = Depends(get_db)):
    search_query = text("SELECT * FROM libros WHERE titulo LIKE :query")
    result = db.execute(search_query, {"query": f"%{query}%"}).fetchall()
    return [schemas.Libro(id=row.id, autor=row.autor,
                          titulo=row.titulo, estado=row.estado) for row in result]


@app.put("/libro/{libro_id}", response_model=schemas.Libro)
async def update_libro(libro_id: int, libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    query = text("""
        UPDATE libros SET autor = :autor, titulo = :titulo, estado = :estado 
        WHERE id = :libro_id
    """)
    db.execute(query, {"autor": libro.autor, "titulo": libro.titulo, "estado": libro.estado, "libro_id": libro_id})
    db.commit()
    return {**libro.dict(), "id": libro_id}

@app.delete("/libro/{libro_id}", response_model=dict)
async def delete_libro(libro_id: int, db: Session = Depends(get_db)):
    query = text("DELETE FROM libros WHERE id = :libro_id")
    db.execute(query, {"libro_id": libro_id})
    db.commit()
    return {"message": "Libro eliminado"}


