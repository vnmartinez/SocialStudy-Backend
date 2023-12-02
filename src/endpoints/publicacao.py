from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from src.schemas.publicacao import PublicacaoSchema, PublicacaoLista    
from src.schemas.comentario import comentarioCreate
from src.models.publicacao import Publicacao
from src.models.comentario import comentarios
from src.models.pessoa import Pessoa
from sqlalchemy.orm import Session, joinedload
from src.dependencies import get_db
from src.helpers.auth_valid import oauth2_scheme, get_current_user

router = APIRouter()

@router.post("/publicar")
async def Cria_Publicacao(publicacaoSchema: PublicacaoSchema, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme),  usuario_atual: dict = Depends(get_current_user)):
     publicacao_criada = Publicacao(titulo=publicacaoSchema.titulo, descricao=publicacaoSchema.descricao, link=publicacaoSchema.link, id_pessoa=usuario_atual['id_pessoa'])
     
     db.add(publicacao_criada)
     db.commit()
     db.refresh(publicacao_criada)
     
     if not publicacao_criada:
          raise HTTPException(status_code=400, detail="Erro ao criar publicação")
     return {"mensagem": "Publicação criada com sucesso!"}

@router.get("", response_model=PublicacaoLista)
async def Listar_Publicacoes(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     lista_publicacoes = db.query(Publicacao).join(Pessoa, Publicacao.id_pessoa == Pessoa.id).options(joinedload(Publicacao.pessoa)).all()
     if not lista_publicacoes:
          raise HTTPException(status_code=404, detail="Nenhuma publicação encontrada")
     return lista_publicacoes

@router.get("/{publicacao_id}")
async def Listar_Publicacao_por_ID(publicacao_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     publicacao = db.query(Publicacao).join(Pessoa, Publicacao.id_pessoa == Pessoa.id).options(joinedload(Publicacao.pessoa)).filter(Publicacao.id == publicacao_id).first()
     if not publicacao:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     return publicacao

@router.delete("/{publicacao_id}")
async def Deletar_Publicacao(publicacao_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     publicacao = db.query(Publicacao).filter(Publicacao.id == publicacao_id).first()
     if not publicacao:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     db.delete(publicacao)
     db.commit()
     return {"mensagem": "Publicação deletada com sucesso!"}

@router.put("/{publicacao_id}")
async def Atualizar_Publicacao(publicacao_id: int, publicacao: PublicacaoSchema, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     publicacao_atualizada = db.query(Publicacao).filter(Publicacao.id == publicacao_id).first()
     if not publicacao_atualizada:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     publicacao_atualizada.titulo = publicacao.titulo
     publicacao_atualizada.descricao = publicacao.descricao
     publicacao_atualizada.link = publicacao.link
     db.commit()
     db.refresh(publicacao_atualizada)
     return {"mensagem": "Publicação atualizada com sucesso!"}

@router.get("/listar/{pessoa_id}")
async def Listar_Publicacoes_Por_Usuario(pessoa_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa_id).all()
     if not pessoa:
          raise HTTPException(status_code=404, detail="Usuário não encontrado")
     lista_publicacoes = db.query(Publicacao).filter(Publicacao.id_pessoa == pessoa_id).all()
     return {"publicacoes": lista_publicacoes}

@router.post("/ler/{publicacao_id}")
async def Ler_Publicacao(publicacao_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme), usuario_atual: dict = Depends(get_current_user)):
     publicacao = db.query(Publicacao).filter(Publicacao.id == publicacao_id).first()
     if not publicacao:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     publicacao_lida = PublicacaoLida(id_publicacao=publicacao_id, id_pessoa=usuario_atual['id_pessoa'])
     db.add(publicacao_lida)
     db.commit()
     db.refresh(publicacao_lida)
     return {"mensagem": "Publicação lida com sucesso!"}