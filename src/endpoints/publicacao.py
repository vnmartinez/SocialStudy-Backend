from fastapi import FastAPI

router = FastAPI()

@router.post("/publicar")
async def root():
     return {"bearer": "LOGADO"}