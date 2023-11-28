from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, joinedload
from src.models.publicacao import Publicacao
from src.dependencies import get_db
from src.helpers.auth_valid import oauth2_scheme

router = APIRouter()

@router.post("/{publicacao_id}")
async def Curtir_Publicacao(publicacao_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     publicacao = db.query(Publicacao).filter(Publicacao.id == publicacao_id).first()
     if not publicacao:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     publicacao.curtidas += 1
     db.commit()
     db.refresh(publicacao)
     return {"mensagem": "Publicação curtida com sucesso!"}

@router.put("/{publicacao_id}")
async def Descurtir_Publicacao(publicacao_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     publicacao = db.query(Publicacao).filter(Publicacao.id == publicacao_id).first()
     if not publicacao:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     publicacao.curtidas -= 1
     db.commit()
     db.refresh(publicacao)
     return {"mensagem": "Publicação descurtida com sucesso!"}