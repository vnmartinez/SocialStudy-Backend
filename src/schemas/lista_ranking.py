from pydantic import BaseModel

class ListaRanking(BaseModel):
    id_pessoa : int
    pessoa_nome : str
    total_lido : int
    
class RankingSchema(BaseModel):
    ranking : list[ListaRanking]