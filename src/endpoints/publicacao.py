from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.post("/publicar")
async def root():
     return {"bearer": "LOGADO"}