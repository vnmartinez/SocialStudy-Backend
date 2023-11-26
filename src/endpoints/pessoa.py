from fastapi import FastAPI, APIRouter, Depends, HTTPException
from src.helpers.auth_valid import oauth2_scheme
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.schemas.user import CreateUserSchema
from src.schemas.pessoa import CreatePessoaSchema, PessoaLista
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

@router.get("/", response_model=PessoaLista)
async def Listar_Pessoas(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     lista_pessoas = db.query(Pessoa).all()
     return {"pessoas": lista_pessoas} 
 
@router.get("/{pessoa_id}", response_model=CreatePessoaSchema)
async def Listar_Pessoa_Por_ID(pessoa_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
     pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa.id).first()
     if not pessoa:
          raise HTTPException(status_code=404, detail="Publicação não encontrada")
     return pessoa