from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func 
from src.helpers.auth_valid import oauth2_scheme, get_current_user
from src.dependencies import get_db
from src.models.publicacao_lida import PublicacaoLida
from src.models.publicacao import Publicacao
from src.schemas.lista_ranking import RankingLeituraSchema, ListaRankingLeitura, RankingPublicacaoSchema, ListaRankingPublicacao
from src.models.pessoa import Pessoa

router = APIRouter()

@router.get("/leitura", response_model=ListaRankingLeitura)
async def Listar_Ranking_Publicacao(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    lista_ranking = db.query(PublicacaoLida.id_pessoa,
                             func.concat(Pessoa.nome,' ',Pessoa.sobrenome).label("pessoa_nome"),
                             func.count(PublicacaoLida.id_pessoa).label("total_lido")
                            ).join(Pessoa, PublicacaoLida.id_pessoa == Pessoa.id
                            ).group_by(PublicacaoLida.id_pessoa, "pessoa_nome"
                            ).order_by(func.count(PublicacaoLida.id_pessoa).desc()).all()
    if not lista_ranking:
        raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
    return {"ranking_leitura": lista_ranking}

@router.get("/publicacao", response_model=ListaRankingPublicacao)
async def Listar_Ranking_Leitura(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    lista_ranking = db.query(Publicacao.id_pessoa,
                             func.concat(Pessoa.nome,' ',Pessoa.sobrenome).label("pessoa_nome"),
                             func.count(Publicacao.id_pessoa).label("total_publicado")
                            ).join(Pessoa, Publicacao.id_pessoa == Pessoa.id
                            ).group_by(Publicacao.id_pessoa, "pessoa_nome"
                            ).order_by(func.count(Publicacao.id_pessoa).desc()).all()
    if not lista_ranking:
        raise HTTPException(status_code=404, detail="Nenhum registro encontrado")
    return {"ranking_publicacao": lista_ranking}