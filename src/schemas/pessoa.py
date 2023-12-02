from pydantic import BaseModel
from datetime import date
from typing import List 
class CreatePessoaSchema(BaseModel):
    nome : str
    sobrenome : str
    cidade : str
    estado : str
    data_aniversario : date
          
class PessoaGet(BaseModel):
    id : int
    nome : str
    sobrenome : str
    cidade : str
    estado : str
    data_aniversario : date

class PessoasList(BaseModel):
    pessoas: List[PessoaGet]
    