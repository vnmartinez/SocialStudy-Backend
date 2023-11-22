from fastapi import FastAPI, APIRouter, Depends, HTTPException
from src.helpers.auth_valid import authenticate_user
from src.schemas.publicacao import PublicacaoSchema    
from src.models.publicacao import Publicacao
from sqlalchemy.orm import Session
from src.dependencies import get_db

router = APIRouter()

@router.post("/publicar", dependencies=[Depends(authenticate_user)])
async def Cria_Publicacao(publicacao: PublicacaoSchema, db: Session = Depends(get_db)):
     criar_publicacao = Publicacao(titulo=publicacao.titulo, conteudo=publicacao.conteudo)
     db.add(criar_publicacao)
     db.commit()
     db.refresh(criar_publicacao)
     return criar_publicacao

@router.get("/", dependencies=[Depends(authenticate_user)])
async def listar_Publicacoes(db: Session = Depends(get_db)):
     return db.query(Publicacao).all()

@router.get("/{publicacao_id}", dependencies=[Depends(authenticate_user)])
async def Listar_Publicacao(publicacao_id: int, db: Session = Depends(get_db)):
     publicacao = db.query(Publicacao).filter(Publicacao.id == publicacao_id).first()
     if not publicacao:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     return publicacao