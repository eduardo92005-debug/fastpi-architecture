from env import Base, session
from dependencies.base_dependencies import *

class Carros(Base):
    __tablename__ = 'carros' #obrigatorio nome tabela
    codigo = Column(Integer, primary_key=True)
    marca = Column(String(50))
    ano = Column(Integer)
    modelo = Column(String(30))
    categoria = Column(String(30))
    def __init__(self, codigo, marca, categoria, modelo, ano):
        self.codigo = codigo
        self.marca = marca
        self.ano = ano
        self.categoria = categoria
        self.modelo = modelo

def getAllCarros():
    return session.query(Carros).all()