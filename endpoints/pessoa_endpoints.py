from fastapi import FastAPI
from fastapi import APIRouter

router = FastAPI()

@router.get("/cadastrar")
async def root():
    return {"message": "Hello World"}