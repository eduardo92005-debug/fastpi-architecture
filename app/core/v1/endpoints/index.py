from fastapi import APIRouter
from schemas.carros import CarrosSchema
from models.carros import Carros, getAllCarros
from typing import Dict,List

router = APIRouter()

@router.get('/carros', tags=['carros'], response_model=List[CarrosSchema])
def list_carros() -> List[CarrosSchema]:
    return getAllCarros()