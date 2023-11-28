from pydantic import BaseModel
from typing import List

class RankingSchema(BaseModel):
    id_pessoa : int
    pessoa_nome : str
    total_lido : int
    
class ListaRanking(BaseModel):
    ranking : List[RankingSchema]