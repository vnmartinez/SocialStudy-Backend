from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/cadastrar")
async def root():
    return {"message": "Hello World"}