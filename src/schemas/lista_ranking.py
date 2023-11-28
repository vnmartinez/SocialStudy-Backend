from pydantic import BaseModel
from typing import List

class ListaRanking(BaseModel):
    id_pessoa : int
    pessoa_nome : str
    total_lido : int
    
class RankingSchema(BaseModel):
    ranking : list[ListaRanking]