from pydantic import BaseModel

##Modelo de producto
class Crea_producto(BaseModel):
    nombre: str
    descripcion: str
    precio: float


##Modelo de inventario
class Crea_inventario(BaseModel):
    id_producto: int
    id_tienda: int
    stock: int

##Modelo de inventario
class tiendaModel(BaseModel):
    id_direccion: int
    nombre: str
    estado: str