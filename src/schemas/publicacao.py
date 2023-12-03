from pydantic import BaseModel
from src.schemas.pessoa import PessoaGet
from typing import List

class PublicacaoSchema(BaseModel):
    id : int
    titulo : str 
    descricao : str
    link : str
    
class PublicacaoLista(BaseModel):
    publicacoes: List[PublicacaoSchema]
    
class PublicacaoPessoa(BaseModel):
    id : int
    titulo : str 
    descricao : str
    link : str
    like_count :int
    pessoa : PessoaGet

class PublicacaoPessoaLista(BaseModel):
    publicacoes: List[PublicacaoPessoa]
    
class PublicacaoCreate(BaseModel):
    titulo : str
    descricao : str
    link : str
    