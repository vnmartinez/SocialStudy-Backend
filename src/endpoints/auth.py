from src.schemas.user import CreateUserSchema
from src.dependencies import get_db
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.user import User
from src.helpers.jwt import create_access_token
from src.schemas.auth import LoginSchema
from src.helpers.hash_password import check_password

router = APIRouter()

@router.post("/login")
async def login(login: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    if not check_password(login.password.encode('utf8'), user.hashed_password.encode('utf8')):
        raise HTTPException(status_code=400, detail="Senha incorreta")
    token = create_access_token(user.email)
    return {"token": token}