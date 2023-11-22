from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    titulo : str
    titulo : str 
    descricao : str
    link : str
    id_pessoa : int