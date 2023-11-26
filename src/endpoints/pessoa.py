from fastapi import FastAPI, APIRouter, Depends, HTTPException
from src.helpers.auth_valid import oauth2_scheme
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.schemas.user import CreateUserSchema
from src.schemas.pessoa import CreatePessoaSchema
from src.models.pessoa import Pessoa
from src.models.user import User
from src.helpers.hash_password import hash_password

router = APIRouter()

@router.post("/cadastrar")
async def cadastrar(pessoa: CreatePessoaSchema, user: CreateUserSchema, db: Session = Depends(get_db)):
    verifica_email = db.query(User).filter(User.email == user.email).first()
    if verifica_email:
       raise HTTPException(status_code=400, detail="Email já cadastrado")
    create_user = User(email=user.email, hashed_password=hash_password(user.password).decode('utf8'))
    db.add(create_user)
    db.commit()
    id_usuario = db.query(User.id).filter(User.email == user.email).first()
    create_pessoa = Pessoa(nome=pessoa.nome, sobrenome=pessoa.sobrenome, cidade=pessoa.cidade, estado=pessoa.estado, data_aniversario=pessoa.data_aniversario, id_usuario=id_usuario.id)
    db.add(create_pessoa)
    db.commit()
    return {"Mensagem": "Usuário criado com sucesso !"}

@router.get("/")
async def Listar_Pessoas(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     return db.query(Pessoa).all()
 
@router.get("/{pessoa_id}")
async def Listar_Pessoa_Por_ID(pessoa_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa.id).first()
     if not pessoa:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     return pessoa

@router.get("/{email_usuario}")
async def Listar_Pessoa_Por_Email(email_usuario: str, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     user.id = db.query(User.id).filter(User.email == email_usuario).first()
     if not user.id:
          raise HTTPException(status_code=404, detail="Usuário não encontrado")
     pessoa = db.query(Pessoa).filter(Pessoa.id_usuario == user.id).first()
     if not pessoa:
          raise HTTPException(status_code=404, detail="Pessoa não encontrada")
     return pessoa

@router.get("/id_usuario")
async def Listar_Pessoa_Por_ID_Usuario(id_usuario: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme), usuario_atual: dict = Depends(get_current_user)):
     return {"id_usuario": usuario_atual['id']}