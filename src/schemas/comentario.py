from pydantic import BaseModel
from datetime import date

class comentarioCreate(BaseModel):
    texto_comentario : str