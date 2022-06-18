from typing import Optional
from pydantic import BaseModel, Field

class CarrosSchema(BaseModel):
    codigo: int = Field(None, title="Codigo do carro")
    marca: str = Field(None, title="Marca do carro")
    ano: int = Field(None, title="Ano do carro")
    modelo: str = Field(None, title="Modelo do carro")
    categoria: str = Field(None, title="Categoria do carro")

    class Config:
        orm_mode = True
