from pydantic import BaseModel
from typing import List

class PublicacaoSchema(BaseModel):
    titulo : str 
    descricao : str
    link : str
    
class PublicacaoLista(BaseModel):
    publicacoes: List[PublicacaoSchema]