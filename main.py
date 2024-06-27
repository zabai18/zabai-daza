#esto es un ejemplo
from fastapi import FastAPI
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
    



