from src.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from src.models.user import User

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    sobrenome = Column(String)
    cidade = Column(String)
    estado = Column(String)
    data_aniversario = Column(Date)
    id_usuario = Column(Integer, ForeignKey("users.id"))