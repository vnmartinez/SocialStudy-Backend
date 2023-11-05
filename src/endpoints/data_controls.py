from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from databases import databases

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