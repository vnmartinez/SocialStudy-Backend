from pydantic import BaseModel
from typing import List

class RankingLeituraSchema(BaseModel):
    id_pessoa : int
    pessoa_nome : str
    total_lido : int
    
class ListaRankingLeitura(BaseModel):
    ranking_leitura : List[RankingLeituraSchema]
    
class RankingPublicacaoSchema(BaseModel):
    id_pessoa : int
    pessoa_nome : str
    total_publicado : int

class ListaRankingPublicacao(BaseModel):
    ranking_publicacao : List[RankingPublicacaoSchema]