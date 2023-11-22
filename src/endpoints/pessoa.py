from fastapi import FastAPI, APIRouter, Depends, HTTPException
from src.helpers.auth_valid import authenticate_user
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.schemas.user import CreateUserSchema
from src.schemas.pessoa import CreatePessoaSchema
from src.models.pessoa import Pessoa
from src.models.user import User

router = APIRouter()

@router.post("/cadastrar")
async def cadastrar(pessoa: CreatePessoaSchema, user: CreateUserSchema, db: Session = Depends(get_db)):
    create_user = User(email=user.email, hashed_password=user.password)
    db.add(create_user)
    create_pessoa = Pessoa(nome=pessoa.nome, sobrenome=pessoa.sobrenome, cidade=pessoa.cidade, estado=pessoa.estado, data_aniversario=pessoa.data_aniversario, id_usuario=create_user.id)
    db.add(create_pessoa)
    db.add(create_pessoa)
    db.commit()
    db.refresh(create_user)
    db.refresh(create_pessoa)
    return {"Mensagem": "Usuário criado com sucesso !"}

@router.get("/", dependencies=[Depends(authenticate_user)])
async def Listar_Pessoas():
     return db.query(Pessoa).all()
 
@router.get("/{pessoa_id}", dependencies=[Depends(authenticate_user)])
async def Listar_Pessoa(pessoa_id: int):
     pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa.id).first()
     if not pessoa:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     return pessoa