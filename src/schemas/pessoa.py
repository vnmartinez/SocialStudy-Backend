from pydantic import BaseModel
from datetime import date

class CreatePessoaSchema(BaseModel):
    nome : str
    sobrenome : str
    cidade : str
    estado : str
    data_aniversario : date
    
class PessoaPorEmailSchema(BaseModel):
    email : str