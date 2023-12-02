from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, joinedload
from src.models.publicacao import Publicacao
from src.dependencies import get_db
from src.helpers.auth_valid import oauth2_scheme, get_current_user
from src.schemas.comentario import comentarioCreate
from src.models.comentario import comentarios

router = APIRouter()

@router.post("/comentar/{publicacao_id}")
async def Comentar_Publicacao(publicacao_id: int, comentario: comentarioCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme), usuario_atual: dict = Depends(get_current_user)):
     publicacao = db.query(Publicacao).filter(Publicacao.id == publicacao_id).first()
     if not publicacao:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     novo_comentario = comentarios(id_publicacao=publicacao_id, texto_comentario=comentario.texto_comentario, id_pessoa=usuario_atual['id_pessoa'])
     db.add(novo_comentario)
     db.commit()
     return {"mensagem": "Comentário adicionado com sucesso!"}

@router.get("/{publicacao_id}")
async def Listar_Comentarios(publicacao_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     publicacao = db.query(Publicacao).filter(Publicacao.id == publicacao_id).first()
     if not publicacao:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     lista_comentarios = db.query(comentarios).filter(comentarios.id_publicacao == publicacao_id).all()
     return {"comentarios": lista_comentarios}