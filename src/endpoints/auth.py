from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.post("/auth")
async def root():
    return {"bearer": "LOGADO"}