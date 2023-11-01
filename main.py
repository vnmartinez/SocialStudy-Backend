from fastapi import FastAPI
from fastapi import APIRouter
from endpoints.pessoa_endpoints import router as pessoa_router

app = FastAPI()

app.include_router(pessoa_router, prefix="/pessoa", tags=["pessoa"])
