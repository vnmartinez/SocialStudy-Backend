from fastapi import FastAPI
from fastapi import APIRouter
from src.endpoints.pessoa_endpoints import router as pessoa_router
from src.endpoints.publicacao_endpoints import router as publicacao_router
from src.endpoints.data_controls import router as data_controls_router

app = FastAPI()

app.include_router(pessoa_router, prefix="/pessoa", tags=["pessoa"])
app.include_router(publicacao_router, prefix="/publicacao", tags=["publicacao"])
app.include_router(data_controls_router, prefix="/data-controls", tags=["data-controls"])