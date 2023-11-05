from fastapi import FastAPI
from fastapi import APIRouter
from src.endpoints.pessoa import router as pessoa_router
from src.endpoints.publicacao import router as publicacao_router

app = FastAPI()

app.include_router(pessoa_router, prefix="/pessoa", tags=["pessoa"])

app.include_router(publicacao_router, prefix="/publicacao", tags=["publicacao"])