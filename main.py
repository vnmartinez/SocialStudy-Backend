from fastapi import FastAPI
from fastapi import APIRouter
from src.endpoints.pessoa import router as pessoa_router
from src.endpoints.publicacao import router as publicacao_router
from src.endpoints.auth import router as auth_router
from src.database import  Base, engine
from src.models.user import User
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
   "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["login"])

app.include_router(pessoa_router, prefix="/pessoas", tags=["pessoa"])

app.include_router(publicacao_router, prefix="/publicacoes", tags=["publicacao"])