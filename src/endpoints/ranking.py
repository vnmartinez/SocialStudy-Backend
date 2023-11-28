from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, joinedload
from src.helpers.auth_valid import oauth2_scheme, get_current_user
from src.dependencies import get_db
from src.models.publicacao_lida import PublicacaoLida

router = APIRouter()

@router.get("/")
async def Listar_Ranking(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    lista_ranking = db.query()
    return {"ranking": lista_ranking}