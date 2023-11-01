from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/create-tables")
async def create_tables():
    query = users.create()
    await database.execute(query)
    return {"message": "Tables created"}