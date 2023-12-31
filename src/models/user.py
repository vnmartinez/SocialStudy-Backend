from src.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import EmailType
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(EmailType, unique=True, index=True)
    hashed_password = Column(String)