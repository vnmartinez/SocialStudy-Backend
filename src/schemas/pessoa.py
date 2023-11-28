from pydantic import BaseModel
from datetime import date
from typing import List 
class CreatePessoaSchema(BaseModel):
    nome : str
    sobrenome : str
    cidade : str
    estado : str
    data_aniversario : date
    
class PessoaPorEmailSchema(BaseModel):
    email : str
    
class PessoaList(BaseModel):
    lista : List[CreatePessoaSchema]