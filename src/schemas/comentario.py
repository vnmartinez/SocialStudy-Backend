from pydantic import BaseModel
from datetime import date
from typing import List

class comentarioCreate(BaseModel):
    texto_comentario : str
    
class getComentario(BaseModel):
    id : int
    texto_comentario :str
    id_pessoa : int
    nome_pessoa : str
    id_publicacao  : int
    
class getComentarioLista(BaseModel):
    comentarios : List[getComentario]