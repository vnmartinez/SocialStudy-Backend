from pydantic import BaseModel, HttpUrl

class PublicacaoSchema(BaseModel):
    titulo : str
    titulo : str 
    descricao : str
    link : HttpUrl