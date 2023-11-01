from fastapi import FastAPI
from fastapi import APIRouter

router = FastAPI()

@router.post("/auth")
async def root():
    return {"bearer": "LOGADO"}