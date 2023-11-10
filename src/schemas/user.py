from pydantic import BaseModel

class CreateUserSchema(BaseModel):
    email: str
    password: str