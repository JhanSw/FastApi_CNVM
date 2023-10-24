from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[str]
    nombre_usuario: str
    numero_doc_usuario: int
    usuario: str
    contrasenia_usuario: str

class DataUser(BaseModel):
    usuario: str
    contrasenia_usuario: str

class ClienteSchema(BaseModel):
    id: Optional[str]
    cliente: str
    nit:str
    solicitante: str
    cargo: str
    direccion: str
    municipio: str
    telefono: str
    fax: str
    consecutivo: str
    observaciones: str
        