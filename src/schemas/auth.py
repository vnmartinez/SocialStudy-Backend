from pydantic import BaseModel
from pydantic.networks import EmailStr

class LoginSchema(BaseModel):
    email: EmailStr 
    password: str