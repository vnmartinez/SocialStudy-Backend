from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func 
from src.helpers.auth_valid import oauth2_scheme, get_current_user
from src.dependencies import get_db
from src.models.publicacao_lida import PublicacaoLida
from src.schemas.lista_ranking import RankingSchema, ListaRanking
from src.models.pessoa import Pessoa

router = APIRouter()

@router.get("", response_model=ListaRanking)
async def Listar_Ranking(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    lista_ranking = db.query(PublicacaoLida.id_pessoa,
                             func.concat(Pessoa.nome,' ',Pessoa.sobrenome).label("pessoa_nome"),
                             func.count(PublicacaoLida.id_pessoa).label("total_lido")
                            ).join(Pessoa, PublicacaoLida.id_pessoa == Pessoa.id
                            ).group_by(PublicacaoLida.id_pessoa, "pessoa_nome"
                            ).order_by(func.count(PublicacaoLida.id_pessoa).desc()).all()
    return {"ranking": lista_ranking}