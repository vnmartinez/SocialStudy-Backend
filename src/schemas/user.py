from pydantic import BaseModel
from pydantic.networks import EmailStr

class CreateUserSchema(BaseModel):
    email: EmailStr
    password: str